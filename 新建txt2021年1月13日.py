#-*-coding:utf8-*-
import os
path=('../Download/WeiXin/temp.txt')
f=open(path,'a')
for l in range(88):
    f.write(str(l)+'\n')     
f.close

