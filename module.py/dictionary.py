def getdictionary():
    d={}
    n=int(input("Enter number of items:"))
    for i in range(n):
        key=input("Enter key:")
        value=int(input("Enter value:"))
        d[key]=value
    return d
def printdictionary(d):
        print("Dictionary is")
        print(d)
def sumvalues(d):
    s=0
    for i in d.values():
        s+=i
    print("Sum=",s)
    