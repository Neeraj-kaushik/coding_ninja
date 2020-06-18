
def checkMember(n):
    value1=0
    value2=1
    i=1
    while i<n:
        fabno=value1+value2
        value1=value2
        value2=fabno
        i=i+1
        if n==fabno:
            checkMember=True
        else:
            checkMember=False
        return checkMember


n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")