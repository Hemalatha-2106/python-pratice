a={12,"Hema",13.12,True,"hi"}
print(a)
print("The length of set is:",len(a))
a.remove("hi")
print("The remove item is:",a)
b={13,14,15,16,17}
c={12,18,19,20,13}
d=b.intersection(c)
print("The common item (set)is:",d)
list1=[1,2,3,4]
list2=[1,2,5,6]
if set(list1)&set(list2):
        print("The common element is(list) exists")
else:
        print("The common element is(list) not exists")
difference=set(list1) - set(list2)   
print("The difference of two list is:",difference) 
l1=[1,2,3,4,5]
l2=[1,6,7,2,5,11]
l3=[1,2,5,12,13]
common=set(l1) & set(l2) & set(l3)
print("The common elemtns in three list are:",common)
e={12,"Hema",12.13,True}
f=tuple(e)
print("tuple:",f)
g=(13,"Hi",12.34,True)
h=set(g)
print("set:",h)
i={14,"Hello",15.17,True}
j=list(i)
print("List:",j)
k={'f','u','l','l','s','t','a','c','k'}
l=("".join(k))
print("The string is:",l)
m="course"
n=set(m)
print("The set is:",n)
o={"a","b","c"}
p=dict.fromkeys(o,1)
print("The dictionary is:",p)
q={1,2,3,4,}
r={5,1,3,6,7}
p=q-r
print("The difference is:",p)
s=q.symmetric_difference(r)
print("The symmetric difference is:",s)
print("Set is subset:",q.issubset(r))
t={"a","B"}
t.clear()
print(t)
u=frozenset([1,2,3])
print("The frozenset is:",u)
v={1,2,3,4}
w={3,4,5}
v.difference_update(w)
print("Remove the intersection of a 2nd set from the 1st set:",v)
x={2,3,4,5,6,7,8,11}
count=0
for num in x:
    if num>1:
      prime=True
    for i in range(2,num):
      if num % i==0:
          prime=False
          break
    if prime:
         count+=1
print("prime number:",count)
y={"kumar","Ravi","kuna"}
count=0
for name in y:
 if "ku" in name:
  count+=1
print("Count:",count)  
vowels="aeiouAEIOU"
for n in y:
   count1=0
   for ch in n:
      if ch in vowels:
         count1+=1
   print(n,"=",count1)  
   z={6,10,28,15,20}
   print("Perfect numbers:")
   for n in z:
       total=0
       for i in range(1,n):
           if n% i==0:
               total+=i
               if total==n:
                   print(n)
even=0
odd=0
for n in z:
    if n%2==0:
        even+=1
    else:
        odd+=1
        print("Even numbers:",even)
        print("odd numbers:",odd)









