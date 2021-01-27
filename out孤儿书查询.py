#-*-coding:utf8-*-
import os
import xlrd


def f(path,file_name):     
 data = xlrd.open_workbook(path)
 sheetname=file_name.rstrip('.xls')
 table = data.sheet_by_name(sheetname.decode('utf-8'))
 rows = table.nrows
 #行列默认是从0开始的
 print(" ")
 f=open('BookNO.txt')
 text_ls=f.readlines()
 
 for l in text_ls:
 
  for row in range(rows):
   stock_NO =table.cell(row,12).value.encode('utf-8')
  
   
   if str(l)[0:13] == str(stock_NO):
       
       bookname=table.cell(row,6).value.encode('utf-8')
       bz=table.cell(row,9).value.encode('utf-8')
       bz_start=bz[0:1] 
       lr.append(bz+" "+bookname)
       
     
 
rootdir = '../Download/WeiXin/cflow'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
lr=[]
for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       file_name=list[i]
       
       if os.path.isfile(path):
              print("成功了")
       f(path,file_name)   
          
for l in lr:   
   print(l)