#-*- coding:utf-8 -*-

"""
get url page from internet
"""

import urllib2
import re
from bs4 import BeautifulSoup

import crawl_log

class WebPageParser(object):
    """
    get all hrefs
    """
    def __init__(self, crawl_timeout):
        """web parser init
        """
        self.crawl_timeout = crawl_timeout

    def get_one_url_href(self, url):
        """
        get url's all hrefs
        """
        try:
            response = urllib2.urlopen(url, timeout = self.crawl_timeout)
        except urllib2.HTTPError as e:
            crawl_log.ERROR_LOG("crawl url:[%s] error!, error code is:[%d]", url, e.code)
            return None
        except urllib2.URLError as e:
            crawl_log.ERROR_LOG("crawl url:[%s] error!, reason is:[%d]", url, e.reason)
            return None

        html_doc = response.read()
        soup = BeautifulSoup(html_doc, "html5lib")
        all_links = soup.find_all("a", href=re.compile(r".*.(htm|html)$"))
        all_urls = []
        for one_link in all_links:
            href_info = one_link.get('href')
            if href_info.startswith('http://') or href_info.startswith('https://'):
                all_urls.append(href_info)
            else:
                merge_url = url + "/" + href_info
                all_urls.append(merge_url)
        return all_urls
