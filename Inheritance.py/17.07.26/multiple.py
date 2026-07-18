class personal():
    def information(self,name,email,mobile,address):
        print("****** P I******")
        print("Name:",name)
        print("Email:",email)
        print("Mobile:",mobile)
        print("Address:",address)

class educational(personal):
    def educational(self,mark,total,percentage):
        print("\n****** E I ******")
        print("Mark:",mark)
        print("Totall:",total)
        print("Percentage:",percentage)
class bank(educational):
    def bankinformation(self,acc_num,branch_name,ifsc_code,available_balance):
        print("\n****** B I ******")
        print("Acc_num:",acc_num)
        print("Branch_name:",branch_name)
        print("Ifsc_code:",ifsc_code)
        print("Available_balance:",available_balance)
obj=bank()
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
acc_num=input("Enter the Acc_num:")
branch_name=input("Enter the Brach_name:")   
ifsc_code=input("Enter the Ifsc_code:")
available_balance=input("Enter the Available_balance:")
obj.bankinformation(acc_num,branch_name,ifsc_code,available_balance)
       