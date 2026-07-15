#lambda function to multiply two numbers
mul=lambda x,y:x*y
result=mul(5,4)
print("Result:",result)

#Find the string with length 6 in a given list
words=["C", "c++", "Python", "Java", "Javascript", "React"]
result=[word for word in words if len(word) ==6]
print("Strings with length 6:",result)

#Multiply each number in a list with a given number using the math function
import math
num=[1,2,3,4,5]
n=5
result=[math.prod([i,n]) for i in num]
print("Result",result)

#Multiply each number in a list with a given number using the map function
import math
num=[1,2,3,4,5]
n=5
result=list(map(lambda x:x*n,num))
print("Result",result)

#check wheather each string in a list is a palindrome using shorthand if-else   
words=["C", "c++", "Python", "Java", "Javascript", "React"]
for word in words:
    print(word,"Palindrome" if word== word [::-1] else "Not Palindrome")

 #check wheather each string in a list is a palindrome or not (using shorthand if-else)   
words=["C", "c++", "Python", "Java", "Javascript", "React"]
for word in words:
    print(word,"->","Palindrome" if word== word [::-1] else "Not Palindrome")

#find the maximum value from given numbers using a 
num=[1,2,3,4,5,6,7,8,9]
maximum=max(num)
print("Maximum Value is:",maximum)

#find the maximum value from given numbers using a lambda function
num=[1,2,3,4,5,6,7,8,9]
maximum=(lambda x:max(x))(num)
print("Maximum Value is:",maximum)