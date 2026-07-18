#Polymorphism Operator
class add():
    def operation(self,a,b):
        print("Addition=:",a+b)
class mul():
    def operation(self,a,b):
        print("Multiplication=:",a*b)
obj=add()
obj1=mul()
obj.operation(10,5)
obj1.operation(10,5)

#Function for Polymorphism
print(len("Python"))
print((len([1,2,3,4])))
print(len((10,20)))

#first class
class Bird:
    def __init__(self,name):
        self.name=name
        print("Bird Name:",self.name)
    def make_sound(self):
        print("Birds make different sounds")
class parrot(Bird):
      def __init__(self):
           super().__init__("Parrot")
      def make_sound(self):
           print("Sound:Squawk")
class sparrow(Bird):
    def __init__(self):
           super().__init__("Sparrow")
    def make_sound(self):
           print("Sound:Chirp")
parrot=parrot()
parrot.make_sound()
print()

sparrow=sparrow()
sparrow.make_sound()


class Country:
    def __init__(self,name):
     self.name=name
     print("Country Name:",self.name)
    def capital(self):
        pass
    def language(self):
        pass

class India(Country):
    def __init__(self):
     super().__init__("India")
     
    def capital(self):
        print("Capital: New Delhi")
    def language(self):
        print("Language:Hindi")
class USA(Country):
    def __init__(self):
     super().__init__("USA")
     
    def capital(self):
        print("Capital: Washington,D.c")
    def language(self):
        print("Language:English")

class UK(Country):
    def __init__(self):
     super().__init__("United kingdom")
    def capital(self):
        print("Capital:London")
    def language(self):
        print("Language:English")

india=India()
india.capital()
india.language()
print()

usa=USA()
usa.capital()
usa.language()
print()

uk=UK()
uk.capital()
uk.language()
print()





