#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 14:46
# @Author  : fanyanpei

import unittest
import pytest

import unittest


class TestSetupTeardown(unittest.TestCase):

    def setUp(self):
        print('连接数据库成功...')

    def tearDown(self):
        print('关闭数据库。')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')


if __name__ == '__main__':
    unittest.main()