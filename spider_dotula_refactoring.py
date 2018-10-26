import time
import requests
import random
import os
import re
from threading import Thread


class Crawl:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    @staticmethod
    def header():
        UserAgent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        headers = {
            "authority": "www.doutula.com",
            "method": "GET",
            "path": "/photo/list/?page=1",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            # "cookie": "__cfduid=de11f0a4d8a821a66385acc5251e6618d1540368172; UM_distinctid=166a51904004b8-0f55709d675c16-551f3c12-100200-166a519040246b; CNZZDATA1256911977=311938175-1540366631-https%253A%252F%252Fwww.google.co.jp%252F%7C1540366631; _ga=GA1.2.1813010388.1540368172; _gid=GA1.2.2099887220.1540368172; yjs_id=a93e91125d97672e2a2a986d3da3d855; ctrl_time=1; XSRF-TOKEN=eyJpdiI6ImVkU29RcmVvbmxld2F4MDhUS3pDVkE9PSIsInZhbHVlIjoiVlV0OFwvZzFYZldRKzh1SnNRWG5UNldnTGs1VGhkbmhERis3RTJYWGNrenY2dHZGRUhBZU9zY3pxVEYwYjg1VEthNzJYbEgxYVdNS3ZYc3NOR2J5OUN3PT0iLCJtYWMiOiI1ZjNiMGZhYzExMzNhNmI5NzdhZGMyMDhkNzJlNDk3MTIzYTc2MzM1OTYzYjgzMDNkZDA2ZjA2NjI3YzFkNTIwIn0%3D; doutula_session=eyJpdiI6IlJ1ZVVjRk1rYXJSN1wvS1lwM3VVNUd3PT0iLCJ2YWx1ZSI6ImUxNmh2cW1CalgwTEtTYUN0MGM0SFVaalJpdW9CUkxVR29rbkZxODdaR1wvNUpCWE9hczVYVkh2cEZhMzVWR0dsQ3N5UGJtV2RrVzZoVDNZcHN5TmVIQT09IiwibWFjIjoiOTUxMGRiYWM5ODYxYjE1MDUxMTBhMTUxYTJkYTdiNzE2M2NhZmY1NzllMThhOTUwOTYwZmQ1ZWEwMjI1MWNjZCJ9",
            "upgrade-insecure-requests": "1",
            "user-agent": random.choice(UserAgent_list)
        }
        return headers

    def get_url(self):
        r = requests.get(self.url, headers=self.header())
        return r

    def parse(self):
        reg = 'data-original="(.*?)".*?alt="(.*?)"'
        reg = re.compile(reg, re.S)
        get_lists = re.findall(reg, self.get_url().text)
        return get_lists

    def run(self):
        t_list = self.parse()
        for i in t_list:
            img_urls = i[0]
            img_titles = i[1]
            img_formats = img_urls.split(".")[-1]
            if "!" in img_formats:
                img_formats = img_formats.split("!")[0]
            if "?" in img_titles:
                img_titles = img_titles.replace("?", "？")
            elif "*" in img_titles:
                img_titles = img_titles.replace("*", "？")
                if "/" in img_titles:
                    img_titles = img_titles.replace("/", "？")
            # return img_urls, img_titles, img_formats
            os.makedirs("./{0}/第{1}页" .format(self.name, self.url.split("=")[-1]), exist_ok=True)
            html = requests.get(img_urls, headers=self.header()).content
            if not os.path.exists("./{0}/第{1}页/{2}.{3}".format(self.name, self.url.split("=")[-1], img_titles, img_formats)):
                with open("./{0}/第{1}页/{2}.{3}".format(self.name, self.url.split("=")[-1], img_titles, img_formats), "wb") as f:
                    f.write(html)
                print("下载<{}>成功！".format(img_titles))


if __name__ == "__main__":
    for i in range(1, 1969):
        url = "https://www.doutula.com/photo/list/?page={}" .format(i)
        name = "doutuwang"
        first_spider = Crawl(url, name)
        os.makedirs("./%s" % name, exist_ok=True)
        t = Thread(target=first_spider.run, args=())
        t.start()
        time.sleep(2)



