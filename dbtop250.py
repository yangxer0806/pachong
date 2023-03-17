# 拿到页面源代码
# 提取信息
# 写入csv
import requests
import re
import csv

# 1.拿到页面内容
url = "https://movie.douban.com/top250"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=header)
page_comtent = resp.text

# 2.解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)人评价</span>', re.S)  # re.S表示.号匹配换行符

# 开始匹配
result = obj.finditer(page_comtent)
# for i in result:
#     print(i.group('name'))
#     print(i.group('year').strip())  # strip去掉前面的空格
#     print(i.group('score'))
#     print(i.group('num'))

# 数据写入csv
f = open('data.csv', mode='w')
csvwriter = csv.writer(f)
for i in result:
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
resp.close()
print('ok')
