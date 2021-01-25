
import pandas

with open(r'C:\Users\Administrator\Desktop\wdl\WordToExcel\变更任务01.html','rb') as f:

    # df = pandas.read_html(f.read().decode("gb2312","in").encode('utf-8'),encoding='utf-8')
    df = pandas.read_html(f.read())

print(df[0])

bb = pandas.ExcelWriter('out.xlsx')

df[0].to_excel(bb)

bb.close()