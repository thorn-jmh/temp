from datetime import datetime

import scrapy

from notify_scrapy.notice_loader import NoticeLoader

JWBINFO_COLLEGE_URL = 'http://jwbinfosys.zju.edu.cn/jwggcx.aspx?type=1'
JWBINFO_FACULTIES_URL = 'http://jwbinfosys.zju.edu.cn/jwggcx.aspx?type=2'


class JwbinfoCollegeSpider(scrapy.Spider):
    name = 'jwbinfo_college'
    source = 21
    publisher = '现代教学管理信息系统'
    auto_tags = ['选课', '考试', '成绩', '教材']
    start_urls = [JWBINFO_COLLEGE_URL]
    publisher_group = '学校部门'

    def __init__(self, name=None, **kwargs):
        super(JwbinfoCollegeSpider, self).__init__(name, **kwargs)
        self.stop_signal = False
        self.page = 0

    def parse(self, response):
        for node in response.xpath('//tr[position()>1 and position()<last()]'):

            loader = NoticeLoader(self, selector=node)
            # load data to Item
            loader.add_value('title', node.xpath('./td/a/text()').extract_first().strip(' '))
            # loader.add_xpath('publisher', './td[2]/text()')
            loader.add_value('publish_time',
                             datetime.strptime(node.xpath('./td[3]/text()').extract_first(), '%Y-%m-%d %H:%M:%S'))
            content = node.xpath('./td/a/@onclick').re(r"window\.open\('(.*?)'")
            if len(content) > 0:
                content = content[0]
                loader.add_value('url', content)
                loader.add_value('type', 'File' if content.startswith('http://jwbinfosys.zju.edu.cn/wbwj/') else 'HTML')
            yield loader.load_item()
            if self.stop_signal:
                return

        # Move to next page
        self.page += 1
        target = 'DataGrid1:_ctl24:_ctl' + str(self.page)
        yield scrapy.http.FormRequest.from_response(
            response,
            formname='Form1',
            formid='Form1',
            callback=self.parse,
            formdata={
                '__EVENTTARGET': target,
                '__EVENTARGUMENT': ''
            })


class JwbinfoFacultiesSpider(JwbinfoCollegeSpider):
    name = 'jwbinfo_faculties'
    start_urls = [JWBINFO_FACULTIES_URL]
