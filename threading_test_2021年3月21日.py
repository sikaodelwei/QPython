#-*-coding:utf8-*-
import threading 
import androidhelper 
droid = androidhelper.Android() 

droid.vibrate(5000)
droid.makeToast("hhjjj")
r=droid.dialogGetInput("title","message")

respond = droid.GetInput("Hello", "What is your name?")
print respond
time_i = 0 
time_end_i = 60 
def fun_timer(): 
    print('hello timer') 
    global timer 
    global time_i 
    time_i = time_i + 1 
    if time_i <= time_end_i: 
       #droid.cameraCapturePicture('../Download/WeiXin/'+str(time_i)+'.jpg') 
       print("金兰姐妹")
       timer = threading.Timer(60.0,fun_timer) 
       timer.start() 
timer = threading.Timer(1,fun_timer) 
timer.start()

       
