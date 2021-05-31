#All control flow tools involve evaluating a condition statement
#The program will proceed differently depending on wether the condition is met
#Comparison signs: ==(equal), !=(not equal), <(smaller than), >(greater than), 
#<=(smaller than or equals to),>=(greater than or equals to)
#Logical operators: and,or,not 

#If Statement, commonly used contrl flow statements
#Allows the program to evaluate if a certain condition is met
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


userInput = input('Enter 1 or 2:')
if userInput =="1":
    print("Hello World")
    print("How are you")
elif userInput == "2":
    print("Python Rocks!")
    print("I love Python")
else:
    print("You did not enter a valid number")


#INLINE IF
#Inline if is a simpler form of an if statement and is more convenient 
# if only need to perform a simple task
#Syntax: do Task A if condition is true else do Task B
'''
num1 = 12 if myInt == 10 else 13
print("This is task A" if myInt == 10 else "This is task B")
'''

#FOR LOOP
#For loop executes a  block of code repeatedly until the condition in the statement is longer valid
#Examples of for loop with different types of sequences
#String
message = "Hello"

count = 0
for character in message:
    print(f'Index: {count}, Character: {character}')
    count += 1
#Tuple
def to_lower_case(my_tuple):
    temp_list = []
    for item in my_tuple:
        temp_list.append(str(item).lower())
    return tuple(temp_list)

fruits = ("Apple", "Orange", "BANANA")
fruits_new = to_lower_case(fruits)
print(fruits_new)
#List
list_ints = [1, 2, 3, 4, 5]
for i in list_ints:
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
#Set
set_cities = set()
set_cities.add("New York")
set_cities.add("New Delhi")
set_cities.add("Bangalore")
set_cities.add("London")
set_cities.add("Bangalore") #duplicate item, will be removed from set

for city in set_cities:
    print(city)
#Dictionary
my_dict = {"1": "Apple", "2": "Kiwi", "3": "Orange"}

for k, v in my_dict.items():
    print(f'Key={k}, Value={v}')
#Using break Statement to exit for loop 
messages = ["Hi", "Hello", "Exit", "Adios", "Hola"]

for msg in messages:
    if msg == "Exit":
        break
    print(f'Processing {msg}')
#For loop with continue statement
ints = (1, 2, 3, 4, 5, 6)
     #process only odd numbers
for i in ints:
    if i % 2 == 0:
        continue
    print(f'Processing {i}')
#For loop with range() function
for i in range(5):
    print("Processing for loop:", i)
#For loop with else statement
databases = ("MySQL", "Oracle", "PostgreSQL", "SQL Server")

for db in databases:
    print(f'Processing scripts for {db}')
else:
    print("All the databases scripts executed successfully.")
#Nested for loop 
list_tuples = [("Apple", "Banana"), ("Orange", "Kiwi", "Strawberry")]

for t_fruits in list_tuples:
    for fruit in t_fruits:
        print(fruit)
#Reverse Iteration using for loop and reversed() function
numbers = (1, 2, 3, 4, 5)

for n in reversed(numbers):
    print(n)
#The for loop variables leaking to global scope
global_var = "global"
for c in range(1, 3):
    x = 10
    global_var = "for variable"
    
print(c) #variable is defined in the for loop
print(x) #variable is defined in the for loop 
print(global_var) #global variable

#looping through an iterable
#An iterable refers to anything that can be looped, such as a string, list or tuple
#Syntax: for a in iterable:
#            print (a)
pets = ['cats', 'dogs', 'rabbits','hamsters']
for myPets in pets:
    print (myPets)
#Display the index of the members in the list
for index, myPets in enumerate(pets):
    print (index, myPets)   
#How loop through a string
message = 'Hello'
for i in message:
    print(i)
#Looping through a sequence of numbers
#The built-in range() function comes in handy when looping through a sequence of numbers
#The range() function generates a list of numbers and hs the syntax (start, end, stop)
for i in range(5):
    print (i)

#WHILE LOOP
#while loop is used to repeat a block of code until the specified condition is false
#Syntax:         while condition is true:
#                    do A
def print_msg(count, msg):
    while count > 0:
        print(msg)
        count -= 1
        
print_msg(3, "Hello World")

#while loop with break statement
while True:
    i = input('Please enter an integer (0 to exit):\n')
    i= int(i)
    if i == 0:
        print("Exiting the program")
        break
    print(f'{i} square is {i ** 2}')
    
