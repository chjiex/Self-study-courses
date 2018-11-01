'''
在图片上加字体
'''

from PIL import Image, ImageFont, ImageDraw

img = Image.open("./download.jpg", "r")
draw = ImageDraw.Draw(img)
widht, lenght = img.size
# print(widht, lenght)
font_size = widht // 9
ttfont = ImageFont.truetype("arial.ttf", font_size)
# draw = ImageDraw.draw(img, "8", (256, 0 , 0), )
draw.text((widht - font_size, 0), "8", (256, 0 , 0), font=ttfont)
img.save('./new.jpg', 'jpeg')