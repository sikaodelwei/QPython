#-*-coding:utf8-*-
import xlrd
import os
import time
import androidhelper 
droid = androidhelper.Android()

while(True):
  x=droid.recognizeSpeech("TTS", "en", " ").result.encode("utf-8")
 
  print(x)
  if x in "123456我们。一起吃饭吧":
      print("是一个子集")
  time.sleep(8)