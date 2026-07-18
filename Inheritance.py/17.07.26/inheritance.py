class personal():
    def information(self,name,email,mobile,address):
        print("****** P I******")
        print("Name:",name)
        print("Email:",email)
        print("Mobile:",mobile)
        print("Address:",address)

class educational(personal):
    def educational(self,mark,total,percentage):
        print("\n****** E I******")
        print("Mark:",mark)
        print("Totall:",total)
        print("Percentage:",percentage)
obj=educational()
name=input("Enter the Name:")
email=input("Enter the email:")   
mobile=input("Enter the mobile:")
address=input("Enter the address:")
obj.information(name,email,mobile,address)
marks=[]
n=int(input("Enter the number of subjects:"))
for i in range(n):
    marks.append(int(input("Enter the mark{i+1}:")))
    total=sum(marks)
    percentage=total/n
obj.educational(marks,total,percentage)
       