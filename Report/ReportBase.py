#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 10:49 上午
# @Author  : fanyanpei
# @File    : ReportBase.py

import json
import logging, time, os, sys
import traceback
from abc import abstractmethod
import typing
import copy


T = typing.TypeVar("T")

class Logger(object):

    cur_path = os.path.dirname(os.path.realpath(__file__))
    log_path = os.path.join(cur_path, 'logs')

    # pyfilename是给excel解析器用的
    def __init__(self, pyfilename=""):
        self.sepList = ["*" * 40]
        self.logStack = []
        self.logData = {}

    def getTestMethodName(self, tracebackList:list)->str:
        stackDescList = []
        for i in tracebackList:
            formatText = i.strip()
            desc:str = formatText.split("\n")[0].strip()
            if not desc.startswith("File"):
                continue
            if "Test.py" not in desc:
                continue
            stackDescList.append(desc)
        return stackDescList[-1].split("in ")[-1]

    def logDrive(self, callBack):
        methodName = callBack.__name__
        module = sys.modules[callBack.__self__.__class__.__module__]
        modulePath = getattr(module, "__file__", None)
        testModuleName = os.path.splitext(os.path.basename(modulePath))[0]
        testClsName = callBack.__self__.__class__.__name__
        signature = testModuleName + "." + testClsName
        data = {'signature': signature,
                'method': methodName,
                'start': self.timeFormat(),
                'traceback': []}
        self.logData.update(data)
        callBack.__self__.methodResult = {"traceback": []}
        try:
            callBack()
        except Exception:
            tracebackList:list = self.logData.get("traceback")
            tracebackContent = traceback.format_exc().split("\n")
            tracebackList.extend(tracebackContent)
            tracebackList.extend(self.sepList)
            updateData = {'status': "fail",
                          'traceback': tracebackList,
                          'end': self.timeFormat()}
            self.logData.update(updateData)
        else:
            self.logData.update({'status': "pass",
                                 'end': self.timeFormat()})
        finally:
            methodNote = "无"
            if hasattr(callBack, "note"):
                methodNote = callBack.__func__.note
            updateData = {'methodNote': methodNote}
            self.logData.update(updateData)
            warningStack = callBack.__self__.methodResult["traceback"]
            if warningStack != []:
                tracebackList: list = self.logData.get("traceback")
                tracebackList.extend(warningStack)
                # tracebackList.extend(self.sepList)
                self.logData.update({'status': "fail",
                                     'traceback': tracebackList,
                                     'end': self.timeFormat()})
            self.__stackInLogStack()

    def timeFormat(self, unixTimeStamp:int= -1)->str:
        if unixTimeStamp == -1:
            timeLocal = time.localtime(int(time.time()))
        else:
            timeLocal = time.localtime(unixTimeStamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeLocal)

    def __stackInLogStack(self):
        data = copy.deepcopy(self.logData)
        self.logStack.append(data)
        # if key in self.logStack.keys():
        #     self.logStack[key].append(data)
        # else:
        #     self.logStack[key] = [data]
        self.logData.clear()

    @abstractmethod
    def genLogFileName(self)->str:
        ...

    def record(self, logPath:str, externalLogStack:list):
        with open(logPath, "a+", encoding="utf-8") as logFile:
            logDataList = [json.dumps(log) + "\n" for log in externalLogStack]
            logStr = "".join(logDataList)
            logFile.write(logStr)

# --------------------------------------------------------------------------------------


if __name__ == "__main__":
    a = Logger()


