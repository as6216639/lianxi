import threading
a=500
class add(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        global a
        for i in range(5):
            if a>=100:
                a=a-100
                print(self,"取走了100还剩余%d"%a)



t1=add("张三")
t2=add("李四")
t1.start()
t2.start()
