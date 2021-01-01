#-*-coding:utf8-*-
from PIL import Image
#相对路径牛吧，无法用绝对路径的我悟出来了
im = Image.open("../Pictures/Screenshots/t.png")
print(im.format,im.size,im.mode) 
#截图
box = (50,100,718,924)
region = im.crop(box)



region.show()
for i in range(0,8):
    #保存
    region.save("ku/"+str(i)+".png")
