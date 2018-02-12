#-*- coding:utf-8 -*-

"""
url table to deduplicate url and forbid multithread visit
"""

import threading
import Queue

class UrlItem(object):
    """
    url item has attr url and level
    """
    def __init__(self, url, level):
        self.url = url
        self.level = level

    def get_url(self):
        """get url item's url
        """
        return self.url

    def get_level(self):
        """get url item's level
        """
        return self.level


class UrlTable(object):
    """description of urltable 
    """
    def __init__(self, url_list, max_level):
        """url table init dict and queue
        """
        self.spider_queue = Queue.Queue()
        self.url_dict = dict()
        self.max_level = max_level
        for one_url in url_list:
            #delete seed deduplicate
            if one_url in self.url_dict:
                continue
            self.url_dict[one_url] = 0 #seed level is 0
            url_item = UrlItem(one_url, 0)
            self.spider_queue.put(url_item)

    def insert_into_dict(self, url, level):
        """insert url into dict
        """
        if level > self.max_level:
            return False
        if url in self.url_dict:
            old_level = self.url_dict[url]
            #if a lower level is found，updata dict
            if old_level > level:
                self.url_dict[url] = level
                url_item = UrlItem(url, level)
                self.spider_queue.put(url_item)
                return True
            else:
                return False
        else:
            self.url_dict[url] = level
            url_item = UrlItem(url, level)
            self.spider_queue.put(url_item)
            return True
