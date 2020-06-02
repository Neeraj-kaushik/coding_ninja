n=int(input())
i=1
p=n
while i<=n:
    new_char=chr(ord("A")+p-1)
    j=1
    while j<=i:
        print(chr(ord(new_char)+j-1),end="")
        j=j+1
    p=p-1
    print()
    i=i+1
