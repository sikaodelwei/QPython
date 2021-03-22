#-*-coding:UTF-8-*-
import xlrd
import os
import re
import urllib
from bs4 import BeautifulSoup
import time
import androidhelper 
droid = androidhelper.Android()

list=[]
f=open('../Download/WeiXin/robot.txt','r')
text=f.readlines()
def url_bs():
     url="http://www.iyuji.cn/iyuji/s/Z3FucTd3NUQ3Sm1xUHE1b0I3cmVNdz09/1616377532124269"
     response=urllib.urlopen(url) 
    
     r=response.read()
     print(r.encode('utf-8'))

     soup = BeautifulSoup(r,'html.parser')
     
     soup_text=soup.find_all('p')
     for s in soup_text:
         list.append(s.decode('utf-8'))
     for l in list:
         print(l)
     time.sleep(30)
     return soup_text

def f():
    #droid.viewHtml('../Download/WeiXin/123.html')
    url="http://www.iyuji.cn/iyuji/s/Z3FucTd3NUQ3Sm1xUHE1b0I3cmVNdz09/1616377532124269"
    droid.webViewShow(url,False)
    time.sleep(60)
    time.sleep(20)


def find_QA(Q_part):
 

    print(Q_part)
    for line in text:
      if Q_part.rstrip('。') in line:
          droid.ttsSpeak("查到了")
          droid.ttsSpeak(line)
          print(line)
  
    time.sleep(20)
       
while(True):
  Q_part=droid.recognizeSpeech("TTS", "en", " ").result.encode("utf-8")
  
 
  find_QA(Q_part)
  time.sleep(5)
  