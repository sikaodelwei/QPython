#-*-coding:utf8-*-
#       录入书号方法
#1 复制小程序盘点扫码获得书号
#2 粘贴txt桌面快捷方式保存
#3 
f=open('bookNO.txt')
list=[]
text=f.readlines()
for t in text:
  print("输出文本")
  if "9787" in t:
      list.append(t)
      
for l in list:
     print(l)