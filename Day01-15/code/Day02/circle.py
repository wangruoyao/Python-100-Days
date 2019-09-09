"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)



Python 字符串格式化使用 "字符 %格式1 %格式2 字符"%(变量1,变量2)，%格式表示接受变量的类型。简单的使用例子如下：

# 例：字符串格式化
Name = '17jo'		
print 'www.%s.com'%Name		
>> www.17jo.com

Name = '17jo'
Zone = 'com'
print 'www.%s.%s'%(Name,Zone)
>> www.17jo.com
字符串格式化时百分号后面有不同的格式符号，代表要转换的不同类型，具体的表示符号如下面所示。

格式符号		表示类型
%s		字符串
%d/%i		十进制整数
%u		十进制整数
%o		八进制整数
%x/%X   		十六进制整数         
%e/%E		科学计数
%f/%F		浮点数
%%		输出%
格式符号为数字时前面可以加为数和补缺位如：%[0][总位数][.][小数位数]来设定要转换的样式，具体使用方法如下：

# 例：数字格式化
nYear = 2018
nMonth = 8
nDay = 18
# 格式化日期 %02d数字转成两位整型缺位填0	
print  '%04d-%02d-%02d'%(nYear,nMonth,nDay)			
>> 2018-08-18		# 输出结果

fValue = 8.123
print '%06.2f'%fValue	# 保留宽度为6的2位小数浮点型
>> 008.12			# 输出

print '%d'%10		# 输出十进制
>> 10
print '%o'%10		# 输出八进制
>> 12
print '%02x'%10		# 输出两位十六进制，字母小写空缺补零
>> 0a
print '%04X'%10		# 输出四位十六进制，字母大写空缺补零
>> 000A
print '%.2e'%1.2888	# 以科学计数法输出浮点型保留2位小数
>> 1.29e+00
