# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MyspiderPipeline(object):

    def __init__(self):
        # self.filename = open(r'top250.txt','a+',encoding='utf-8')
        self.filename = open(r'sun.txt', 'a+', encoding='utf-8')
        
    def process_item(self, item, spider):
        content = str(item['link']) + "\n"
        self.filename.write(content)
        # txt2 = self.filename.readlines()
        # txtset=set(txt2)
        # lenth1=(txtset)


        # content = str(item['link'])+ "\n"
        # txtset.add(str(item['link']))
        # lenth2=(txtset)
        #
        # if lenth2!=lenth1:  # 如果从源文档中读取的内容不在目标文档中则写入，否则跳过，实现去除重复功能！
        #     self.filename.write(content)
        #
        # else:
        #     print("已去除重复-->" + content)


        return item

    def spider_closed(self, spider):
        self.filename.close()