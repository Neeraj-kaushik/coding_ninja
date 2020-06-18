n=int(input())
i=1
while i<=n:
    space=1
    while space<=i-1:
        print(' ',end="")
        space=space+1
    j=i
    while j<=n:
        print(j,end="")
        j=j+1
    print()
    i=i+1

i=n-1
while i>=1:
    j=i
    while j<=n:
        print(j,end="")
        j=j+1
    print()
    i=i-1