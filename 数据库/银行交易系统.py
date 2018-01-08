import pymysql
db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='python1',
    charset='utf8'
)
cursor=db.cursor()

def pd1():
    a=int(input("返回继续操作请按1，退出请按2"))
    if a==1:

        dljm1()
        p=int(input("请按序号输入要选择的操作"))
        if p==1:
            add('b')
            pd1()
        elif p==2:
            qukuan('b')
            pd1()
        elif p==3:
            update('b')
            pd1()

        elif p==4:
            gs1()
            pd1()
        elif p==5:
            jg('a')
            pd1()
        elif p==6:
            cx('a')
            pd1()


    elif a==2:
        print("感谢您的操作")

def pd():
    a=int(input("返回继续操作请按1，退出请按2"))
    if a==1:

        dljm1()
        p=int(input("请按序号输入要选择的操作"))
        if p==1:
            add('a')
            pd()
        elif p==2:
            qukuan('a')
            pd()
        elif p==3:
            update('a')
            pd()

        elif p==4:
            gs1()
            pd()
        elif p==5:
            jg('a')
            pd()
        elif p==6:
            cx('a')
            pd()


    elif a==2:
        print("感谢您的操作")

def dljm1():
    print("1=======存款=======")
    print("2=======取款=======")
    print("3=======转账=======")
    print("4=======挂失=======")
    print("5=======解挂=======")
    print("6=====查询余额======")

def dljm():
    print("=============欢迎使用私人银行============")
    a=int(input("请输入银行卡号"))
    b=int(input("请输入密码"))
    a1='select num from name '
    b1='select password from name '
    cursor.execute(a1)
    rut1 = cursor.fetchall()
    cursor.execute(b1)
    rut2=cursor.fetchall()
    if a==rut1[0][0] and b==rut2[0][0]:
        dljm1()
        p=int(input("请按序号输入要选择的操作"))
        if p==1:
            add('a')
            pd()
        elif p==2:
            qukuan('a')
            pd()
        elif p==3:
            update('a')
            pd()

        elif p==4:
            gs1()
            pd()
        elif p==5:
            jg('a')
            pd()
        elif p==6:
            cx('a')
            pd()
    elif a==rut1[1][0] and b==rut2[1][0]:
        dljm1()
        p=int(input("请按序号输入要选择的操作"))
        if p==1:
            add('b')
            pd1()
        elif p==2:
            qukuan('b')
            pd1()
        elif p==3:
            update('b')
            pd1()
        elif p==4:
            gs2()
            pd1()
        elif p==5:
            jg('b')
            pd1()
        elif p==6:
            cx('b')
            pd1()
    else:
        print('登陆失败')
        print("请重新登陆")
        dljm()

def add(sum):
    pd="select exist from %s"%(sum)
    cursor.execute(pd)
    rut3=cursor.fetchall()
    if rut3[0][0]==1:
        ck=int(input("请输入存款金额"))
        try:
            sql="update %s set blance=blance+'%d'"%(sum,ck)
            cursor.execute(sql)
            sq2="insert into c values(null,'%s','+%s') "%(sum,ck)
            cursor.execute(sq2)
            db.commit()
            print("存款成功")
        except:
            db.rollback()
            print("存款失败")
    else:
        print("账户已被注销")

def qukuan(cum):
    pd = "select exist from %s" % (cum)
    cursor.execute(pd)
    rut3 = cursor.fetchall()
    if rut3[0][0] == 1:
        qk=int(input("请输入取款金额"))
        sq1="select blance from %s"%(cum)
        cursor.execute(sq1)
        ru1=cursor.fetchall()
        if qk<=ru1[0][0]:
            try:
                sq2="update %s set blance=blance-'%d'"%(cum,qk)
                cursor.execute(sq2)
                sq3="insert into c values(null,'%s','-%s')"%(cum, qk)
                cursor.execute(sq3)
                db.commit()
                print("取款成功")
            except:
                print("取款失败")
        else:
            print("余额不足")
    else:
        print("账户已注销")


def update(sum):
    a=int(input("请输入转账账户"))
    b=input("请输入账户人姓名")
    a1="select num from name"
    cursor.execute(a1)
    ru1=cursor.fetchall()
    a2="select name from name"
    cursor.execute(a2)
    ru2=cursor.fetchall()
    if ru1[0][0]==a and ru2[0][0]==b:
            c=int(input("请输入转账金额"))
            sqq="select blance from b"
            cursor.execute(sqq)
            ruu=cursor.fetchall()
            if ruu[0][0]>=c:
                try:
                    sq1="update %s set blance=blance+'%d'"%(sum,c)
                    cursor.execute(sq1)
                    sq2 = "update b set blance=blance-'%d'"%(c)
                    cursor.execute(sq2)
                    sq11 = "insert into c values(null,'%s','+%s')"%(sum,c)
                    cursor.execute(sq11)
                    sq12 = "insert into c values(null,'b','-%s')"%(a)
                    cursor.execute(sq12)
                    db.commit()
                    print("转账成功")
                except:
                    print("转账失败")
            else:
                print("账户余额不足")
    elif ru1[1][0]==a and ru2[1][0]==b:
        try:
            s=int(input("请输入转账金额"))
            sqw = "select blance from a"
            cursor.execute(sqw)
            rus= cursor.fetchall()
            if rus[0][0]>=s:
                sq3 = "update %s set blance=blance+'%d'"%(sum,s)
                cursor.execute(sq3)
                sq4= "update a set blance=blance=-'%d'"%(s)
                cursor.execute(sq4)
                sq13 = "insert into c values(null,'%s','+%s')"%(sum,s)
                cursor.execute(sq13)
                sq14= "insert into c values(null,'b','-%s')"%(s)
                cursor.execute(sq14)
                db.commit()
                print("转账成功")
            else:
                print("余额不足")
        except:
                print("转账失败")

    else:
        print("账户名或姓名错误")
        update(sum)

def gs1():
    sq1="""create event gs
    on schedule at now()+interval 10 minute
    do update a set exist=0;
    """
    cursor.execute(sq1)
    db.commit()

def gs2():
    sq1="""create event gs
    on schedule at now()+interval 10 minute
    do update b set exist=0;
    """
    cursor.execute(sq1)
    db.commit()

def jg(sum):
    sq1="update %s set exist=exist+'%d'"%(sum,1)
    cursor.execute(sq1)
    db.commit()
    print("解除挂失成功")


def cx(sum):
    sq1="select blance from %d"%(sum)
    cursor.execute()
    s=cursor.fetchall()
    print(s[0][0])


dljm()



