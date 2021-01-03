#-*-coding:utf8-*-
import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0, 0,label='你看不见我')
workbook.save('unsee1.xls')


# 创建一个工作簿
xl = xlwt.Workbook(encoding='utf-8')
# 创建一个sheet对象,第二个参数是指单元格是否允许重设置，默认为False
sheet = xl.add_sheet('菜鸟的成长历程', cell_overwrite_ok=False)
# 初始化样式
style = xlwt.XFStyle()
# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
# 黑体
font.bold = True
# 下划线
font.underline = False
# 斜体字
font.italic = True
# 设定样式
style.font = font
# 第一个参数代表行，第二个参数是列，第三个参数是内容，第四个参数是格式
sheet.write(0, 0, '不带样式的携入')
sheet.write(1, 0, '带样式的写入', style)

# 保存文件
xl.save('字体.xls')



import xlwt
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('单元格背景色')
# 创建背景模式对像
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 #设置模式颜色 May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 =
# Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
style = xlwt.XFStyle() # 创建样式对象Create the Pattern
style.pattern = pattern # 将模式加入到样式对象Add Pattern to Style
sheet.write(0, 0, '单元格内容', style)#向单元格写入内容时使用样式对象style
xl.save('菜鸟的成长历程.xls')