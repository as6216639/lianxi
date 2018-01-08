def jm():
    print("     ======学生管理系统=======")
    print("     ======1查看学生信息======")
    print("     ======2修改学生信息======")
    print("     ======3增加学生信息======")
    print("     ======4删除学生信息======")

names={
    "陈淑宁":{"性别":"女","身高":170},
    "魏东":{"性别":"男","身高":170},
    "贾旭":{"性别":"男","身高":170},
    "三川":{"性别":"男","身高":170},
    "小松":{"性别":"男","身高":170},
     "王琪":{"性别":"男","身高":170},
     "赵本飞":{"性别":"男","身高":170},
}

def pd():
    sf=int(input("是否继续操作，是请按1，退出请按2："))
    if sf==1:
        look()
    elif sf==2:
        print("感谢您的操作")

def xg():
    for i in names.items():
        print(i)
    name=input("请选择您要修改学生的名字：")
    if name in names:
        xx1=input("请选择你要改的选项，身高，性别：")
        if xx1 in names[name]:
            xx2=input("请输入你要修改的内容：")
            names[name][xx1]=xx2
            print("修改成功")
            for i in names.items():
                tuple(i)
                print(i)
            pd()
        else:
            for k,v in names.items():
                print(v)
                print("请重新输入信息选项")
                if xx1 in names[name]:
                    xx2 = input("请输入你要修改的内容：")
                    names[name][xx1] = xx2
                    print("修改成功")
                    for i in names.items():
                        tuple(i)
                        print(i)
                    pd()
    else:
        print("请重新输入正确的修改信息")
        name = input("请选择您要修改学生的名字：")
        if name in names:
            xx1 = input("请选择你要改的选项，身高，性别：")
            if xx1 in names[name]:
                xx2 = input("请输入你要修改的内容：")
                names[name][xx1] = xx2
                print("修改成功")
                for i in names.items():
                    tuple(i)
                    print(i)
                pd()
            else:
                for k, v in names.items():
                    print(v)
                    print("请重新输入信息选项")
                    if xx1 in names[name]:
                        xx2 = input("请输入你要修改的内容：")
                        names[name][xx1] = xx2
                        print("修改成功")
                        for i in names.items():
                            tuple(i)
                            print(i)


def zj():
    name1=input("请输入你要增加的学生姓名：")
    xx3=input("请输入您要增加学生的信息：")
    xx4=input("请输入您要增加学生的信息内容：")
    names[name1]={}
    names[name1][xx3]=xx4
    print("增加成功")
    for i in names.items():
        tuple(i)
        print(i)
    pd()

def sc():
    s=int(input("选择删除学生所有信息的输入1，删除学生信息内容请输入2"))
    if s==1:
        for j in names.items():
            print(j)
        s1=input("请输入要删除学生信息的名字")
        names.pop(s1)
        for i in names.items():
            tuple(i)
            print(i)
        print("删除成功")
        pd()
    elif s==2:
        for j in names.items():
            print(j)
        s2 = input("请输入要删除学生信息的名字")
        s3 = input("请输入要删除学生信息的内容")
        names[s2].pop(s3)
        print("删除成功")
        for j in names.items():
            tuple(j)
            print(j)
        pd()

def look():
    jm()
    num=int(input("请按编号输入您的操作："))
    if num==1:
        for k,v in names.items():
            #print(k)
            print(v)
        pd()
    elif num==2:
        xg()
    elif num==3:
        zj()
    elif num==4:
        sc()
look()