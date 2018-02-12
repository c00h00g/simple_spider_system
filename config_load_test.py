#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test SpiderConfigure
"""

import unittest

from config_load import SpiderConfigure

class TestSpiderConfigure(unittest.TestCase):
    """test spiderConfigure"""
    def test_init(self):
        """test init"""
        a = SpiderConfigure("./spider.conf")
        self.assertTrue(isinstance(a, SpiderConfigure))

    def test_get_info(self):
        """test get_info"""
        a = SpiderConfigure("./spider.conf")
        section = "spider"
        option = "max_depth"
        b = a.get_info(section, option)
        self.assertEquals(b, "3")

if __name__ == '__main__':
    unittest.main()
