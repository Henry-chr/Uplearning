import re
# 数量词
# * 匹配0次或者无限次
# + 匹配1次或者无限次
# ？ 匹配0次或者1次
a = 'pytho0python1pythonn2'

b = re.findall('python*',a)
c = re.findall('python+',a)
d = re.findall('python?',a)
print('a:'+a)
print('*:'+str(b))
print('+:'+str(c))
print('?:'+str(d))

# 边界
# ^ 开头
# $ 结尾


# 组
# () 且
# [] 或

def convert(value):
    print(value)
    matched = value.group()
    return '!!'+matched+'!!'

lanuage = 'PythonC#javaPHPC#'

lanuage1 = re.sub('C#',convert,lanuage)
print(lanuage1)


s = 'A8B3C4D0E8F2G0'

def convert1(value):
    matched = value.group()
    if int(matched) >= 6:
        return '1'
    else:
        return '-1'

s1 = re.sub('\d',convert1,s)
print(s1)


# match和search都只返回第一个匹配上的匹配项
a = '5s4f65ds1f32ds15'
# 首字母不成立则返回空
a1 = re.match('\d',a)
# span()获取匹配项所在位置
print(a1.span())
a2 = re.search('\d',a)
# group获取匹配上的内容
print(a2.group())

