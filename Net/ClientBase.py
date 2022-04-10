#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 17:30
# @Author  : fanyanpei

import socket
from abc import ABCMeta, abstractmethod

class ClientBase(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def initHeartBeatThread(self):
        pass

    @abstractmethod
    def newClient(self):
        pass

    @abstractmethod
    def genAccount(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    # todo 客户端更多的抽象