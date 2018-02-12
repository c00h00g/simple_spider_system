#-*- coding:utf-8 -*-

"""
This class provide the method
1) multi thread crawl urls
2) save url to local
"""

import config_load
import threading
import urllib2
import urllib
import time
import os

import url_table
import webpage_parse
import crawl_log

lock = threading.Lock()

class CrawlThread(threading.Thread):
    """ crawlThread
    """
    def __init__(self, max_level, crawl_interval, web_parser, url_table, thread_name, save_path):
        threading.Thread.__init__(self)
        self.max_level = max_level
        self.crawl_interval = crawl_interval
        self.web_parser = web_parser
        self.url_table = url_table
        self.thread_name = thread_name
        self.save_path = save_path

    def run(self):
        while not self.url_table.spider_queue.empty():
            time.sleep(self.crawl_interval)
            #use with 
            with lock:
                url_item = self.url_table.spider_queue.get()
                print url_item.get_url()
                self.parse_url(url_item)
                self.url_table.spider_queue.task_done()

    def parse_url(self, url_item):
        """ save current url
        and get all hrefs of current url
        """
        url = url_item.get_url()
        level = url_item.get_level()

        #save url
        self.save_url(url)

        all_hrefs = self.web_parser.get_one_url_href(url)
        if not all_hrefs:
            return
        if level <= self.max_level:
            for one_href in all_hrefs:
                self.url_table.insert_into_dict(one_href, level + 1)

    def save_url(self, url):
        """
        all io operation should be under exception
        """
        if not os.path.exists(self.save_path):
            try:
                os.mkdir(self.save_path)
            except os.error as err:
                crawl_log.ERROR_LOG("download to path, mkdir error: %s" % err)
                return False

        try:
            path = os.path.join(self.save_path, \
                    url.replace('/', '_').replace(':', '_').replace('?', '_').replace('\\', '_'))
            urllib.urlretrieve(url, path, None)
            crawl_log.INFO_LOG("thread:[%s], url:[%s] is saved!", self.thread_name, url)
        except Exception as e:
            crawl_log.ERROR_LOG("save page error!")
            return False
        return True
