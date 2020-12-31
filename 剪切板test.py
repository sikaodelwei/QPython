#-*-coding:utf8-*-
from androidhelper import Android
droid = Android()
droid.setClipboard("978751333286629787513335447197875596295861 ")

clipboard = droid.getClipboard().result
print(clipboard)
