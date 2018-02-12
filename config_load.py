#-*- coding:utf-8 -*-

"""
This class provide the methods how to get a config
"""

from ConfigParser import ConfigParser

class SpiderConfigure(object):
    """packing configure in spider
    """
    def __init__(self, conf):
        """init of config
        """
        self.config_parser = ConfigParser()
        self.config_parser.read(conf)

    def get_info(self, section, option):
        """get config info
        """
        return self.config_parser.get(section, option)
