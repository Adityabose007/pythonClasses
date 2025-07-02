myList = [20, "Coding", 99.9, "Java#"]

print(myList)
print(myList[0])  # Accessing the first element

print(myList[1])  # Accessing the second element

print(len(myList)) # Getting the length of the list

myList[1] = "Python Programming"  # Modifying the second element
print(myList)


myList.extend(["Java", "C++"])  # Adding multiple elements to the list
print(myList)


print(myList[-1])  # Accessing the last element using negative indexing



#slicing
print(myList[1:4])  # Slicing the list from index 1 to 3 (4 is exclusive)
print(myList[-4:-1])   # Slicing the list from start to index 2 (3 is exclusive)
print(myList[2:])  # Slicing the list from start to index 2 (3 is exclusive)
print(myList[:6])  # Slicing the list from index 2 to end

print(myList[1::2])  # Slicing the list from index 1 to end with a step of 2
print(myList[::-1])  # Reversing the list using slicing


myList.insert(2, "JavaScript")  # Inserting an element at index 2
print(myList)



#adding

myList.append("C#")  # Adding an element to the end of the list
print(myList)

list2 = [1, 2, 3]
myList.extend(list2)  # Extending the list with another list
print(myList)

newList = myList + list2  # Concatenating two lists
print(newList)

# Removing elements
myList.remove("Java")  # Removing the first occurrence of "Java"   
print(myList)

'''myList.pop(2)  # Removing the element at index 2
print(myList)

myList.clear()  # Clearing the entire list
print(myList)  # Printing the cleared list (should be empty)


myList.delete(1)  # Deleting the element at index 1
print(myList)  # Printing the list after deletion (should be empty)'''

#loop Lists
for item in myList:
    print(item)  # Printing each item in the list
print("Showing the Elements:")
for i in range(len(myList)):
    print(myList[i])  # Printing each item in the list using index



list3 = [1, 2, 3, 4, 5]
list3.sort()  # Sorting the list in ascending order
print(list3)  # Printing the sorted list


list4 = ["bmw" , "audi", "mercedes", "tesla"]
list4.sort(reverse=True) # Sorting the list in descending order
print(list4)  # Printing the sorted list`

thisIsList = list(("hello", 24, True))
print(thisIsList)  # Printing the list created from a tuple
print(type(thisIsList))  # Printing the type of the list


#Tuples

myTuple = ("Tuple", 2, 3, 4, 5, "Data")  # Creating a tuple

print(myTuple)  # Printing the tuple

print(myTuple[0])  # Accessing the first element of the tuple
print(myTuple[-1])  # Accessing the second element of the tuple


print(len(myTuple))  # Getting the length of the tuple


#Slicing tuples
print(myTuple[1:5])  # Slicing the tuple from index 1 to 3 (4 is exclusive)

print(myTuple[-4:-1])  # Slicing the tuple from third last to second last

for i in myTuple:
    print(i)  # Printing each item in the tuple

for i in range(len(myTuple)):
    print(myTuple[i])  # Printing each item in the tuple using index


