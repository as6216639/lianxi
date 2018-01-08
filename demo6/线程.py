import _thread
def xc():
    for i in range(100,0,-1):
        print("子线程",i)


if __name__=="__main__":
    _thread.start_new_thread(xc,())
    for j in range(1,101,1):
        print("主线程",j)
