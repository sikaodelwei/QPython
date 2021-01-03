#-*-coding:utf8-*-
import xlrd

data_xj = xlrd.open_workbook("xiajia.xls")
table_xj = data_xj.sheet_by_name('xiajia')
rows_xjia = table_xj.nrows

data = xlrd.open_workbook("4.xls")
table = data.sheet_by_name('4')
rows = table.nrows
list=[]
list_xjia=[]

for row in range(0,rows):
      flei=table.cell(row,5).value.encode('utf-8')  
      bz=table.cell(row,11).value.encode('utf-8')  
      bz_start=bz[0:1]   
      if bz_start=="C":
         list.append(bz[0:6]+flei)
         
    
for k in list:
  for row in range(0,rows_xjia):
    xj_flei=table_xj.cell(row,7).value.encode('utf-8')  
    a=k.replace(k[0:6],"")
   
    if a==xj_flei:
       xj_bookname=table_xj.cell(row,6).value.encode('utf-8')            
       list_xjia.append(k[0:6]+xj_bookname)

for k in list_xjia:
    print(k)