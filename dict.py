mydict = {
    "rollno":1,
    "name":"a",
    "subject":"bca",
    "year":2000
    }
print(mydict)
print(mydict["name"])
print(len(mydict))

for i in mydict:
    print(i)

for i in mydict:
    print(i,"---->", mydict[i])
    #print(mydict[i])

mydict["name"]="Alice"
print(mydict)

mydict["color"]="red"
print(mydict)

mydict.pop("color")
print(mydict)

mydict.popitem()
print(mydict)

mydict.clear()
print(mydict)

#del mydict
#print(mydict)