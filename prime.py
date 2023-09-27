n=int(input("enter the min range"))
m=int(input("enter the max range"))
for i in range(n,m+1):
     flag = 1
     j=2
     while (j * j <= i):
        if (i % j == 0):
            flag = 0
            break
        j+=1
       
     if (flag == 1 and i!=1 and i!=0):
        print(i,end=" ")
