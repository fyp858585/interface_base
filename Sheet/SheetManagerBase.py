#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 6:17 下午
# @Author  : fanyanpei
# @File    : SheetManagerBase.py

from abc import abstractmethod, ABCMeta
import csv

class SheetManagerBase(metaclass=ABCMeta):

    key_row = 2
    cs_row = 0
    start_row = 6

    # @classmethod
    # def Csv2Dcit(cls, filename):
    #     with open(filename, "r", encoding="utf-8 sig")as read_obj:
    #         content = csv.reader(read_obj)
    #         result_dict = {}
    #         for index, row in enumerate(content):
    #             need_dict = {}
    #             if index == cls.cs_row:
    #                 cs_info = row
    #             elif index == cls.key_row:
    #                 key_word = row
    #             if index >= cls.start_row:
    #                 for i in range(len(cs_info)):
    #                     if cs_info[i] in ["cs", "c", "s"]:
    #                         need_dict[key_word[i]] = row[i]
    #                 result_dict[row[0]] = need_dict
    #     return result_dict

    @abstractmethod
    def Csv2Dict(self):
        pass