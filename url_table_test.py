#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test url_table
"""

import unittest

from url_table import UrlItem
from url_table import UrlTable

class TestUrlItemTable(unittest.TestCase):
    """test UrlItem and UrlTable"""
    def test_item_init(self):
        """test item init"""
        url_item = UrlItem("http://c00h00g.github.io", 3)
        self.assertTrue(isinstance(url_item, UrlItem))

    def test_get_url(self):
        """test get_url"""
        url_item = UrlItem("http://c00h00g.github.io", 3)
        url = url_item.get_url()
        level = url_item.get_level()
        self.assertEquals(url, "http://c00h00g.github.io")
        self.assertEquals(level, 3)

    def test_table_init(self):
        """test table init"""
        url_list = ['http://www.baidu.com/', 'http://www.sina.com/']
        url_table = UrlTable(url_list, 3)
        self.assertTrue(isinstance(url_table, UrlTable))
        url_one = url_table.spider_queue.get().get_url()
        url_two = url_table.spider_queue.get().get_url()
        self.assertEquals("http://www.baidu.com/", url_one)
        self.assertEquals("http://www.sina.com/", url_two)

    def test_insert_into_dict(self):
        """test insert into dict"""
        url_list = ['http://www.baidu.com/', 'http://www.sina.com/']
        url_table = UrlTable(url_list, 3)
        url = "http://www.chg.com/"
        level = 3
        res = url_table.insert_into_dict(url, level)
        self.assertEquals(res, True)
        url_table.spider_queue.get()
        url_table.spider_queue.get()
        insert_url = url_table.spider_queue.get().get_url()
        self.assertEquals("http://www.chg.com/", insert_url)


if __name__ == '__main__':
    unittest.main()
