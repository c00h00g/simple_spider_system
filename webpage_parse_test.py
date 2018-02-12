#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test webpage parser
"""

import unittest

from webpage_parse import WebPageParser

class TestWebPageParser(unittest.TestCase):
    """test class WebPageParser"""
    def test_init(self):
        """test init"""
        a = WebPageParser(5)
        self.assertEquals(a.crawl_timeout, 5)

    def test_get_one_url_href(self):
        """test get_one_url_href"""
        a = WebPageParser(5)
        url = "http://pycm.baidu.com:8081"
        urls = a.get_one_url_href(url)
        first_url = "http://pycm.baidu.com:8081/page1.html"
        self.assertEquals(first_url, urls[0])

if __name__ == '__main__':
    unittest.main()


