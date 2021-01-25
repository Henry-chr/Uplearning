# int(): 将数据转换为 int 类型

str1 = "10"
# int() 默认按10进制转换后显示
num1 = int(str1)
print(num1)

# int() 处理浮点数，只留下整数部分，舍弃小数部分（并不是四舍五入操作）
num2 = int(3.74)
print(num2)

"""
num1 = int(str1, 8) # 第二个参数为8，表示按8进制转换后显示，结果为 8
num1 = int(str1, 16) # # 第二个参数为16，表示按16进制转换后显示，结果为 16
#01 02 03 04 05 06 07 10
#01 02 ... 0B 0C 0D 0E 0F 10
print(num1)
"""


# float() 将数据转化为浮点数
str2 = "3.14"
f1 = float(str2)
print(type(f1))

f2 = float(10)
print(f2)

# complex() 创建复数: 第一个参数是复数的实部，第二个参数是复数的虚部
c1 = 10 + 4j
c2 = complex(10, 4)

print(c1)
print(c2) # 等同与c1

# str() : 转换为 字符串类型
num1 = 10
f1 = 3.14

print(type(str(num1)))
print(type(str(f1)))

# repr()： 转换为表达式字符串
num1 = 10
print(type(repr(num1)))
print(repr(num1))


# eval(): 将字符串形式的数据，还原为原本的类型
str1 = "3.14"
print(type(eval(str1)))

str2 = "[10, 20, 30]"
l = eval(str2)
print(type(l))
print(l[0])


# chr: 将一个整数转换为对应的 Unicode 字符
s = chr(1065)
print(s)

# ord ：将一个字符转换为对应的字符编码数字
n = ord("A")
print(n)

# bin: 将一个整数转换为二进制
print(bin(1024)) # 0b 开头表示二进制数

# oct：将一个整数转换为八进制
print(oct(1024)) # 0o 开头表示八进制数

# hex: 将一个整数转换为十六进制
print(hex(1024)) # 0x 开头表示十六进制
