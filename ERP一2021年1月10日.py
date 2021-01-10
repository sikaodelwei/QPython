#-*-coding:utf8-*-
import xlrd

def lookAto(yjfl):
  listC=[]
  listB=[]
  listA=[]
  listBN=[]
  listAN=[]
  data = xlrd.open_workbook("../Download/WeiXin/erp.xls")
  table = data.sheet_by_name(yjfl.decode('utf-8'))
  print("\n当前所选表Sheetname为:"+yjfl)
  
  
  #第2处修改:要调的展台所在区位 新品? 畅销? A B C
  xcc="C"
  print("当前所处区位:"+xcc+"区\n")
  
  
  rows = table.nrows
  for row in range(1,rows):
    name=table.cell(row,0).value.encode('utf-8')
    isbn=table.cell(row,1).value.encode(' utf-8')
    one_cla=table.cell(row,3).value.encode('utf-8')
    stock=table.cell(row,5).value
      
    old_loc=table.cell(row,6).value.encode('utf-8')
    old_jia=table.cell(row,7).value.encode('utf-8')
          
    new_loc=table.cell(row,8).value.encode('utf-8')
    new_jia=table.cell(row,9).value.encode('utf-8')
    #xcc="B"
    #print("当前区位"+xcc+"区")
    if xcc in old_loc:
       if new_jia[0:1]=="C":
          listC.append(new_jia+" "+name+"\n                  on"+old_jia)     
          listC.sort()
       if new_jia[0:1]=="B":
          listB.append(new_jia+" "+name)      
          listB.sort() 
          listBN.append(new_loc+" "+name+"\n                  on"+old_jia)
          listBN.sort()
       if new_jia[0:1]=="A":
          listA.append(new_jia+" "+name)      
          listA.sort()    
          listAN.append(new_loc+" "+name+"\n                  on"+old_jia)      
          listAN.sort() 
         
    
  print("──────────── to n ────────────") 
  for l in listBN:     
    print(l)   
    
  print("──────────── to n ────────────") 
  for l in listAN:     
    print(l)   
    
  print("──────────── to C ────────────")      
  for l in listC:
    print(l)   
    
    
#第1修改处:  选择表sheetname

#yjfl="经济管理"
#yjfl="科技"
#yjfl="社科"

yjfl="文学"

#yjfl="设计"
#yjfl="心理心灵"
#yjfl="艺术"
#yjfl="生活"

lookAto(yjfl)
