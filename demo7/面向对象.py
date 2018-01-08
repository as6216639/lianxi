class student(object):
    name="张三"
    ega=18
    __sex="男"

    #def __init__(self):
       # self.name="李四"
       # self.ega=15
       # self.xixi="shican"

    def run(self):
        print("跑步")
    def eat(self):
        print("吃东西")
    def getname(self):
       return self.__sex
    def setsex(self,sex):
        if sex=="男"or sex=="女":
            self.__sex=sex
            print(sex)

class boss(student):
    name="学生"

    def getboss(self,name):
        self.name=name
        print(name,"在玩",)

    def run(self):
        print("erzi")

def fun(student):
    student.run()

p=boss()
d=student()
#p.name="李四"
#print(p.name)
#print(student.name)
#print(p.getname())
#p.setsex('ren')
#p.ss="haha"
#print(p.name)
#print(student.name)
#print(p.ss)
#print(p.xixi)
#print(p.name)
#p.run()
fun(p)
fun(d)
p.run()
d.run()






