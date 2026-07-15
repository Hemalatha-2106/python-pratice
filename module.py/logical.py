def prime(n):
   if n<2:
      print(n,"Is not prime")
      return
   for i in range(2,n):
          if n%i==0:
             print(n,"Is not prime")
             return
   print(n,"Is prime")
def perfect(n):
 s=0
 for i in range(1,n):
    if n%i==0:
        s+=i
    if s==n:
      print(n,"Is perfect number")
 else:
    print(n,"Is not perfect number")
def armstrong(n):
    temp=n
    digits=len(str(n))
    s=0
    while temp>0:
     rem=temp%10
     s+=rem**digits
     temp//=10
    if s==n:
     print(n,"IS armstrong number")
    else:
     print(n,"Is not armstrong number")


                        

