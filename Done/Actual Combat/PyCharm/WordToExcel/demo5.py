# 这样每次复制会覆盖之前复制的内容，想求问有什么好的解决办法？

import xlrd

import openpyxl

import os

from xlutils.copy import copy

rb = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\wdl\Excel\变更任务01.xls',formatting_info="True")

wb = (rb)

# rb1 = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\wdl\Excel\output.xlsx')

# wb2 = copy(rb1)

wb.save(r'C:\Users\Administrator\Desktop\wdl\Excel\test1.xls')

# wb2.save(r'C:\Users\Administrator\Desktop\wdl\Excel\test1.xlsx')