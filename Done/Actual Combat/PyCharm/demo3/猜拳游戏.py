#include <stdio.h>

# 导入 random 模块，模块里有很多功能函数可以使用，比如 randint
import random

# command 变量值为 'Y'
command = 'Y'

# while 循环，循环条件是 command == 'Y'
while command == 'Y':
    computer = random.randint(1, 3) # randint() 随机生成一个整数 1 2 3 之间
    # 1 表示 剪刀，2 表示 石头， 3 表示 布

    # 玩家输入数字，如果是4表示退出游戏
    player = int(input("请出招( 1 表示 剪刀，2 表示 石头，3 表示 布, 4 则退出游戏：):"))

    if player >= 1 and player <= 4: # 判断数字范围，超过表示恶意输入
        if player == 4:
            command = 'N'
        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            print("玩家获胜，电脑笨蛋！")
        elif player == computer:
            print("双方平局！")
        else:
            print("电脑获胜！")
    else:
        print("玩家恶意输入，请重新输入！")

print("谢谢使用！")


# isinstance(10, int)