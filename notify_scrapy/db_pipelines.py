# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import pdb
from scrapy.exceptions import DropItem

# The code is from Scrapy docs, see https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from notify_scrapy.items import NoticeItem, HTMLContentItem


class BaseMYSQLPipeline(object):
    def __init__(self, mysql_uri, mysql_db, notice_collection, html_content_collection,
                 publishers_collection, publisher_groups_collection):
        self.mysql_uri = mysql_uri
        self.mysql_db = mysql_db
        # self.user = "root"
        # self.user_password = 'Notify'
        # self.cursor = cursor
        self.notice_collection = notice_collection
        self.html_content_collection = html_content_collection
        self.publishers_collection = publishers_collection
        self.publisher_groups_collection = publisher_groups_collection
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_uri=crawler.settings.get('MYSQL_URI'),
            mysql_db=crawler.settings.get('MYSQL_DATABASE', 'notify'),
            # user=crawler.settings.get('MYSQL_USER', 'root'),
            # user_password=crawler.settings.get('MYSQL_USER_PASSWORD', 'Notify'),
            # cursor=None,
            notice_collection=crawler.settings.get('MYSQL_COLLECTION_NAME', 'notices'),
            html_content_collection=crawler.settings.get('MYSQL_HTML_CONTENT_COLLECTION_NAME', 'html_content'),
            publishers_collection=crawler.settings.get('MYSQL_PUBLISHERS_COLLECTION_NAME', 'publishers'),
            publisher_groups_collection=crawler.settings.get('MYSQL_PUBLISHER_GROUPS_COLLECTION_NAME',
                                                             'publisher_groups')
        )

    def open_spider(self, spider):
        # the user is 'root' and the password is 'Notify', change it if necessary
        # self.db = MySQLdb.connect(self.mysql_uri, "notify_2021", "ej5kQRbZBscU9f", self.mysql_db, charset='utf8')
        self.db = MySQLdb.connect(host=self.mysql_uri, user="root", password="123456", database=self.mysql_db, charset='utf8')

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        pass


class NoticeMYSQLPipeline(BaseMYSQLPipeline):
    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item
        # pdb.set_trace()
        print("OUTPUT:  ",item)
        item_dict = dict(item)
        # Check and close spider
        # pdb.set_trace()
        column_content = ""
        tags_content = ""
        table_name= item_dict['source']
        for columns in item_dict['column']:
            column_content = column_content + str(columns) + ';'
        for its_tags in item_dict['tags']:
            tags_content = tags_content + str(its_tags) + ';'

        cmd = "SELECT * FROM notices WHERE notify_title = %s and notify_release_time = %s and " + \
              "notify_url = %s and notify_source = %s and notify_category = %s"
        data = [item_dict['title'], str(item_dict['publish_time']), item_dict['url'],
                item_dict["source"], column_content]
        cursor = self.db.cursor()
        cursor.execute(cmd, data)
        self.db.commit()
        if cursor.fetchall():
            if getattr(spider, 'max_sticky', 0) > 0:
                spider.max_sticky -= 1
                raise DropItem('A possible sticky notice was found (duplicated). '
                               'Allowed sticky notice(s) left: %d.' % spider.max_sticky)
            else:
                spider.stop_signal = True
                raise DropItem('Notice already existed, spider reached the latest.')

        cmd = "insert into notices(notify_title,notify_url,notify_release_time,notify_content,notify_source," \
              "notify_faculty,notify_type,notify_category,notify_tags) " + \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (item_dict['title'], item_dict['url'], str(item_dict['publish_time']), item_dict['content'],
                item_dict['source'], item_dict['publisher'], item_dict['type'], column_content, tags_content)
        cursor.execute(cmd, data)  # insert a data
        self.db.commit()

        if hasattr(spider, 'max_sticky') and spider.max_sticky > 0:
            spider.max_sticky -= 1
        return item


class HTMLContentMYSQLPipeline(BaseMYSQLPipeline):
    def process_item(self, item, spider):
        if not isinstance(item, HTMLContentItem):
            return item
        # pdb.set_trace()
        item_dict = dict(item)
        cmd = "SELECT * FROM html_content WHERE notify_url = %s"
        data = item_dict['url']
        cursor = self.db.cursor()
        cursor.execute(cmd, [data])
        self.db.commit()
        if cursor.fetchall():
            cmd = "UPDATE html_content SET notify_content = %s WHERE notify_url = %s"
            data = (item_dict['content'], item_dict['url'])
            cursor.execute(cmd, data)  # update a data
        else:
            cmd = "insert into html_content(notify_url,notify_content) values (%s,%s)"
            data = (item_dict['url'], item_dict['content'])
            cursor.execute(cmd, data)  # insert a data
        self.db.commit()
        return item


class PublisherAutoRegisterPipeline(BaseMYSQLPipeline):
    def __init__(self, mysql_uri, mysql_db, notice_collection, html_content_collection, publishers_collection,
                 publisher_groups_collection):
        super().__init__(mysql_uri, mysql_db, notice_collection, html_content_collection, publishers_collection,
                         publisher_groups_collection)
        self.registered_groups = {}
        self.registered_publishers = {}

    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item

        if not hasattr(spider, 'publisher_group') or spider.publisher_group == '':
            return item

        cursor = self.db.cursor()

        if len(self.registered_publishers) == 0:
            cmd = "SELECT * FROM publishers"
            cursor.execute(cmd)
            self.db.commit()
            publishers = cursor.fetchall()
            self.registered_publishers = {publisher[1]: True for publisher in publishers}

        if len(self.registered_groups) == 0:
            cmd = "SELECT * FROM publisher_groups"
            cursor.execute(cmd)
            self.db.commit()
            groups = cursor.fetchall()
            self.registered_groups = {group[1]: True for group in groups}

        group = spider.publisher_group
        publisher = item['publisher']

        if not self.registered_publishers.get(publisher, False):
            cmd = "insert into publishers(notify_name,notify_group) values (%s,%s)"
            data = (publisher, group)
            cursor.execute(cmd, data)
            self.db.commit()
            self.registered_publishers[publisher] = True

        if not self.registered_groups.get(group, False):
            cmd = "insert into publisher_groups(notify_name) values (%s)"
            data = [group]
            cursor.execute(cmd, data)
            self.db.commit()
            self.db[self.publisher_groups_collection].insert_one({'name': group})
            self.registered_groups[group] = True

        return item
