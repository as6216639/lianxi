'''oldname=input("请出入要拷贝的文件夹：")
oldfile=open(oldname,"rb")
if oldfile:
    len=oldname.rfind(".")
    h=oldname[len:]

    newname=oldname[:len]+"附件"+h
    newfile=open(newname,"wb")
    for i in oldfile.readlines():
         newfile.write(i)
newfile.close()
oldfile.close()'''



