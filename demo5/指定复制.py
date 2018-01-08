import os
oldname=input("请输入拷贝的文件名")
oldfile=open(oldname,"rb")
if oldfile:
    len=oldname.rfind(".")
    h=oldname[len:]
