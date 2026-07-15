num=int(input("Enter the number:"))
temp=num
sum=0
n=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp=temp//10
if num==sum:
        print(num,"is an Armstrong number")
else:
        print(num,"is not an Armstrong number")