'''
n=1
while n<=9:
    j = 1
    while j<=n:
        print('%dx%d=%d\t' %(n,j,n*j),end="")
        j+=1
    print()
    n+=1
'''
for i in range(1,10):
    for j in range(1,10):
        print(j,"x",i,"=",j*i,"  ",end="")
        if i==j:
            print()
            break
            #ddddd
            #ssss