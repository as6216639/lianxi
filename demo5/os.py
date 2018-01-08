import os
#os.rename("demo1附件.txt","demo2.txt")
#os.mkdir("haha")
fun=1
funame="./haha/"
dirl=os.listdir(funame)
for i in dirl:
    print(i)
    if fun==1:
        newname="前缀-"+funame
    elif fun==2:
        l=len("前缀-")
        newname=funame[l:]
    os.rename(funame+i,funame+newname)