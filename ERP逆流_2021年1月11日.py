#-*-coding:utf8-*-
import xlrd
import androidhelper 
import time
import re

droid = androidhelper.Android() 

def look_cover(isbn):
  url = "http://search.dangdang.com/?key="+isbn
  droid.startActivity("android.intent.action.VIEW",url)
  time.sleep(20)

def lookAto(yjfl):
  listC=[]
  listB=[]
  listA=[]
  listBN=[]
  listAN=[]
  list_findC=[]
  list_findC1=[]
  list_findA=[]
  list_findA1=[]
  list_findCC0=[]
  list_findCtoC=[]
  
  data = xlrd.open_workbook("../Download/WeiXin/erp.xls")
  table = data.sheet_by_name(yjfl.decode('utf-8'))
  #print("\n当前所选表Sheetname为:"+yjfl)
  
  print(" ")
  #第2处修改:要调的展台所在区位 新品? 畅销? A B C
  xcc="C"
  print("当前所找书来自区位:"+xcc+"区\n")
  
  
  rows = table.nrows
  for row in range(1,rows):
    name=table.cell(row,0).value.encode('utf-8')
    isbn=table.cell(row,1).value.encode(' utf-8')
    price=table.cell(row,2).value
    one_cla=table.cell(row,3).value.encode('utf-8')
    stock=table.cell(row,5).value
      
    old_loc=table.cell(row,6).value.encode('utf-8')
    old_jia=table.cell(row,7).value.encode('utf-8')
          
    new_loc=table.cell(row,8).value.encode('utf-8')
    new_jia=table.cell(row,9).value.encode('utf-8')
    
    if xcc in old_loc:     
       if (new_jia[0:1]=="B")and(old_jia[0:1]=="C"):
         
         list_findC.append(old_jia+" "+"书号"+isbn+" "+name+" 价格 "+str(price)+" to "+new_loc) 
         list_findC.sort()
         
         
         list_findC1.append(new_loc+" "+name+isbn+" "+str(stock).rstrip(".0")+" 本") 
         list_findC1.sort()
         
       if (new_jia[0:1]=="A")and(old_jia[0:1]=="C"):
         
         list_findA.append(old_jia+" "+"书号"+isbn+" "+name+" 价格 "+str(price)+" to "+new_loc)     
         list_findA.sort()
         
         list_findA1.append(new_loc+" "+name+" "+str(stock).rstrip(".0")+" 本") 
         list_findA1.sort()
         
       if (new_jia[0:1]=="C")and(old_jia[0:1]=="C"):
         list_findCC0.append(old_jia+" "+"书号"+isbn+" "+name+" 价格 "+str(price)+" to "+new_jia+new_loc)     
         list_findCC0.sort()
         
         list_findCtoC.append(new_jia+" "+new_loc+" "+name+" "+str(stock).rstrip(".0")+" 本") 
         list_findCtoC.sort()
  print("──────────── C 逆流B  ────────────")      
  for l in list_findC:
    
    star=l.find("978")
    isbn= l[star:star+13]
    
    look_cover(str(isbn))  
    
    print(l)    
    
    
  print("──────────── C 逆流 A  ────────────")      
  for l in list_findA:
      
     
    star=l.find("978")
    isbn= l[star:star+13]
    #look_cover(str(isbn))
    #print(l)    
     #h=2
    
  print("───────────C 逆流B n 排序：方便找书  ────────────")      
  for l in list_findC1:
      import os
      path=('../Download/WeiXin/temp.txt')
      f=open(path,'a')
      f.write(str(l)+'\n')     
      print(l)    
     
  f.close
  print("───────────C 逆流A n 排序：方便找书  ────────────")      
  for l in list_findA1:
    print(l)  
     #op=6
    
   
  print("───────────C 逆流 C 排序：方便找书  ────────────")      
  for l in list_findCtoC:
     print(l)  
     #op=6
     
  print("───────────C 逆流 C   ────────────")      
  for l in list_findCC0:
      
     print(l)       
     
  print(len(list_findC1))
  print(len(list_findA1))
  print(len(list_findCtoC))
    
  
  print(len(list_findC1)+len(list_findA1)+len(list_findCtoC))
    
#第1修改处:  选择表sheetname

yjfl1="经济管理"
yjfl2="科技"
yjfl3="社科"

yjfl11="文学"

yjfl21="设计"
yjfl55="心理心灵"
yjfl22="艺术"
yjfl23="生活"

lookAto(yjfl55)
#lookAto(yjfl2)
#lookAto(yjfl3)
