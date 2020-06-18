n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        if i==j:
            print("*",end="")
        else:
            print("0",end="")
        j=j+1
    j=(2*n+1)/2
    while j==(2*n+1)/2:
        print("*",end="")
        j=j+1

    j=1
    while j<=n:
        k=n-i+1
        if j==k :
            print("*",end="")
        else:
            print("0",end="")
        j=j+1
        k=k-1
    print()
    i=i+1