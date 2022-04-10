#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 14:35
# @Author  : fanyanpei

from abc import ABCMeta, abstractmethod
import os
import subprocess

class ProtocolConvertBase(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def protocol_convert(self):
        pass

    @classmethod
    def pb2py(cls, protocPath: str, pbPath: str, pyPath: str, fileName: str):
        protocPath = cls.replaceSep(protocPath)
        pbPath = cls.replaceSep(pbPath)
        pyPath = cls.replaceSep(pyPath)
        if not pbPath.endswith(os.sep):
            pbPath += os.sep
        if not pyPath.endswith(os.sep):
            pyPath += os.sep
        if not os.path.exists(pyPath):
            os.makedirs(pyPath)
        cmd = f'{protocPath} ' \
              f'-I={pbPath} ' \
              f'--python_out={pyPath} ' \
              f'{pbPath}{fileName}'
        print(cmd)
        subprocess.run(cmd)

    @classmethod
    def replaceSep(cls, path: str) -> str:
        path.replace("\\", os.sep)
        path.replace("/", os.sep)
        return path
