from scrapy.loader import ItemLoader

from notify_scrapy.items import HTMLContentItem
from notify_scrapy.parser_selector import page


@page('ygb.zju.edu.cn')  # Postgraduate Work Department
def parse_article(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="article"]/*').extract()))
    yield loader.load_item()


@page('www.ghls.zju.edu.cn', r'\/.+?page\.htm')  # Guanghua Law School
@page('www.ccea.zju.edu.cn', r'\/.+?page\.htm')  # College of Civil Engineering and Architecture
@page('www.psych.zju.edu.cn', r'\/.+?page\.htm')  # Department of Psychology and Behavioral Sciences
@page('office.cas.zju.edu.cn', r'\/.+?page\.htm')  # College of Animal Sciences
@page('www.cab.zju.edu.cn', r'\/.+?page\.htm')  # College of Agriculture and Biotechnology
@page('www.spa.zju.edu.cn', r'\/.+?page\.htm')  # School of Public Affairs
@page('marx.zju.edu.cn', r'\/.+?page\.htm')  # School of Marxism
@page('cspo.zju.edu.cn', r'\/.+?page\.htm')  # CS College
@page('www.isee.zju.edu.cn', r'\/.+?page\.htm')  # ISEE College
@page('lantian.zju.edu.cn')  # Lantian Community
@page('yunfeng.zju.edu.cn', r'\/.+?page\.htm')  # Ziyun&Bifeng Community
@page('mse.zju.edu.cn', r'\/.+?page\.htm')  # School of Materials Science and Engineering
@page('www.cls.zju.edu.cn', r'\/.+?page\.htm')  # College of Life Sciences
@page('ee.office.zju.edu.cn', r'\/.+?\.htm')  # College of Electrical Engineering
@page('doe-oa.zju.edu.cn', r'\/.+?page\.htm')  # College of Energy Engineering
@page('me.zju.edu.cn', r'\/.+?page\.htm')  # Mechanical Engineering School
@page('www.sis.zju.edu.cn', r'\/.+?page\.htm')  # inter_studies_school
@page('webplus.zju.edu.cn', r'\/.+?page\.psp')  # inter_studies_school && College of Environmental and Resource Sciences
@page('office.physics.zju.edu.cn', r'\/.+?page\.htm')  # physics_depart
@page('office.polymer.zju.edu.cn', r'\/.+?page\.htm')  # polymer_depart
@page('www.psych.zju.edu.cn', r'\/.+?page\.htm')  # psychology_depart
@page('qsxy.zju.edu.cn', r'\/.+?page\.htm')  # qiushi_college
@page('www.cst.zju.edu.cn', r'\/.+?page\.htm')  # software_college
@page('www.math.zju.edu.cn', r'\/.+?page\.htm')  # School of Mathematical Sciences
@page('www.cmic.zju.edu.cn', r'\/.+?page\.htm')  # media_college
@page('www.cmm.zju.edu.cn', r'\/.+?page\.htm')  # School of Medicine
@page('office.opt.zju.edu.cn', r'\/.+?page\.htm')  # College of Optical Science and Engineering
@page('office.cps.zju.edu.cn', r'\/.+?page\.htm')  # College of Pharmaceutical Sciences
@page('office.chem.zju.edu.cn', r'\/.+?page\.htm')  # Department of Chemistry
@page('dqxy.zju.edu.cn', r'\/.+?page\.htm')  # Danyang&Qingxi Community
@page('gs.zju.edu.cn', r'\/.+?page\.htm')  # School of Earth Sciences
@page('office.ckc.zju.edu.cn', r'\/.+?page\.htm')  # chu_kochen_honors_college
@page('www.ir.zju.edu.cn', r'\/.+?page\.htm')  # global_engagement
# @page('libweb.zju.edu.cn', r'\/.+?page\.htm')  # Library
def parse_wp_articlecontent(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="wp_articlecontent"]/*').extract()))
    yield loader.load_item()


@page('office.cbeis.zju.edu.cn', r'\/.+?page\.htm')  # BEIS College
def parse_beis_college(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="wp_articlecontent"]/*').extract()))
    yield loader.load_item()


@page('grs.zju.edu.cn')  # Graduate School
@page('saa.zju.edu.cn')  # School of Aeronautics and Astronautics
@page('www.doe.zju.edu.cn')  # College of Energy Engineering
@page('www.caefs.zju.edu.cn')  # College of Biosystems Engineering and Food Science
@page('www.cmic.zju.edu.cn')  # College of Media and International Culture
@page('ckc.zju.edu.cn')  # CKC College
@page('bksy.zju.edu.cn', r'\/dwjlfwpt.+')  # Exchange Service Platform
def parse_art_content(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="art-content article-content"]/*').extract()))
    yield loader.load_item()


@page('libweb.zju.edu.cn', r'\/.+?page\.htm')  # Library
@page('www.news.zju.edu.cn', r'\/.+?page\.htm')  # QuiShi news
@page('bksy.zju.edu.cn', r'\/.+?page\.htm')  # undergraduate_school
def parse_library_college(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    # loader.add_value('content', ''.join(response.xpath('//div[@class="content_aa"]//tr[4]/td/*').extract()))
    loader.add_value('content', ''.join(response.xpath('//div[@class="wp_articlecontent"]/*').extract()))
    yield loader.load_item()


@page('zulg.zju.edu.cn')  # Logistics
def parse_logistics_college(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//span[@id="content"][2]/*').extract()))
    yield loader.load_item()


# @page('ee.zju.edu.cn', r'\/.+?\.html')  # College of Electrical Engineering
# def parse_content_source(response):
#     loader = ItemLoader(item=HTMLContentItem(), response=response)
#     loader.add_value('url', response.meta['origin_url'])
#     loader.add_value('content', ''.join(response.xpath('//div[@class="content_source"]/*').extract()))
#     yield loader.load_item()


@page('www.cst.zju.edu.cn')  # College of Software Technology
def parse_vid_wz(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="vid_wz"]/*').extract()))
    yield loader.load_item()


# @page('www.cers.zju.edu.cn')  # College of Environmental and Resource Sciences
# def parse_cers(response):
#     loader = ItemLoader(item=HTMLContentItem(), response=response)
#     loader.add_value('url', response.meta['origin_url'])
#     loader.add_value('content', ''.join(
#         response.xpath('/html/body/div[2]/table/tr/td/div/table/tr[2]/td/table[1]/tr[3]/*').extract()))
#     yield loader.load_item()


# @page('www.cmm.zju.edu.cn')  # School of Medicine
# def parse_cmm(response):
#     loader = ItemLoader(item=HTMLContentItem(), response=response)
#     loader.add_value('url', response.meta['origin_url'])
#     loader.add_value('content', ''.join(
#         response.xpath('//div[@class="xiangqing-news-box"]/*[position() > 3]').extract()))
#     yield loader.load_item()


# @page('www.cps.zju.edu.cn')  # College of Pharmaceutical Sciences
# def parse_cps(response):
#     loader = ItemLoader(item=HTMLContentItem(), response=response)
#     loader.add_value('url', response.meta['origin_url'])
#     loader.add_value('content', ''.join(response.xpath('//div[@class="bt_p"]/*').extract()))
#     yield loader.load_item()


@page('www.cec.zju.edu.cn')  # School Of Economics
# The word "pagation" is a typo made by Chingo Software
def parse_content_pagation(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="content-pagation"]/*[position() > 2]').extract()))
    yield loader.load_item()


@page('mse.zju.edu.cn', r'\/.+?page\.htm')  # School of Materials Science and Engineering
def parse_mse_school(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('/html/body/div[2]/table/tr/td/table/tr[4]/*').extract()))
    yield loader.load_item()


# @page('www.chem.zju.edu.cn')  # Department of Chemistry
# def parse_cers(response):
#     loader = ItemLoader(item=HTMLContentItem(), response=response)
#     loader.add_value('url', response.meta['origin_url'])
#     loader.add_value('content', ''.join(
#         response.xpath('/html/body/table/tr/td/table[3]/tr/td/table/tr/td/table[2]/tr[3]/*').extract()))
#     yield loader.load_item()


@page('polymer.zju.edu.cn')  # Department of Polymer Science and Engineering
def parse_mse_school(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content',
                     ''.join(response.xpath('/html/body/div[2]/table/tr/td[2]/div[2]/table/tr[3]/td/*').extract()))
    yield loader.load_item()


@page('www.ie.zju.edu.cn')  # Department of Industrial and Systems Engineering
def parse_ie_depart(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="xiangxi"]/*').extract()))
    yield loader.load_item()


@page('qsxy.zju.edu.cn')  # Qiushi College
def parse_qiushi_college(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//*[@id="news_body_4"]/div[2]/*').extract()))
    yield loader.load_item()


@page('www.cse.zju.edu.cn', r'.+?id=.*')  # cse college
def parse_cse_college(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="con2f mg2"]/*').extract()))
    yield loader.load_item()


@page('www.career.zju.edu.cn', r'.+?&lmtype=.')  # career_development_centre
def parse_career_development(response):
    loader = ItemLoader(item=HTMLContentItem(), response=response)
    loader.add_value('url', response.meta['origin_url'])
    loader.add_value('content', ''.join(response.xpath('//div[@class="news-detail-ctn"]/*').extract()))
    yield loader.load_item()
