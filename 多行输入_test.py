#-*-coding:utf8-*-
textList = []
keywords = '11'
print('文字多行输入，输入“{0}”即可停止。\n请在下方输入内容。\n'.format(keywords))

while True:
	text = input()
	
	if text == keywords:
		break
	else: 
		textList.append(text)

for i in textList:
	print(i)
