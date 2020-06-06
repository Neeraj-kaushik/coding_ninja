n= int(input())
n1=(n+1)/2
n2=n/2
i=1
while i<=n1:
    space=1
    while space<=i-1:
        print(' ',end="")
        space+=1
    j=1
    while j<=i:
        print("*",' ',end="")
        j=j+1
    print()
    i=i+1
i=1
while i<=n2:
    space=1
    while space<=n2-i:
        print(' ',end="")
        space+=1
    j=1
    while j<=n2-i+1:
        print("*",' ',end="")
        j=j+1
    print()
    i=i+1
