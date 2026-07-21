#Divide Two Numbers with E H
try:
  num1=float(input("Enter the first number:"))
  num2=float(input("Enter the second number:"))
  result=num1/num2
  print(f"Result:{result}")
except ZeroDivisionError:
  print("Error:Cannot divide by zero")
except ValueError:
  print("Error:Please enter the valid numbers")

#Function to Add Two Numbers with E H
def add_num(a,b):
    try:
         return float (a) + float (b) 
    except ValueError:
        return "Error:please enter the Both inputs are valid numbers "
print(add_num(10,2))
print(add_num("ghi",5))

#Prompt Integer Input & Raise value Error
try:
     user_input=input("Please enter the integer number:")
     if not user_input.lstrip('-').isdigit():
        raise ValueError(f"'{user_input}'is not a valid integer")
     number =int(user_input)
     print(f"Success! Your Interger is:{number}")
except ValueError as ve:
     print(f"EXception Raised:{ve}")

#Prompt for Two Numbers & Raise TypeError
try:
     number1=input("Enter the first number:")
     number2=input("Enter the second number:")
     def is_numeric(value):
         try:
             float(value)
             return  True
         except ValueError:
             return False
     if not (is_numeric(number1)and is_numeric(number2)):
        raise TypeError("Please enter the Both inputs are numerics ")
     print(f"Inputs receivedsucessfully:{number1}and {number2}")
except TypeError as te:
     print(f"Exception Raised:{te}")

#find value in a list or Raise ValuError
def list1(target_list,target_value):
     if target_value not in target_list:
       raise ValueError(f"Exception:'{target_value}' is not present in the list") 
     a=target_list.index(target_value)
     return f"Found'{target_value}' at index{a}"
l=[15,25,35,45]
try:
    result=list1(l,15)
    print(result)    
except ValueError as e:
 print(e)
try:
    result=list1(l,20)
    print(result)    
except ValueError as e:
 print(e)
     
  

        