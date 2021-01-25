chepiao = 1
daoju = 9 # cm
yeti = 80 # ml

if chepiao:
    print("请旅客朋友进站！")
    if daoju < 10 and yeti < 100:
        print("可以上车...")
    else:
        print("携带违禁物品，不允许上车，呼叫警察叔叔！")
else:
    print("没有车票，不允许上车!")


"""
老婆给当程序员的老公打电话：如果下班回家，就顺路买十个包子，如果看到卖西瓜的，买一个。
当晚老公手捧一个包子进了家门…老婆怒道：你怎么只买一个包子？！
老公甚恐，喃喃道：因为我真看到卖西瓜的了。
"""

xiaban = 1 # 1 表示下班
xigua = 1 # 表示看到卖西瓜的
baozi = 0

if xiaban:
    baozi = 10
    if xigua:
        baozi = 1
else:
    baozi = 0

print("回家带了%d个包子..." % baozi)


