def add(a):
    sum=0
    for i in a:
        sum+=i
    return sum
def sub(a):
       if not a:
           return 0
       sum=a[0]
       for i in a[1:]:
          sum-=i
       return sum
def mul(a):
    sum=1
    for i in a:
        sum*=i
    return sum
def div(a):
        if not a:
         return 0
        sum=a[0]
        for i in a[1:]:
            if i==0:
                print("Cannot divide by zero")
                continue
            sum/=i
        return sum
s=int(input("Enter your how many number:"))
l=[]
for i in range(s):
  va=int(input("Enter the number:"))
  l.append(va)
if s>10:
      print("addition=",add(l))
elif s>8:
       print("subtraction=",sub(l))
elif s>5:
       print("multiplication=",mul(l))
elif s>2:
       print("division",div(l))
else:
  print("Not value")
  
       