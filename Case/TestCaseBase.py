#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 21:46
# @Author  : fanyanpei

from abc import abstractmethod, ABCMeta
import typing
import inspect
from collections import OrderedDict

# 代表任何数据类型
T = typing.TypeVar("T")


# 元类 如果当前类以Test结尾则认为是测试类 需要有测试方法 否则没有要求
class OrderedMeta(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(metacls, name: str, bases, classdict: dict):
        d = dict(classdict)
        order = []
        if name.endswith("Test"):
            for memberName, member in classdict.items():
                if not inspect.isfunction(member):
                    continue
                if not memberName.endswith("Test"):
                    continue
                member._name = memberName
                order.append(memberName)
            d["methodNameListOrderedByDef"] = order
            if len(order) == 0:
                raise RuntimeError("在测试类%s中未发现测试方法，需要至少一个测试方法"%name)
        return type.__new__(metacls, name, bases, d)

class TestCaseBase(object, metaclass=OrderedMeta):

    def __new__(cls, *args, **kwargs):
        if cls is TestCaseBase:
            raise RuntimeError("TestCaseBase只能作为测试类的基类使用，不允许直接实例化")
        return super().__new__(cls)

    def __init__(self):
        self.a = 0
        # for method in self.__dir__():
        #     print(method)

    def fuck(self):
        pass

    # 测试前准备 只执行一次
    @abstractmethod
    def setUpClass(self):
        pass

    # 测试后清理 只执行一次
    @abstractmethod
    def tearDownClass(self):
        pass

    # 每个用例开始前都执行
    @abstractmethod
    def setUp(self):
        pass

    # 每个用例结束后都执行
    @abstractmethod
    def tearDown(self):
        pass

    def __assertEqual(self, actual: T, expect: T, assert_content=""):
        if actual != expect:
            raise AssertionError(assert_content)

    def __assertNotEqual(self, actual: T, expect: T, assert_content=""):
        if actual == expect:
            raise AssertionError(assert_content)

    def __assertIn(self, actual: T, expect: T, assert_content=""):
        if actual not in expect:
            raise AssertionError(assert_content)

    def __assertNotIn(self, actual: T, expect: T, assert_content=""):
        if actual in expect:
            raise AssertionError(assert_content)

    def requireEqual(self, actual: T, expect: T, assert_content=""):
        self.__assertEqual(actual, expect, assert_content)

    def requireNotEqual(self, actual: T, expect: T, assert_content=""):
        self.__assertNotEqual(actual, expect, assert_content)

    def requireIn(self, actual: T, expect: T, assert_content=""):
        self.__assertIn(actual, expect, assert_content)

    def requireNotIn(self, actual: T, expect: T, assert_content=""):
        self.__assertNotIn(actual, expect, assert_content)


if __name__ == '__main__':\
    test = TestCaseBase()
