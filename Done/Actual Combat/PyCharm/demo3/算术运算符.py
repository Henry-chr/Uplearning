## Python 的算数运算符

# + 加号运算符
num1 = 10
num2 = 20
num3 = num1 + num2
print(num3) # 30
f2 = 5.

f1 = 3.14882
print(f1 + f2)

# 整数和浮点数运算，结果一定是浮点数
print(num1 + f1)

# 字符串和字符串相加，相当合并字符串
s1 = "hello"
s2 = "world"
s3 = "!"
print(s1 + " " + s2 + s3)


# - 减号运算符
print(num1 - num2)
print(f1 - f2)
print(s1 + s2)

# * 乘号运算符
print(num1 * num2)
print(f1 * f2)
print(s1)


# / 除号运算符
num1 = 10
num2 = 20
f1 = 2.5
f2 = 5.0
print(num1 / num2)
print(num1 / f1) # 结果为浮点数
print(f2 / f1)


# // 整除运算符 ： 保留商，舍弃余数
print(num2 // 3)

# % 取余运算符： 保留余数，舍弃商
print(num2 % 3)

# ** 指数运算符 :
print(2 ** 10)


# 算数运算符的优先级：** >  * / % // > + -
# 在做混合运算时，如果用到了多种算术运算符，容易造成优先级混淆
# 最好的办法就是 用小括号 () 来控制优先级
print((10 + 3) * (2 ** 3))