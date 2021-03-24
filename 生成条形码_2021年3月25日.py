#-*-coding:utf8-*-
from barcode.writer import ImageWriter
from barcode.ean import EuropeanArticleNumber13
import barcode
import androidhelper 
import time

droid = androidhelper.Android()
path="../Download/WeiXin/temp/"
ean = EuropeanArticleNumber13("690123456789", writer=ImageWriter())
ean.save(path+"image")


