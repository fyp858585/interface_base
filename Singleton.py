#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 6:31 下午
# @Author  : fanyanpei
# @File    : Singleton.py

class Singleton(type):
    """
    单例模式
    """
    def __init__(self, *args, **kwargs):
        self.__isinstance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__isinstance is None:
            self.__isinstance = super().__call__(*args, **kwargs)
            return self.__isinstance
        else:
            return self.__isinstance
