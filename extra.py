n=int(input())
while True:
    if n==1:
        value1=int(input())
        value2=int(input())
        sum=value1+value2
        print(sum)
    elif n==2:
        value1=int(input())
        value2=int(input())
        dif=value1-value2
        print(dif)
    elif n==3:
        value1=int(input())
        value2=int(input())
        product=value1*value2
        print(product)
    elif n==4:
        value1=int(input())
        value2=int(input())
        qut=int(value1/value2)
        print(qut)
    elif n==5:
        value1=int(input())
        value2=int(input())
        rem=value1%value2
        print(rem)
    elif n!=1 or n!=2 or n!=3 or n!=4 or n!=5 or n!=6 :
        print("Invalid Operation")
    else:
        break
    n=int(input())
    