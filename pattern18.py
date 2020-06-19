n=int(input())
k=1
for i in range(1,n+1):
    for j in range (k,k+n):
        print(j,end=" ")
    print()
    if(i==((n+1)//2)):
        if((n%2!=0)):
            k=n*(n-2)+1
        else:
            k=n*(n-1)+1
    elif((i>(n+1)//2)):
        k=k-2*n
    else:
        k=k+2*n