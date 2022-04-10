#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 14:35
# @Author  : fanyanpei

from abc import ABCMeta, abstractmethod

class ProtocolConvertBase(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def protocol_convert(self):
        pass

