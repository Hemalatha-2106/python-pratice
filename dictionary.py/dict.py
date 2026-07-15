d1={}
n=int(input("Enter the pairs"))
for i in range(n):
    k=int(input("Enter the keys"))
    v=input("Enter the value")
    d1[k]=v
    print("dict.elements:",d1)
d={1:"R",2:"P"}
print(d[2])
d[3]="k"
print(d)
d.popitem()
print(d)
del d[1]
print(d)
d.clear()
print(d)
a1={1:"R",2:"H",3:"P"}
a2="STS"
a3={"R","h","P","S"}
a4={1,2,3,4}
print(a1)
print(a1.keys())
print(a1.items())
print(a1.values())
print(dict.fromkeys(a3,a4))
print(dict(zip(a3,a4)))
