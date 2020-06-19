n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print(' ',end="")
    for j in range(i,n):
        print(j+1,end="")
    print()
for i in range(2,n+1):
    for j in range(0,n-i):
        print(' ',end="")
    for j in range (n-i,n):
        print(j+1,end="")
    print()