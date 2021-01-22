#-*-coding:utf8-*-
from PIL import Image
import os
import gzip

#相册找到
im = Image.open("../Pictures/Screenshots/t.png")
print(im.format,im.size,im.mode) 
#截图
box = (10,100,950,950)
region = im.crop(box)

region.show()
for i in range(0,3):
    region.save("ku/"+str(i)+".png")
   
#-*-coding:utf8-*-
import androidhelper
import urllib
droid = androidhelper.Android()
isbn="9787544298995"
url="https://search.dangdang.com/?key="+str(isbn)
print(url)
r=droid.startActivity("android.intent.action.VIEW",url)
box = (10,100,950,950)
region = im.crop(box)

region.show()
for i in range(0,3):
    region.save("ku/"+str(i)+".png")



