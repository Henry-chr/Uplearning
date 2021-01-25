import re
str = '75.6万'
str1 = float(re.findall('\d+\.\d+?',str)[0])
str2 = re.findall('\d+\.\d+?([万千]{1})',str)[0]
str3 = re.findall('\d*',str)
a = 1