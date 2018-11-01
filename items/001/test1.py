from PIL import Image
table = '#8XOHLTI)i=+;:,. '

def deal_picture(path):
	img = Image.open(path, 'r')
	if img.mode != 'L':
		img = img.convert('L')
	# w = img.size[0]
	# h = img.size[1]
	img = img.resize((int(960*0.2), int(1280*0.2)),Image.ANTIALIAS)
	w = img.size[0]
	h = img.size[1]
	f = open("./{}.txt" .format(path.split('.')[0]), "w+")
	for i in range(0,h,2):
		line = ''
		for j in range(w):
			line += table[int((float(img.getpixel((j, i) )/ 256)) * len(table))]
		line += "\n"
		f.write(line)
	f.close()
	
	
if __name__ =="__main__":
	path = input("输入你要转换的图片，包含格式后缀名：")
	deal_picture(path)