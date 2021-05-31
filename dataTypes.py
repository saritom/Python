#data types 
#intergers, variableName = initial value
#intergers are numbers with no decimal parts, such as -5, -4, 0, 5, 8
userAge = 20
mobileNumber = 12398724
print (userAge)
print (mobileNumber)

#float
#float refers to numbers that have decimal parts, such as 1.234, -0.0023, 12.01
# declaring, variableName = initial value

userHeight = 1.82
userWeight = 67.2
print (userHeight)
print (userWeight)

#strings
#string refers to text 
#declaring, variableNmae = "initial value"

userName = 'Peter'
userSpouseName = "Janet"
userAge = '30'
print (userName)
print (userSpouseName)
print (userAge)

#multiple substrings by use of the concatenate sign (+)
userName = "Peter" + "Lee"
print (userName)

#built-in string functons
userName = 'Peter'.upper()
print (userName)

#formatting strings using the % operator
#syntax, "string to be formatted" %(values or variables to be inserted into string, separated by commas)
#the round brackets () with values inside is actually known as tuple
brand = 'Apple'
exchangeRate = 1.235235245 

message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' % (brand, 1299, exchangeRate)
print (message)
#%s formatter is used to represent a string("Apple"in this case) while 
# the %d formatter represents an interger (1299)
#%f formatter is used to format floats(numbers with decimals) 
# %4.2f where 4 refers to total length and 2 refers to 2 decimal places


#formatting strings using the format () method
#syntax, "string to be formatted".format(values or variables to be inserted into string, separated by commas)
brand = 'Apple'
exchangeRate = 1.235235245 

message = 'The price of this {0:s} laptop i {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print (message)
"""
The parameter ‘Apple’ has a position of 0,
1299 has a position of 1 and
1.235235245 has a position of 2.
Positions always start from ZERO.
When we write {0:s}, we are asking the interpreter to replace {0:s} with
the parameter in position 0 and that it is a string (because the formatter is ‘s’).
When we write {1:d}, we are referring to the parameter in position 1,
which is an integer (formatter is d).
When we write {2:4.2f}, we are referring to the parameter in position 2,
which is a float and we want it to be formatted with 2 decimal places and
a total length of 4 (formatter is 4.2f).
"""

