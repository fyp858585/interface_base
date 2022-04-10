#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 17:26
# @Author  : fanyanpei

from abc import ABCMeta, abstractmethod

class GmManagerBase(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def _runCommand(self, *args, **kwargs):
        pass

