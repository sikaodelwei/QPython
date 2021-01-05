#-*-coding:utf8-*-
import androidhelper 
droid = androidhelper.Android() 
url = "http://www.baidu.com"
droid.startActivity("android.intent.action.VIEW",url)