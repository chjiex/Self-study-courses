import requests
from bs4 import BeautifulSoup 
import re
import os

def crawl(url):
	r = requests.get(url)
	return r.content


def parse(html):
	soup = BeautifulSoup(html, features="lxml")
	img_urls = soup.find_all("img",{"src": re.compile(".*?\d\.jpg")})
	url_list = []
	for img in img_urls:
		url_list.append(img["src"])
	return url_list

	
def download(url_lists):
	os.makedirs(r"C:\Users\cheng\Desktop\img", exist_ok=True)
	for url in url_lists:
		img_name = url.split("/")[-1]
		page_img = crawl(url)
		with open(r"C:\Users\cheng\Desktop\img\%s" % img_name, "wb") as f:
			f.write(page_img)
		print("download %s is successful!" % img_name)
crawl_url = crawl("http://www.ngchina.com.cn/animals")
url_lists = parse(crawl_url)
download(url_lists)

