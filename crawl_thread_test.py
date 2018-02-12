#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
test crawl_thread
"""

from crawl_thread import CrawlThread

class TestCrawlThread(unittest.TestCase):
    """test crawl thread"""
    def test_init():
        """test crawl thread init"""
        max_level = 2
        a = CrawlThread()
