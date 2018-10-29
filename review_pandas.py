# 此次是对天猫手机搜索第一页的处理，没有找出每页的规律，就没有对页面进行爬取了 慢慢加油吧！ 
import pandas as pd
import requests
import re


headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}
url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.4f492a68luypyX&q=%CA%D6%BB%FA&sort=s&style=g&from=..pc_1_searchbutton&active=2&type=pc'

r = requests.get(url, headers=headers)
# print(r.text)

reg = '<em title="(.*?)">.*?<a href="(.*?)" target=".*?" title=".*?" data-p=".*?" >(.*?)</a>' \
      '.*?<span>该款月成交 <em>(.*?)</em></span>.*?<span .*? data-item="(.*?)" .*? data-tnick="(.*?)" .*?></span>'
reg = re.compile(reg, re.S)
get_lists = re.findall(reg, r.text)
# print(get_list)
# for i in get_lists:
#     print(i)
# 将列表进行数据框处理
df = pd.DataFrame(get_lists)
# print(df)
df.columns = ['Prince', 'Href', 'ProductModel', 'TredMls', 'Data_item', 'ProductShop_name']

# print(df)
# 将数据进行CSV，Excel文件储存
df.to_csv('phone.csv', encoding='gbk')
df.to_excel("phone.xls", sheet_name='第一页')
