class school():
    def information(self,name,email,mobile,address):
        print("****** S I******")
        print("Name:",name)
        print("Email:",email)
        print("Mobile:",mobile)
        print("Address:",address)

class staff(school):
    def staffinformation(self,name,email,mobile,address,dept):
       self.information(name,email,mobile,address)
       print("Department:",dept)

class student(school):
    def studentinformation(self,name,email,mobile,address,dept):
       self.information(name,email,mobile,address,)
       print("Department:",dept)  

choice=input("Enter Student or Staff:")
if choice=="student":
    obj=student()
    name=input("Enter the Name:")
    email=input("Enter the email:")   
    mobile=input("Enter the mobile:")
    address=input("Enter the address:")  
    dept=input("Enter the Department:")  
    obj.studentinformation(name,email,mobile,address,dept)
elif choice=="staff":
    obj=staff()
    name=input("Enter the Name:")
    email=input("Enter the email:")   
    mobile=input("Enter the mobile:")
    address=input("Enter the address:")  
    dept=input("Enter the Department:")  
    obj.staffinformation(name,email,mobile,address,dept)
else:
   print("Invalid Choice")