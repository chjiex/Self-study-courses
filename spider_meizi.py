import requests
import os
import re
from bs4 import BeautifulSoup

# 浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safafi/537.1"}

base_url = "http://www.mzitu.com/all"
# 请求头
r = requests.get(base_url, headers=headers) 
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
	r_second = requests.get(url, headers=headers).text
	# with open(r"C:\Users\cheng\Desktop\img_miezi\%s\%s" %(title, ))
	soup_second = BeautifulSoup(r_second, "lxml")
	page_num = soup_second.find("div", {"class": "pagenavi"}).find_all("span")
	num = page_num[-2].get_text()
	# print(num)
	for times in range(1,int(num)+1):
		page_url = url + "/" + str(times)
		# print(page_url)
		r_third = requests.get(page_url, headers=headers).text
		soup_third = BeautifulSoup(r_third, "lxml")
		img_href = soup_third.find("div", {"class": "main-image"}).find("img")["src"]
		print(img_href)
		img = requests.get(img_href, headers=headers)
		with open(r"C:\Users\cheng\Desktop\img_miezi\%s\%s.jpg" %(title, str(times)), "wb") as f:
			f.write(img.content)
		print("download %s successful!!" % str(times))
