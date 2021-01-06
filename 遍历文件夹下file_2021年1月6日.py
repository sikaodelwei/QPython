#-*-coding:utf8-*-
import os
rootdir = '../Download/WeiXin'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       print(path)
       if os.path.isfile(path):
              print("成功了")
              print(list[i])