n=int(input())
n1=(n+1)/2
n2=n/2
i=1
while i<=n1:
    space=1
    while space<=n1-i:
        print(' ',end="")
        space+=1
    j=1
    k=(2*i)-1
    while j<=k:
        print("*",end="")
        j=j+1
    print()
    i=i+1
i=1
while i<=n2:
    space=1
    while space<=i:
        print(' ',end="")
        space+=1
    
    j=1
    k=2 * (n2-i)
    while j<=k:
        print("*",end="")
        j=j+1
    print()
    i=i+1
