# -*- coding: utf-8 -*-
__author__ = 'Br'

# Maybe this script is so ugly, but it does work. XD

# Hint: Before you start it, make sure you have read the **How to use this scrapy.md** in the same dir !!

import os
import pdb

where_is_scrapy = input("where is your scrapy project?\n")
alpha_list = []

for i in range(1, 44):
    alpha_list.append(str(i))

for i in alpha_list:
    # pdb.set_trace()
    os.system("cd " + where_is_scrapy + "&& scrapy crawl_module " + i)


