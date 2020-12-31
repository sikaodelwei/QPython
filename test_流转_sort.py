#-*-coding:utf8-*-
import xlrd
data = xlrd.open_workbook("4.xls")
table = data.sheet_by_name('4')
rows = table.nrows
listBC=[]
listAB=[] 
listAC=[]
listAA=[]
listCB=[]
chosecla="文学"
for row in range(0,rows):
      cla=table.cell(row,4).value.encode('utf-8')
      move=table.cell(row,8).value.encode('utf-8')
      to  =table.cell(row,9).value.encode('utf-8')
      bookname=table.cell(row,2).value.encode('utf-8')
      bzhu=table.cell(row,2).value.encode('utf-8')
       
      if (chosecla in cla)and("畅销" in move)and("常销" in to):
         listBC.append(bookname)
      if (chosecla in cla)and("新品" in move)and("畅销" in to):
         listAB.append(bookname)    
      if (chosecla in cla)and(("新品" in move)or("" is move))and("常销" in to):
         listAC.append(bookname)             
      if ( chosecla in cla)and("新品" in to):
         listAA.append(bookname)        
      if (chosecla in cla)and("常销" in move)and("畅销" in to):
         listCB.append(bookname)
      
         
             
print("   B 一> C   ")   
for k in listBC:
    print(k)  
              
print("   A 一> B   ")   
for k in listAB:
    print(k)
             
print("   A 一> C  ")   
for k in listAC:
    print(k)
    
                 
print("   新品   ")   
for k in listAA:
    print(k)
                     
print("   C一>B   ")   
for k in listCB:
    print(k)
