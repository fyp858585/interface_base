#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 6:29 下午
# @Author  : fanyanpei
# @File    : ReplacerBase.py

from abc import abstractmethod, ABCMeta


class ReplacerBase(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def convertCsv(self):
        pass

    @abstractmethod
    def delFile(self):
        pass

    @abstractmethod
    def copyFile(self):
        pass

    @abstractmethod
    def writeInitFile(self):
        pass

    @abstractmethod
    def writeSheetManagerPool(self):
        pass
