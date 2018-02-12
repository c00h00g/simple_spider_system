#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test crawl_log
"""

import unittest

import crawl_log
import logging

class TestCrawlLog(unittest.TestCase):
    """test crawllog"""
    def test_init(self):
        """test init"""
        a = crawl_log.logger
        print a
        self.assertTrue(isinstance(a, logging.Logger))

if __name__ == "__main__":
    unittest.main()
