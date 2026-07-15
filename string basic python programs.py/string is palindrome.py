a=input("Enter the string: ")
if a==a[::-1]:
   print(" The string is palindrome")
else:
   print("The string is not palindrome")
   a1=input("Enter the string: ")
   b=len(a1)//2
   if len(a1)%2==0:
      symmetric=a1[:b]==a1[b:]
   else:
      symmetric=a1[:b]==a1[b+1:]
palindrome=a1==a1[::-1]
print("symmetric" if symmetric else "Not Symmetric")
print("palindrome" if palindrome else "Not palindrome")
a3=["1","2","3"]
a3.reverse()
print(a3)