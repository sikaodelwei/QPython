#-*-coding:utf8-*-
from PIL import Image
import os

path="../Download/WeiXin/test/"

def search_im():
    for root,dirs,files in os.walk(path):
        for file in files: 
            cut(file)           
            
def cut(file):
    im = Image.open(path+file)
    print(im.format,im.size,im.mode)
    #这个大小刚好合适
    box = (10,100,171,800)
    region = im.crop(box) 
    region.show()   
    region.save( path+file+".png" ) 
    
search_im()