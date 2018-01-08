import random
import time
b=0
c=0
n=0
while n<5 :
    num = int(input("请输入0剪刀，1石头，2布"))
    cum = random.randint(0, 2)
    if num == 0 or num == 1 or num == 2:
        if num==cum:
            print("平局")
            print("电脑的分数为", c)
            print("玩家的分数为", b)
        elif num==0 and cum==1 or num==1 and cum==2 or num==2 and cum==0:
            c+=1
            print("本局电脑胜利")
            print("电脑的分数为",c)
            print("玩家的分数为",b)
        elif cum==0 and num==1 or cum==1 and num==2 or cum==2 and num==0:
            b+=1
            print("本局玩家胜利")
            print("玩家的分数为",b)
            print("电脑的分数为",c)
        n+=1
    else:
        print("输入错误")
if c>b:
    print("电脑获胜")
else:
    print("玩家获胜")