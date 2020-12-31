#-*-coding:utf8-*-
import xlrd
data = xlrd.open_workbook("4.xls")
table = data.sheet_by_name('4')
rows = table.nrows
list=[]
listv=[]
for row in range(0,rows):
      cla=table.cell(row,4).value.encode('utf-8')

      bookname=table.cell(row,2).value.encode('utf-8')
      bz=table.cell(row,11).value.encode('utf-8')  
      bz_start=bz[0:1] 
  
      if bz_start=="C":
         list.append(bz[0:6]+bookname)
         

for cb in list:
    for j in range(0,len(list)):
     if cb[0:1]=="C":
         listv.append(cb)
             
    
for cb in list:
    print(cb)
   