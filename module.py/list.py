def getlist():
    l=[]
    n=int(input("Enter list size:"))
    for i in range (n):
        num=int(input("Enter number:"))
        l.append(num)
    return l
def printlist(l):
    print("list=",l)
def evencount(l):
    count=0
    for i in l:
        if i%2==0:
            count+=1
    print("Even numbers=",count)
    
    