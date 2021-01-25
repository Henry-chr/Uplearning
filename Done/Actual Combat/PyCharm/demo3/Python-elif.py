# elif  相当于 else if

score = int(input("请输入同学成绩:"))

if score >= 90 and score <= 100:
    print("评级为A!")
elif score >= 80 and score < 90:
    print("评级为B")
elif score >= 70 and score < 80:
    print("评级为C")
elif score >= 60 and score < 70:
    print("评级为D")
else:
    print("不及格，需要重修！")

print("流程结束！")