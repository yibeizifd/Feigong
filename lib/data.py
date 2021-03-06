#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from urllib import quote
from sqlier.advanced_config import AdvanceConfig
from lib.log import logger

__author__ = "LoRexxar"


class DataProcess(AdvanceConfig):
    # 获取返回数据
    def __init__(self):
        AdvanceConfig.__init__(self)

    def GetLen(self, payload):
        data = quote(payload)
        try:
            r = self.s.get(self.url + "?" + data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        lens = len(r.text.encode('utf-8'))
        return lens

    def GetData(self, payload):
        data = payload
        try:
            r = self.s.get(self.url + "?" + data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        return r.text.encode('utf-8')

    def GetBuildData(self, payload, llen):
        data = payload
        try:
            r = self.s.get(self.url + "?" + data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        lens = len(r.text.encode('utf-8'))
        # print r.text.encode('utf-8')
        # print payload
        if lens == llen:
            return True
        else:
            return False

    def GetTimeData(self, payload, dtime):
        data = payload
        ptime = time.time()
        try:
            r = self.s.get(self.url + "?" + data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        rr = r.text.encode('utf-8')
        ntime = time.time()
        if ntime-ptime > dtime:
            return True
        else:
            return False

    def PostLen(self, payload):
        data = payload
        r = self.s.post(self.url, data=data, headers=self.headers)
        return len(r.text.encode('utf-8'))

    def PostData(self, payload):
        data = payload
        try:
            r = self.s.post(self.url, data=data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        return r.text.encode('utf-8')

    def PostBuildData(self, payload, llen):
        data = payload
        try:
            r = self.s.post(self.url, data=data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        lens = len(r.text.encode('utf-8'))
        # print r.text.encode('utf-8')
        if lens == llen:
            return True
        else:
            return False

    def PostTimeData(self, payload, dtime):
        data = payload
        ptime = time.time()
        try:
            r = self.s.post(self.url, data=data, headers=self.headers)
        except:
            logger.error("Time out...")
            exit(0)
        rr = r.text.encode('utf-8')
        ntime = time.time()
        if ntime - ptime > dtime:
            return True
        else:
            return False

