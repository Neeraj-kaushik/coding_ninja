n=int(input())
i=1
while i<=n:
    p=n-i+1
    j=1
    while j<=p:
        if i%2!=0:
            print("1",end="")
        else:
            print("0",end="")
j=j+1
    print()
    i=i+1