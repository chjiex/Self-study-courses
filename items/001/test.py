'''
将图片转化为字符画
'''
# _*_ coding: utf-8 _*_
from PIL import Image

codelib = '#8XOHLTI)i=+;:,. '

img = Image.open('./download.jpg', 'r')
if img.mode != 'L':   # 判断图像是否为灰度图像，L为灰度模式
	img = img.convert('L')
w = img.size[0]
h = img.size[1]
# print(img.size)
img = img.resize((w, h) # 图像大小可随意设置的
f = open('./img2.txt', 'w+')
for i in range(0,h,2): # 每隔一行取一行像素，是为了保持视觉上的纵横比
	line = " "
	for j in range(w):
		line += codelib[int((float(img.getpixel((j,i)))/ 256) * len(codelib))] # 计算当前像素属于哪个字符
	line += "\n"
# with open('./img2.txt', 'w+') as f:
	f.write(line)
print(img.getpixel((2,3)),len(codelib))
f.close()

	
