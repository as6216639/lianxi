i=open("demo1.txt","rb")
f=i.read(3)
print("读取的数据",f)
d=i.tell()
print("当前的位置",d)

i.seek(5,1)
f=i.read(3)
print("读取的数据",f)
d=i.tell()
print("当前的位置",d)

i.close()

