# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DongguanItem
import re


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['javdb.com']
    # 田中宁宁
    # url = 'https://javdb.com/actors/kzx6?t=s,d&sort_type=0&page='
    # 新有菜
    # url = 'https://javdb.com/actors/RJM8?t=s,d&sort_type=0&page='
    # 三上悠亚
    # url = 'https://javdb.com/actors/Av2e?t=s,d&sort_type=0&page='
    # 明日花
    # url = 'https://javdb.com/actors/wm9B?t=s,d&sort_type=0&page='
    # 凉森
    # url = 'https://javdb.com/actors/KxPb?t=s,d&sort_type=0&page='
    # 安宅拉拉
    # url = 'https://javdb.com/actors/DXE5?t=s,d&sort_type=0&page='
    # 高桥圣子
    # url = 'https://javdb.com/actors/x4MV?t=s,d&sort_type=0&page='
    # 彩美旬果
    # url = 'https://javdb.com/actors/5Dya?t=s,d&sort_type=0&page='
    # 葵つかさ
    # url = 'https://javdb.com/actors/A5yq?t=s,d&sort_type=0&page='
    # Rio
    # url = 'https://javdb.com/actors/33nb?t=s,d&sort_type=0&page='
    # 桃乃木かな
    # url = 'https://javdb.com/actors/0dKX?t=s,d&sort_type=0&page='
    # 天使萌
    # url = 'https://javdb.com/actors/5Oyz?t=s,d&sort_type=0&page='
    # 坂道みる
    # url = 'https://javdb.com/actors/vd5z?t=s,d&sort_type=0&page='
    # 水卜櫻
    # url = 'https://javdb.com/actors/0edE?t=s,d&sort_type=0&page='
    # 希崎潔西卡
    # url = 'https://javdb.com/actors/dxne?t=s,d&sort_type=0&page='
    # 櫻空桃
    # url = 'https://javdb.com/actors/bvWB?t=s,d&sort_type=0&page='
    # 新井爱丽
    # url = 'https://javdb.com/actors/rD3r?t=s,d&sort_type=0&page='

    # 相澤南
    # url = 'https://javdb.com/actors/RAnD?t=s,d&sort_type=0&page='
    # 桃谷繪裏香
    # url = 'https://javdb.com/actors/gwE?t=s,d&sort_type=0&page='
    # 佳苗琉華
    # url = 'https://javdb.com/actors/O1bD?t=s,d&sort_type=0&page='
    # 山岸逢花
    # url = 'https://javdb.com/actors/8BDW?t=s,d&sort_type=0&page='
    # 辻本杏
    # url = 'https://javdb.com/actors/5J58?t=s,d&sort_type=0&page='
    # 河北彩花
    # url = 'https://javdb.com/actors/EvkJ?t=s,d&sort_type=0&page='
    # 冬月枫
    # url = 'https://javdb.com/actors/Arq0?t=s,d&sort_type=0&page='
    # 小泽玛利亚
    # url = 'https://javdb.com/actors/78EM?t=s,d&sort_type=0&page='
    # 上原瑞穂
    # url = 'https://javdb.com/actors/m7Vn?t=s,d&sort_type=0&page='
    # 麻仓优
    # url = 'https://javdb.com/actors/exkz?t=s,d&sort_type=0&page='
    # 櫻由羅
    # url = 'https://javdb.com/actors/YbZ8?t=s,d&sort_type=0&page='
    # 希志爱野
    # url = 'https://javdb.com/actors/bAGB?t=s,d&sort_type=0&page='
    # 古川织衣
    # url = 'https://javdb.com/actors/Y8Mx?t=s,d&sort_type=0&page='
    # 小花暖
    # url = 'https://javdb.com/actors/B8K29?t=s,d&sort_type=0&page='
    # 希美真由
    # url = 'https://javdb.com/actors/P9mN?t=s,d&sort_type=0&page='
    # 横山美雪
    # url = 'https://javdb.com/actors/BAJG?t=s,d&sort_type=0&page='
    # 希岛爱里
    # url = 'https://javdb.com/actors/wK0z?t=s,d&sort_type=0&page='
    # 前田香织
    # url = 'https://javdb.com/actors/mPpy?t=s,d&sort_type=0&page='
    # 友田彩也香
    # url='https://javdb.com/actors/dENv?t=s,d&sort_type=0&page='
    # 鈴村愛裏
    # url = 'https://javdb.com/actors/nRKm?t=s,d&sort_type=0&page='
    # 神咲詩織
    # url = 'https://javdb.com/actors/vynb?t=s,d&sort_type=0&page='
    # 八掛海
    # url = 'https://javdb.com/actors/p33Qb?t=s,d&sort_type=0&page='
    # 鈴原愛蜜莉
    # url = 'https://javdb.com/actors/98Yp?t=s,d&sort_type=0&page='
    #
    # 大橋未久
    # url = 'https://javdb.com/actors/21Jp?t=s,d&sort_type=0&page='
    # url = 'https://javdb.com/actors/0JEb?t=s,d&sort_type=0&page='
    # 麻倉憂(無碼)
    # url = 'https://javdb.com/actors/21Jp?t=s,d&sort_type=0&page='
    # url = 'https://javdb.com/actors/OmM0?t=s,d&sort_type=0&page='
    # 河合明日菜
    # url = 'https://javdb.com/actors/69A0?t=s,d&sort_type=0&page='
    # 美空あやか
    # url = 'https://javdb.com/actors/ap64?t=s,d&sort_type=0&page='
    # url = 'https://javdb.com/actors/OXZO?t=s,d&sort_type=0&page='
    # 佐仓绊
    # url = 'https://javdb.com/actors/ap64?t=s,d&sort_type=0&page='
    url = 'https://javdb.com/actors/pRDB?t=s,d&sort_type=0&page='
    # 本庄鈴♀
    # url = 'https://javdb.com/actors/ap64?t=s,d&sort_type=0&page='
    url = 'https://javdb.com/actors/BzpA?t=s,d&sort_type=0&page='

    # top 250
    # url = 'https://javdb.com/rankings/top?page='
    # top 250 有码
    # url = 'https://javdb.com/rankings/top?t=0&page='

    # https: // javdb.com / rankings / top2
    # cookie={
    #     'cookie':'list_mode=h; theme=auto; locale=zh; _rucaptcha_session_id=81cc41d114f7c80d679d9f74fd5f515c; over18=1; _ym_uid=1699936750334282433; _ym_d=1699936750; _ym_isad=1; cf_clearance=D2.mWdQvXU6966HKBVLqMZaHltN4J1xhx9fRFP_vUlg-1699941639-0-1-d327fe3.22004eb6.c1ac0296-0.2.1699941639; redirect_to=%2Frankings%2Ftop; remember_me_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltaFFWR1kyZVZWNWRtbzRVR1I2WVhwNFVHMTNJZz09IiwiZXhwIjoiMjAyMy0xMS0yMVQwNjowMjozMS4wMDBaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX21lX3Rva2VuIn19--2c490aecd9055696af9271bfd65b6d566ba94c41; _jdb_session=ZOMHIWwY7MdgGeZkN7g1rPMOgqURCukvppggPrpEQFNaKuhLWnmu8vih9O9sxOF3I8C%2BLnxu9Mv6gb%2BP%2BjopOoysgnIRuM4PS7MiGzeX6%2FtGoVHcawWjxviRfk86ndafYuyweDB3TllsBqLN7MXiKw%2BXMLKbQWFR3ntTfbQPkbQAI9Z5HvEUJcbV5yRcKIxCG%2B%2F8ac1Rs%2BqOGRLGvZI0kM4rrONltfC3C4aKPEwUX2tLt1jdf0wmFzRiGOkKg82qKZgHMDW2mjPdEl%2FuXzaShjFNClziyGHS8QOzQGdu9eIadM%2FrHQEiG%2FUFGUQ60hgjeb1sf0eim6OEdoKrNj%2FcOuHM52xgl6EjMJnVLO%2F9gxguJZDP7wiezPFJEFh9xlev33zbfp%2BPgoOr2rJSHIjaoYtRQK7d%2Bl4gCaUWqIog08oxb1QdPI%2BllWW2McaNTqb%2FH31M%2FoDWLpPkokkhZZxaBHvP--FApTCM9eZ8u8fzbO--OOmMIP3UEABqvmJQ4FPaWQ%3D%3D'
    # }

    offset = 1
    start_urls = [url + str(offset)]

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        # 指定cookies

        # cookies = {'list_mode': 'h',
        #            'theme': 'auto',
        #            'locale': 'zh',
        #            '_rucaptcha_session_id': 'f9f730c6f4e89189a0846f6a0a7fe8d0',
        #            'over18': '1',
        #            '_ym_uid': '169997592689178066',
        #            '_ym_d': '1699975926',
        #            '_ym_isad': '1',
        #            'remember_me_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltVjRXVXBvV2pGNGFrdDJaMjVCWTJreFVrTkxJZz09IiwiZXhwIjoiMjAyMy0xMS0yMVQxNTozMjo0OS4wMDBaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX21lX3Rva2VuIn19--f1a1db3cef4edefbc84f9d7d07682e3c14d01773',
        #            'cf_clearance': '7mmQ.tpmFsnusp58smh1cImU8QINjBWUYACyiIu7RQg-1699976950-0-1-4900e024.27442b3a.c4e8671a-0.2.1699976950',
        #            '_jdb_session': 'ynH0dtF0P9NicWghmOei1MxknBBSxM5oq5PHPJQz7zbVCRIjrDNh+xYBYznCtbKELQK31nB1oDjXbDpWINZGAsW9M1ToI/avbvVazZDgA24nCCBMtGQMmed7K+AK1hojKwwDXzAYcmaR6RosuBcATn/8sJIr5WjWYVRb7sTSVZgQApn+W4HqaD2cOlQxTEUJeNaMkgEytiPFOGqUUWmlaem0v8kkrvijuIxTLGfoXG2v750xOcM8yHhemU+Zg/i52bxbTO0zgxZAmixRlHdq+Y0u16vjEnuXjFtugVINlmnuDL1VtIQ0rMp3dhLayOsAEsSW0l0/CqYKJH+qJohrQR3ZJwySny6XnQbOnT6MiMb6qMn/kQFPiSs+GmhDkA==--ZdFEsQh4JU8Ypu+T--9ZPm7LFfRtf+7PbzZJpCCg=='
        #
        #            }

        # 再次请求到详情页，并且声明回调函数callback，dont_filter=True 不进行域名过滤，meta给回调函数传递数据
        # yield scrapy.Request(url=self.url + '1', headers=headers, cookies=cookies, callback=self.parse,
        #                      dont_filter=True)
        yield scrapy.Request(url=self.url + '1', headers=headers, callback=self.parse,
                             dont_filter=True)

    def parse(self, response):
        # 取出每个页面里帖子链接列表
        links = response.xpath("//a[@class='box']/@href").extract()
        # print(links)
        # 迭代发送每个帖子的请求，调用parse_item方法处理
        for link in links:
            # print(link)
            yield scrapy.Request("https://javdb.com" + link, callback=self.parse_item)
        # 设置页码终止条件，并且每次发送新的页面请求调用parse方法处理
        if links:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    # 处理每个帖子里
    def parse_item(self, response):
        item = DongguanItem()
        # 标题
        item['link'] = response.xpath('//div[@class="magnet-name column is-four-fifths"]/a/@href').extract()[0]

        yield item
