# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HackernewsProjectPipeline:
    def process_item(self, item, spider):
        return item
    
import mysql.connector

class MySQLPipeline:

    def open_spider(self, spider):
        # Thiết lập kết nối đến MySQL
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fafa123123haha..',
            database='scrapy_db'
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # Đóng kết nối
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        # Lưu dữ liệu vào bảng
        self.cursor.execute(
            'INSERT INTO comments (user, comment) VALUES (%s, %s)',
            (item.get('user'), item.get('comment'))
        )
        return item

