q=[1,2]
print(sum(q))
def add():
    print(10+12)
add()

def add(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
add(4,1)
add(5,2)

def welcome():
    print("No argument and no retuen type:","Welcome")
welcome()

def wel(name):
    print("With argument and no return type:","Welcome1",name)
wel("Hema")

def ai():
    print("No argument and with  return type:","Your age")
    return 22
a=ai()
print(a)

def b(a):
    return a+1
c=b(a)
print("With argument and with return type:",c)

def d(a,b):
    print(a)
    print(b) 
    return "Success"
e=d(b=10,a=30)
print("Keyword argument:",e)

def d(**a):
    for i,j in a.items():
      print(j)
    return a  
e=d(b=10,a=30,c=56,d=676)
print(" Arbitary Keyword argument:",e)

def s(*a,b=100,c=500):
    sum=0
    for i in a:
        sum+=i
    print(sum*b/c)
    return sum* b/c
b=s(10,20,50,40,70)
print("Default:",b)