#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 15:04
# @Author  : fanyanpei

import Case
import sys
import inspect
import os
import importlib
import pkgutil
import multiprocessing
import threading
from threading import Lock
from FrameConfigManager import FrameConfigManager
import time


class ExecuteBase(object):

    def __init__(self, testClsNameList: list = None):
        # todo
        self.threadNum = 5
        self.lock = Lock()
        self.casePath_todo = Case.__name__ + "."
        self.allClsList = self.collectAllTestClsByList(testClsNameList) if testClsNameList else self.collectAllTestCls()
        self.logName = FrameConfigManager.getConfigByKey("projectName") + "-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".log"
        self.logPath = FrameConfigManager.getConfigByKey("logAddress")

    # 获取所有Case 并import
    def importAllTestCase(self):
        for root, case_name, is_package in pkgutil.walk_packages(path=Case.__path__, prefix=self.casePath_todo):
            if not case_name.endswith("Test"):
                continue
            if is_package:
                continue
            # print(case_name)
            importlib.import_module(case_name)

    def collectAllTestClsByList(self, testClsNameList):
        # todo 收集所有输入的类 创建一个测试类列表
        pass

    # 获取所有测试类
    def collectAllTestCls(self) -> list:
        self.importAllTestCase()
        testClsList = []
        haveCls = False
        for name, module in sys.modules.items():
            if name.endswith("Test"):
                haveCls = True
                for clsName, cls in inspect.getmembers(module):
                    if inspect.isclass(cls):
                        if clsName.endswith("Test"):
                            testClsList.append(cls)
        if not haveCls:
            raise SystemError("未收集到任何测试模块")
        if not testClsList:
            raise SystemError("未收集到任何测试类")
        # print(testClsList)
        return testClsList

    # 执行所有测试方法
    def _runAllTestMethod(self):
        while self.allClsList:
            self.lock.acquire()
            cls = self.allClsList.pop(0)
            self.lock.release()
            obj = cls()
            for methodName in obj.methodNameListOrderedByDef:
                method = getattr(obj, methodName)
                # 运行
                obj.reporter.logDrive(method)
            print(obj.reporter.logStack)
            obj.reporter.record(self.logHolePath, obj.reporter.logStack)

    # 多线程执行
    def _threadRunAll(self):
        threads = []
        for i in range(self.threadNum):
            now_thread = threading.Thread(target=self._runAllTestMethod)
            threads.append(now_thread)
        for j in threads:
            j.start()
        for k in threads:
            k.join()


if __name__ == '__main__':
    ex = ExecuteBase()
    # ex.importAllTestCase()
    # ex.collectAllTestCls()
    # ex._runAllTestMethod()
    ex._threadRunAll()
