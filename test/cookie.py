# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "list_mode=h; theme=auto; locale=zh; cf_clearance=6IJnhb.O.QmunZl4LQ93MVnjMmS9HyhpwwD0Cjs12JM-1699975922-0-1-95bfe989.8fff4b66.6c530746-0.2.1699975922; _rucaptcha_session_id=f9f730c6f4e89189a0846f6a0a7fe8d0; over18=1; _ym_uid=169997592689178066; _ym_d=1699975926; _ym_isad=1; remember_me_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltVjRXVXBvV2pGNGFrdDJaMjVCWTJreFVrTkxJZz09IiwiZXhwIjoiMjAyMy0xMS0yMVQxNTozMjo0OS4wMDBaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX21lX3Rva2VuIn19--f1a1db3cef4edefbc84f9d7d07682e3c14d01773; _jdb_session=ng5XKsfcjksgqZ6GmcXhhWwwuSV3j1V6VI1NY8IwPIvNxBkwJ+vGQr6EQKVmZ1xTZNHxyHaL5zUx8d0Bc3Irb9nVTWLRkCG8n7prpnDdNWktTNp4tn4OTVjgLY4nF5/JZDno26yuC8GuVGJ3tJSbr0VnipNO24rRQRaVZmfNkqhGEctvOyNt6alW1dcke14rtjSebuzQBtcUoZWzE5sWrXDp0s/P0U4EnTZz6LVBJEsViHuzUMOJMznJ3QimcDdDzZjCGkgzsho2+Z/dvW2gzZZ2p9Y7AsuvgDq5A+ia7VV+E9oJWewYjDddg/DdRYTVRYKs/2dktNncysMF8SNfp3hEVqwwxSCZQlRj+1YrJ5BVtv+chwn6PWNtxZ6UFA==--OF4B0AbeYrjqSG4w--XPypWk0KHjpusHtGWwZOig=="
    trans = transCookie(cookie)
    print(trans.stringToDict())
