# -*- coding:utf-8 -*-
'''
2022年3月7日14:14
①后台网站点击下载RW
②运行该程序
③生的RW.csv在Download/upload appinventor文件夹下 
④微信发送RW.csv和RW.txt到群里 
'''
import pandas as pd
import os
from androidhelper import Android 
import sys
import xlwt
droid = Android() 
reload(sys)
#droid.makeToast("文件名不含“退库任务RW”需转.csv,eg改名 退库任务RW ABC1234")
path="../Download/"
folder="../Download/upload appinventor/"

if not os.path.exists(folder): 
    os.makedirs(folder)

for root,dirs,files in os.walk(path):
    for file in files: 
        if "退库任务RW" in str(file) and "csv" not in str(file):
             excle_name=file 
             with open(folder+"RW.txt", "a") as f:
                  data = f.write(excle_name[12:32]+",") #读取文件                  

for root,dirs,files in os.walk(path):
    for file in files: 
        if "退库任务RW" in str(file) and "csv" not in str(file):
             excle_name=file 
             print(file)      
             df= pd.read_excel('..//Download/'+excle_name,'sheet1',index_col=0)
             row_num = len ( df )
             df.insert(0,'' ,'',allow_duplicates=False) #添加列 2022年3月7日时间
             #print ( "总行数" + str (row_num ))
             #print ( df )
             
             df.drop(df.index[3:5],inplace=True)# pandas删除行 2022年3月5日14:39
             df.to_csv(folder+excle_name[12:32]+'.csv',encoding='utf-8') 
             
print("\n已转为  csv  保存在 /Download/upload appinventor")
print("已生成  RW.txt  待上传 APP inventor")
    

   