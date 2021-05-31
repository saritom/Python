#list refers to a collection of data which are normally related
#To declare a list, listName = [initial values]
#Note the use of square brackets[] when declaring a list
#Multiple values are separated by a comma

userAge = [21, 22, 23, 24, 25]
print(userAge)

#Individual values in the list are accessible by their indexes
#Indexes always start from ZERO, not 1
userAge0 = userAge
print (userAge0)
userAge2 = userAge
print (userAge2)

userAge3 = userAge[2:4]
print (userAge3)
#Assigning items with index 2 to index4-1 from the list userAge3
#userAge3 = [23, 24]
#The notation 2:4 is known as slice
userAge4 = userAge[1:5:2]
print (userAge4)

#To modify items in alist, write listName[index of the item to be modified] = new value
userAge[1] = 5
print (userAge)

#To add items in alist, use append() function
userAge.append(99)
print (userAge)

#To remove items, write del listName[index of the item to be deleted]
del userAge[2]
print (userAge)


#To fully appreciate the workings of a list, try running the following program
#declaring the list, list elements can be of different data types
myList = [1, 2, 3, 4, 5, "Hello"]
print(myList)

#Print the third item (recall: index starts from zero)
print(myList[2])

#print the last item
print(myList[-1])

#assign myList (from index 1 to 4) to myList2 and print myList2
myList2 = myList[1:5]
print(myList2)

#modify the second item in myList and print updated list
myList[1] = 20
print(myList)

#append a new item to myList and print the updated list
myList.append("How are you")
print (myList)

#remove the sixth item from myList and print the updated list
del myList[5]
print (myList)