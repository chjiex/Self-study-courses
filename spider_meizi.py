import requests
import os
import re
from bs4 import BeautifulSoup

# 浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦） 注意---防盗链
def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers
base_url = "http://www.mzitu.com/all"
# 请求头
r = requests.get(base_url) 
# print(r.text)

soup = BeautifulSoup(r.text, "lxml")
img_urls = soup.find("div", {"class": "all"}).find_all("a")
img_urls.pop(0)
# print(img_urls[0])
for i in img_urls:
	title = i.get_text()
	url = i["href"]
	# print(url, title)
	os.makedirs(r"C:\Users\cheng\Desktop\img_miezi\%s" %title, exist_ok=True)
	r_second = requests.get(url).text
	# with open(r"C:\Users\cheng\Desktop\img_miezi\%s\%s" %(title, ))
	soup_second = BeautifulSoup(r_second, "lxml")
	page_num = soup_second.find("div", {"class": "pagenavi"}).find_all("span")
	num = page_num[-2].get_text()
	# print(num)
	for times in range(1,int(num)+1):
		page_url = url + "/" + str(times)
		# print(page_url)
		r_third = requests.get(page_url).text
		soup_third = BeautifulSoup(r_third, "lxml")
		img_href = soup_third.find("div", {"class": "main-image"}).find("img")["src"]
		print(img_href)
		img = requests.get(img_href, headers=header（img_href))
		with open(r"C:\Users\cheng\Desktop\img_miezi\%s\%s.jpg" % (title, str(times)), "wb+") as f:
			f.write(img.content)
		print("download %s successful!!" % str(times))
