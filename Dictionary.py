#Dictionary is a collection of related data PAIRS
#For instance, if we want to store the username and age of 5 users, we can store them in a dictionary
#To declare a dictionary, write dictionaryName = {dictionary key : data}

userNameAndAge = {"Peter":38, "John":51, "Alex":13, "Alvin":"Not Available"}
print (userNameAndAge)

#To declare a dictionary using the dict() method
userNameAndAge = dict(Peter = 38, John = 51, Alex = 13, Alvin = "Not Available")
print (userNameAndAge)

#To access individual items in the dictionary
#{dictionary key: data}
print (userNameAndAge["John"])

#To modify items in a dictionary, write dictionaryName[dictionary key of item to be modified] = new data
userNameAndAge["John"] = 21
print (userNameAndAge)

#Declaring a dictionary without assigning any initial values to it
#simply write dictionaryName = {}

#To add items to a dictionary 
#write, dictionaryName[dictionary key] = data
userNameAndAge["Joe"] = 40
print (userNameAndAge)

#To remove items from a dictionary
#write, del dictionaryName[dictionary key]
#remove "Alex"
del userNameAndAge["Alex"]
print (userNameAndAge)


#Declaring the dictionary, dictionary keys and data can be of different data types
myDict = {"One":1.35, 2.5: "Two Point Five", 3:"+", 7.9:2}

#print the entire dictionary
print (myDict)

#print the item with key = "One"
print(myDict["One"])

#print item with key = 7.9
print (myDict[7.9])

#modify the item with key = 2.5 and print the updated dictionary
myDict[2.5] = "Two and a Half"
print (myDict)

#add a new item and print the updated dictionary
myDict["New item"] = "I'm new"
print (myDict)

#remove the item with key = "One" and print the updated dictionary
del myDict["One"]
print(myDict)