#while loop with continue statement
while True:
    i = input('Please enter an integer (0 to exit):\n')
    i = int(i)
    if i < 0:
        print("The program works with Positive Integers only.")
        continue
    if i == 0:
        print("Exiting the Program")
        break
    print(f'{i} square is {i ** 2}')
    
#while loop with else statement
count = 5

while count > 0:
    print("Welcome")
    count -= 1
else:
    print("Exiting the while loop")
#change the program to break out of the while loop
count = 5

while count > 0:
    print("Welcome")
    count -= 1
    if count == 2:
        break
else:
    print("Exiting the while loop")    
    
#Nested while loop
i = 3
j = 3

list_tuples = []
while i > 0:
    while j > 0:
        t = (i, j)
        list_tuples.append(t)
        j -= 1
    j = 3
    i -= 1
    
print(list_tuples)

#BREAK
#break keyword is used if you may want to exit the entire loop when certai  condition is met
#break statement with for loop 
t_ints = (1, 2, 3, 4, 5)

for i in t_ints:
    if i == 3:
        break
    print(f'Processing {1}')

print("Done")

#break statement with the while loop
count = 10

while count > 0:
    print(count)
    if count == 5:
        break
    count -= 1
    
#break statement with a nested loop
list_of_tuples = [(1, 2), (3, 4), (5, 6)]

for t in list_of_tuples:
    for i in t:
        if i == 3:
            break
        print(f'Processing {i}')
        
#CONTINUE
#when continue keyword is used, the rest of the loop "after" the keyword is skipped for that "iteration"
#Continue statement with for loop
t_ints = (1, 2, 3, 4, 5)

for i in t_ints:
    if i == 3:
        continue
    print(f'Processing integer {i}')

print("Done")
 
#Continue statement with the while loop
count = 10

while count > 0:
    if count % 3 == 0:
        count -= 1
        continue
    print(f'Processing Number {count}')
    count -= 1

#continue statement with a nested loop
list_of_tuples = [(1, 2), (3, 4), (5, 6, 7)]

for t in list_of_tuples:
    #don't process tuple with more than 2 elements
    if len(t) > 2:
        continue
    for i in t:
        #don't process if the tuple element value is 3
        if i == 3:
            continue
        print(f'Processing {i}')

#TRY, EXCEPT statement
#This statement controls how the program proceeds when an error occurs
#Syntax:
# try:
#     do something
# except:
#     do something else when an error occurs
#Exceptions are error scenarios that alter the normal execution flow of the prgram
#Exception handling is achieved by three keyword blocks: try,except and finally
#Try block contains the code that may raise exceptionsor errors
#Except block is used to catch the exceptions and handle them
#Catch block is executed only when the corresponding exception is raised
#Finally block is always executed, whether the program executed properly or it raised an exception
def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
        
divide(10, 2)
divide(10, 0)
divide(10, 4)
#Handling multiple Exceptions in a single except block
def divide (x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
#Catch-All exceptions in a single except block
def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
    except:
        print("unknown error occurred")
#using else bock with try-except
def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print("divide() function worked fine.")
        
divide(10, 2)
divide(10, 0)
divide(10, 4)
#Using finally block with try-except
def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print("divide() function worked fine.")
    finally:
        print("close all the resources here")
        
divide(10, 2)
divide(10, 0)
divide(10, 4)
#python exception handling syntax
#Raising exceptions
#Some of the possible scenarios are:
# .Function input parameters validation fails
# .Catching an exception and then throwing a custom exception
class ValidationError(Exception):
    pass

def divide(x, y):
    try:
        if type(x) is not int:
            raise TypeError("Unsupported type")
        if type(y) is not int:
            raise TypeError("Unsupported type")
    except TypeError as e:
        print(e)
        raise ValidationError("Invalid type of arguments")
    
    if y is 0:
        raise ValidationError("We can't divide by 0.")
    
try:
    divide(10, 0)
except ValidationError as ve:
    print(ve)

try:
    divide(10, "5")
except ValidationError as ve:
    print(ve)
#Nested try-except blocks example
'''We can have nested try-except blocks in Python. 
In this case, if an exception is raised in the nested try block, 
the nested except block is used to handle it. 
In case the nested except is not able to handle it, 
the outer except blocks are used to handle the exception.
'''
x = 10
y = 0

try:
    print("outer try block")
    try:
        print("nested try block")
        print(x / y)
    except TypeError as te:
        print("nested except block")
        print(te)
except ZeroDivisionError as ze:
    print("outer except block")
    print(ze)
