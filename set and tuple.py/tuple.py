a=(12,"Hello")
print("Tuple:",a)
print("size of tuple:",len(a))
b=(40,30,35,10)
s_t=tuple(sorted(b))
print("Sorted tuples:",s_t)
c=[12,"Hema",35.78,True]
print("There are different type of tuple:",c)
d=("Hema",22,"Madurai")
name,age,city=d
print(name)
print(age)
print(city)
e= ('f','u','l','l','s','t','a','c','k')
f=("".join(e))
print("The string is:",f)
print("4th element:",e[4])
print("4th element for last:",e[-4])
for i in e:
    if e.count(i)>1:
        print("The repeted elements are:",i)
        g=(10,20,30)
        m=30
if m in g:
            print("The element is exists")
else:
            print("The element not exists")
h=[12,13,14,15,16]
i=tuple(h)
print("Tuple",i)
h.remove(13)
print("Remove the item:",h)
k=(17,18,19,20,21,22)
print("Slice tuple:",k[0:4])
print("Index of 20:",k.index(20))
l=k[::-1]
print("The reverse  tuple:",l)
m=["hi","hello","fine"]
n=tuple(m)
print("The Tuple is:",n)
