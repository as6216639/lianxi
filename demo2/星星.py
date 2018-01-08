
n=int(input("请输入行数"))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()