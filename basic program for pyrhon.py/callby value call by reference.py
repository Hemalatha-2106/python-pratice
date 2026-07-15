a=10
b=a
b+=1
print(a)
print(b)
a=[1,2,3,5,7]
b=a.copy()
b[1]=20
print(a)
print(b)
b=list(a)
c=a+b
print(c)
a.append(b)
a.extend(b)
print(a)
print(b)


