myset={"a","b",1,2,3,"b"}
print(myset)

print(len(myset))
print(type(myset))

for i in myset:
    print(i)

myset.add("Shubham")
print(myset)
myset.add(5)
print(myset)

myset2={34,"shu",99}
myset.update(myset2)

print(myset)

myset.remove("Shubham")
print(myset)

x=myset.pop()
print(x)

print(myset)
#del myset

myset.clear()
print(myset)

set1={1,2,3,4, "d"}
set2={'a','b','c','d', 4}

newset=set1.union(set2)
print(newset)

newsetop = set1|set2
print(newsetop)

newset1=set1.intersection(set2)
print(newset1)

newsetop2=set1&set2
print(newsetop2)

newset2=set1 -set2
newset3=set2.difference(set1)
print(newset2)
print(newset3)