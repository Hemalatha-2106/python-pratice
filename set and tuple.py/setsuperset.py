set1={1,2,3}
set2={4,5,6}
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
set3=set1.copy()
print("set1:",set1)
print("set3:",set3)
set1.add(7)
print("The added item is:",set1)
set2.remove(6)
print("The remove item is:",set2)
set3={8,9,10}
set3.discard(9)
print("The delete particular item:",set3)
