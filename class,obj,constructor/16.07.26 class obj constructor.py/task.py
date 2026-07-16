class Addstudent():
    #constructor
   def __init__(self):
        self.students={}
#Add students
   def addstudent(self):
    rollnumber=int(input("Enter the Roll Number:"))
    name=input("Enter the Student Name:")
    age=input("Enter the Age:")
    education=input("Enter the Education:")
    percentage=input("Enter the Percentage:")
    self.students[rollnumber]={
        "Name":name,
        "Age":age,
        "Education":education,
        "Percentage":percentage
    }
    print("Student Added Sucessfully")

#Remove Student
   def removestudent(self):
        rollnumber=int(input("Enter the Roll Number to Remove:"))
        if rollnumber in self.students:
          del self.students[rollnumber]
          print("Student Removed Successfully")
        else:
           print("Student Not Found")

#Update Student
   def updatestudent(self):
    rollnumber=int(input("Enter the Roll Number to Update:"))
    if rollnumber in self.students:
        self.students[rollnumber]["Name"]=input("Enter New Name:")
        self.students[rollnumber]["Age"]=input("Enter New Age:")
        self.students[rollnumber]["Education"]=input("Enter New Education:")
        self.students[rollnumber]["Percentage"]=input("Enter New Percentage:")
        print("Student Updated Successfully")
    else:
            print("Student Not Found")
        
#View Student
   def viewstudent(self):
    if len(self.students)==0:
        print("No Student Records")
    else:
        print("\n*************Student Details*************")      
    for rollnumber,details in self.students.items():
        print("Roll Number    :",rollnumber)
        print("Name           :",details["Name"])
        print("Age            :",details["Age"])
        print("Education      :",details["Education"])
        print("Percentage     :",details["Percentage"])
        print("------------------------------------------")

#Object Creation                
obj=Addstudent()
while True:
    print("\n*************S M S*************")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. View Student")
    print("5. Exit")
    choices=(input("Enter Your Choices:"))
    if choices=="1":
        obj.addstudent()
    elif choices =="2":
        obj.removestudent()
    elif choices =="3":
        obj.updatestudent()
    elif choices =="4":
        obj.viewstudent()
    elif choices =="5":
        print("****Thank You****")
        break
    else:
       print("=======Invalid Choices! Please Try Again Correct Choices=======")

