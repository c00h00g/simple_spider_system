#-*- coding:utf-8 -*-

"""
the main page of use python multithread to spider urls 
"""

import threading
import time
import argparse

import config_load
import webpage_parse
import url_table
import crawl_thread
import crawl_log

def get_url_list(path):
    """
    get all url seeds
    """
    url_list = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            url_list.append(line)
    return url_list


def main():
    """
    func entrance
    """
    #0. 处理命令行参数
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-v", "--version", \
            help="print current version of spider program!", action="store_true")
    arg_parser.add_argument("-c", "--spider_conf", help="add the spider conf!")
    args = arg_parser.parse_args()

    SPIDER_CONF = args.spider_conf

    if args.version:
        print "version is 1.0"
    
    if SPIDER_CONF is None:
        print "please input -h to see help!"
        return

    #1. 读取配置
    conf_parser = config_load.SpiderConfigure(SPIDER_CONF)
    thread_num = int(conf_parser.get_info("spider", "thread_count"))
    max_depth = int(conf_parser.get_info("spider", "max_depth"))
    crawl_interval = int(conf_parser.get_info("spider", "crawl_interval"))
    crawl_timeout = int(conf_parser.get_info("spider", "crawl_timeout"))
    url_seed_path = conf_parser.get_info("spider", "url_list_file")
    seed_list = get_url_list(url_seed_path)

    #2. webPageParser
    web_parser = webpage_parse.WebPageParser(crawl_timeout)
    url_table_ins = url_table.UrlTable(seed_list, max_depth)
    threads = []

    #3 create thread
    save_path = './download_page'
    for i in range(thread_num):
        name = "thread_" + str(i)
        thread = crawl_thread.CrawlThread(max_depth, crawl_interval, \
                web_parser, url_table_ins, name, save_path)
        thread.setDaemon(True) 
        thread.start()
        threads.append(thread)

    url_table_ins.spider_queue.join()

    crawl_log.ERROR_LOG("crawl main thread finished!")

if __name__ == '__main__':
    main()
