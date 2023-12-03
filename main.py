from scrapy import cmdline
cmdline.execute('scrapy crawl sun'.split())
# fi = open('sun.txt', 'r') # 打开需要处理的test.txt。
# txt = fi.readlines()
# with open('sun_OK.txt', 'a') as f:#创建处理去重复后的结果保存文档，防止找不到文件出错
#     f.close()
# for w in txt:
#     fi2 = open('sun_OK.txt', 'r')
#     txt2 = fi2.readlines()
#     with open('sun.txt_OK.txt', 'a') as f:  # 打开目标文件开始写入
#         if w not in txt2:	#如果从源文档中读取的内容不在目标文档中则写入，否则跳过，实现去除重复功能！
#             f.write(w)
#         else:
#             print("已去除重复-->"+w)
#         f.close()
# fi.close()
