# -*- coding: utf-8 -*-
__author__ = 'Br'

import pdb
from scrapy.commands import ScrapyCommand
from notify_scrapy.faculty_map import key2value
import sys

# Runs all of the spiders begin with the prefix your typed; usage: scrapy crawl_module <spidername_prefix>
# If you want to run all the spiders, use: scrapy crawl_module all

class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return ''

    def short_desc(self):
        return 'Runs all of the spiders begin with the prefix your typed;\n \
        usage: scrapy crawl_module <spider_name_prefix>'

    def run(self, args, opts):
        begin_with = sys.argv[1]
        spider_list = self.crawler_process.spider_loader.list()
        # pdb.set_trace()
        for name in spider_list:
            faculty = name.split('_')[0]
            if str(key2value(faculty)) == begin_with or begin_with == 'all':
                self.crawler_process.crawl(name, **opts.__dict__)
                'a notice'
        self.crawler_process.start()



