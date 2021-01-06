#-*-coding:utf8-*-
import urllib

response=urllib.urlopen('https://www.baidu.com')  #请求站点获得一个HTTPResponse对象
print(response.read().decode('utf-8'))   #返回网页内容
#print(response.getheader('server')) #返回响应头中的server值
#print(response.getheaders()) #以列表元祖对的形式返回响应头信息
#print(response.fileno()) #返回文件描述符
#print(response.version)  #返回版本信息
#print(response.status)  #返回状态码200，404代表网页未找到
#print(response.debuglevel) #返回调试等级
#print(response.closed)  #返回对象是否关闭布尔值
#print(response.geturl()) #返回检索的URL
#print(response.info()) #返回网页的头信息
#print(response.getcode()) #返回响应的HTTP状态码
#print(response.msg)  #访问成功则返回ok
print(response) #返回状态信息