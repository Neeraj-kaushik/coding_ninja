n=int(input())
i=1
while i<=n:
    p=1
    j=n
    while j>=i:
        print(p,end="")
        j=j-1
        p=p+1
    print()
    i=i+1