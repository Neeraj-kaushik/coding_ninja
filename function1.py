def armstrong(n):
    num=0
    while n!=0:
        rem=n%10
        num=rem*rem*rem
        n=n//10
    if n==num:
        armstrong=True
    else:
        armstrong=False
    return armstrong

n= int(input())
if (armstrong(n)):
    print("true")
else:
    print("false") 