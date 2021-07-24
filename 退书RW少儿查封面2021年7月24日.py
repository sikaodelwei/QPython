#-*-coding:utf-8-*-
import androidhelper 
import time
import pandas as pd
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
droid = androidhelper.Android()

#列命名方便df.sort_values(by="")排序
df = pd.read_excel('../Download/test.xls',names=
[' ','书名','书号',' ',' ',' ',' ','当前道具',' ',' '])


#RW少儿按书名排序后获取书号查当当2021年7月24日
df1=df.sort_values(by="书名")
names=df1.ix[:,1].values
isbns=df1.ix[:,2].values
nowlocs=df1.ix[:,7].values
finds=df1.ix[:,9].values

#冒号就能遍历所有行哈哈哈2021年7月24日
max_row=len(df1.ix[:,1].values)

for i in range(1,max_row):
    print(names[i])
    print(isbns[i])
    print(nowlocs[i])
    print(finds[i])
    droid.dialogGetInput('TTS', '点击OK').result
    url = "http://search.dangdang.com/?key="+isbns[i]+"&act=input"
    droid.startActivity("android.intent.action.VIEW",url) 
    droid.makeToast(names[i])
    time.sleep(10)
    droid.ttsSpeak("需要找的数量为"+str(finds[i]))
    time.sleep(5)