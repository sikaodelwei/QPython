#-*-coding:utf8-*-
import xlrd
import androidhelper 
import time
import os

droid = androidhelper.Android()

list=[]
   
def search_dang(isbn,find,nowloc):
    droid.ttsSpeak("这本书所在架号为"+str(nowloc))
    #r=droid.dialogGetInput("hh" "name")
    url = "http://search.dangdang.com/?key="+isbn+"&act=input"
    droid.startActivity("android.intent.action.VIEW",url) 
    time.sleep(30)
    droid.ttsSpeak("需要找的数量为"+find)
    time.sleep(30)
    
    
def sort_jiahao(RW):
    data = xlrd.open_workbook("../Download/WeiXin/"+RW) 
    table = data.sheet_by_name('sheet1')
    rows = table.nrows
    for i in range(7,rows):
      isbn=table.cell(i,2).value
      nowloc=table.cell(i,7).value
      find=table.cell(i,8).value
      list.append( str(nowloc)+'_'+str(isbn)+'-'+str(int(find)))
    list.sort()
    for l in list:
        nowloc=l.split('_')[0]
        isbn_find=l.split('_')[1]
        isbn=isbn_find.split('-')[0]
        find=isbn_find.split('-')[1]
        print(isbn)
        print(find+"本")
        search_dang(isbn,find,nowloc)
       
def search_RW():
    path="../Download/WeiXin"
    for root,dirs,files in os.walk(path):
        for file in files:
            RW=file 
            droid.ttsSpeak("开始找下一单")
            RW_numb=RW[len(file)-10:len(file)-3]
            droid.ttsSpeak(RW_numb)
            print(RW)          
            time.sleep(5)
            sort_jiahao(RW)
              
search_RW()
droid.ttsSpeak("全部找完啦，你可真厉害！")