from datetime import date
class a():
    def __init__(self,name,country,year,month,day):
        self.name=name 
        self.country=country
        self.birth=date(year,month,day)
    def age(self):
        today=date.today()
        age=today.year - self.birth.year
        if(today.month, today.day)<(self.birth.month, self.birth.day):
            age-=1
        print("Name:",self.name)
        print("Country:",self.country)
        print("Age:",age)
b=a("Hema","India",2004,6,21)
b.age()

class cal():
   def add(self,a,b):
       print("Addition:",a+b)
   def sub(self,a,b):
       print("Subtraction:",a-b)
   def mul(self,a,b):
       print("Multiplicationon:",a*b)
   def div(self,a,b):
       print("Division:",a/b)
c=cal()
c.add(10,5)
c.sub(10,5)  
c.mul(10,5)
c.div(10,5)

import math
class circle():
    def area(self,r):
        print("Circle Area=",math.pi*r*r)
    def perimeter(self,r):
        print("Circle perimeter=",2*math.pi*r)
class triangle():      
    def area(self,b,h):
        print("Triangle Area=",0.5*b*h)
    def perimeter(self,a,b,c):
        print("Triangle perimeter=",a+b+c)
class square():      
    def area(self,a):
        print("Square Area=",a*a)
    def perimeter(self,a):
        print("Square perimeter=",4*a)
d=circle()
d.area(7)
d.perimeter(7)    
e=triangle()
e.area(10,8)
e.perimeter(3,4,5)
f=square()
f.area(6)
f.perimeter(6)