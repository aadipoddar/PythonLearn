import cv2
import math

print("Hello World\n")


print("Hello World")

print(5 + 8)

print("5 + 8")

print(math.gcd(3,6))

if (5>4): #This is the ehader part
    print("5 is greater than 4") #This is body part
    print("Got it!")

else:  #This is the ehader part
    print("Bye guys!")  #This is body part

'''
this is a multiline comment
'''

#It's a single line comment

print("Hello Everyone")

'''
It's a multi
line
comment
'''

print("Hope you understood about comments")

i = 0

'''
while (i<10) : #This is a header part
    print(i+1) #This is a body part
    i-i+1
'''




print("Here we will use some math functions")
a = 2
b = 4
c = math.sqrt(16)
d = math.pow(a,b)
print(c)
print(d)



print("\t\tType Casting")

a = 52
b = 58.68
c = "Demo"

print(type(a))
print(type(b))
print(type(c))


print("\t\tType Casting\n")

a = 15
b = "25"
print(type(b))
b = int(b)
print(type(b) )
print("Sum of a and b is",a+b)


print("\t\t Strings")

a = "Hello"
print(a)

demo = '''
This is an
example of
multi-line
string.
'''
print((b))


print("\t\t Strings")

a = "Hello"
print(a[0])
print(a[1])
print(a[2:5])


print("\t\t Strings")

a = "   Hello  "
print(a)
print(a.strip())


print("\t\t Strings")

a = "Hello"
print(a)
print(len(a))


print("\t\t Strings")

a = "Hello"

print(a)
print("\n")
print(a.lower())



print("\t\t Strings")

a = "Hello"

print(a)
print("\n")
print(a.upper())



print("\t\t Strings")

a = "Hello"
print(a)
print(a.replace('ello', 'i'))


print("\t\t Strings")

a = "Hello"
b = " Guys"
print(a+b)


print("\t\t Strings")

a = "Demo"
b = "Format"
print("This is the {} string".format(a,b))
print("This is the {0} string".format(a,b))
print("This is the {1} string".format(a,b))


print("\t\t Strings")

a = "Demo"
b = "Format"
print(f"This is a {a} of {b} string")


print("\t\tList\n")

lst = [8,5,2,9,7]

print(lst)
print(type(lst))

print(lst[0])
print(lst[1])
print(lst[2: 5])


lst = [8,5,2,9,7]

print(lst)
print(type(lst))

lst.append(99)      #append runction
print(lst)


lst = [8,5,2,9,7]

print(lst)
print(type(lst))

lst.insert(0,99)        #insert runction
print(lst)


lst = [8,5,2,9,7]

print(lst)
print(type(lst))

lst.remove(2)       #remove runction
print(lst)


lst = [8,5,2,9,7]

print(lst)
print(type(lst))

lst.pop()       #remove one element from list
print(lst)


lst = [8,5,2,9,7]

print(lst)
print(type(lst))

del lst[2]       #remove the element at index 2
print(lst)


lst = [8,5,2,9,7]

print(lst)
print(type(lst))

lst.clear()       #clears the list
print(lst)


print("\t\tTuples\n")

tup = ('Demo', 'Hello', 54, 'Guys')
print(tup)
print(type(tup))
tup = list(tup)
tup[1] = 99
print(tup)


print("\t\tSets\n")

set1 = {1,2,3,4,5,1,2,3}
print(set1)
print(type(set1))
set1.add(99)
print(set1)



print("\t\tSets\n")

set1 = {1,2,3,4,5,1,2,3}
print(set1)
print(type(set1))
set1.update([5,6,99,109,199])
print(set1)




print("\t\tDictionary\n")

dictionary1 = {
    "Play" : "Doing some activity",
    "Food" : "Something eatable",
    "Python" : "Language",
}

print(dictionary1)
print(len(dictionary1))



input()


print("\t Input statement \n")

a = int(input("Enter any number: "))
name = (input("Enter any name: "))
print(type(a))
print(a)
print(type(name))
print(name)


print("\t Conditional Statements \n")

x = int(input("Enter any number: "))
if (x>100):
    print("Number entered is greater than 100")

print("\t Conditional Statements \n")

print("\t Loops \n")

num = 5
for a in range(1, 11 ):
    print(num, 'x ', a, '=', num* a)

print("\t Loops \n")

x = 1
while(x<=100):      #while loop
    print(x)
    x = x+1



'''
def function_name () :

         statement 1,

         statement 2,

         ….
'''



print("\t Functions \n")

def demo():     #Derining a runction
    print("Hlo Guys")
    print("It's my First Function")
    print(" : )")

demo()      # Calling a runction



print("\t Functions \n")

def add(a,b):        #Derining Function
    c = a+b
    return c

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

z = add(x,y)        #Calling Function
print("The Sum is", z)


'''def function_name( parameters ) :

         statement 1

         statement 2'''




# import cv2
# import math

# This is a comment
# print("Hello world")
# print(math.gcd(3,6))
'''
This is a multi line comment

'''
# This is also a comment
# print(5+8)
# if(age<18):
#     print("hello")


a = 34
b = "Harry"
c = 45.32
d = 3

# print(a + d)
# print(a - d)
# print(a * d)
# print(a / d)

# Quiz: Try these operators:
# 1. ** Exponentiation operator
# 2. // Floor division operator
# 3. %  Modulo operator

# Wrong syntax
# harry project = 45 
# Rules for creating variables

# 1. variable should start wioth a letter or an underscore
# 2. variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensitive. Harry and harry are two different variables

# typeA = type(a)
# typeB = type(b)
# print(typeB)
e = "31"
e = float(e)
# e = str(455)
# e = int("34")
# e = 3.14
# print(type(e))
# print(e+2)


name = "Harry, Shubham, vikrant"
# print(name[2:5])
# print(name)
# print(name.strip())
# print(len(name))
var = name.lower()
var = name.upper()
var = name.replace("ar", "t")
var = name.replace(", ", '\n')
# print(var)

stri = "This is a "
name1 = "Harry"
name2 = "Rohan"
stri2 = "This is not a"
# print(stri + name)
# temp = "This is a {1} and he is a good boy named {0}".format(name1, name2)
temp = f"this is a {name2} and he is a good boy {name1}"
# print(temp)

'''
Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary

'''
# List
lst = [61,2,3,4,6,41]
# var = type(lst)
# lst[2] = 45
# var = lst[2]
# lst.append(100)
# lst.insert(1,100)
# lst.remove(61)
# lst.pop()
# del lst[3]
# del lst
lst.clear()
var = lst
# var = len(lst)
# var = lst[1:4]
# print(var)


# Tuple
a = ("Harry", "Shubh", "Rohan")
# var = a
a = list(a)
var = type(a)

# Cannot do this
a[0] = "Vikrant" 
# print(var)

# Set
s1 = {23,2,2,2,2,2,7,3,2,1,2,2,12,7,6,3,12,}
# s1.add(44444)
# s1.update([12,12,423,3423,634,123,432,23])
# print(len(s1))
# s1.remove(1666)
# Like list you can use: .pop, .clear, del
# and.. intersection, union
# s1.discard(1666)
# print(s1)

harryDict = {
    "Name": "Harry",
    "Class": "4th",
    "Marks": 34.34,
    "Hours In School": 6
}
harryDict["Marks"] = 34
# print(harryDict["Marks"])
harryDict.pop("Marks")
# del, clear, pop, update
# print(harryDict)

# age = 34
# age = input("Enter Your Age\n")
# age = int(age)
# # print(type(age))
# if(age>18):
#     print("You can drive a car")

# elif(age==18):
#     print("You are an awesome teen")

# else:
#     print("You cannot drive")    


# Loops:
# Scenario: you have to print numbers between 1 to 1000
# for i in range(0, 1000):
#     print(i)

# li = [1, 432, "this"]
# for item in li:
#     print(item)
# # Quiz: Use for loop to iterate dictionary, set and tuples  
# i = 0
# while(i<100):
#     i = i + 1
#     if i == 78:
#         continue
#     print(i+1)

# Functions:
# def greet():
#     print("Good morning sir")
#     print("Good morning mam")
#     print("Good morning Uncle")

# greet()     

# def sum(a, b):
#     print("Running sum")
#     c = a + b
#     return c

# d = sum(34, 45)
# print(d)

class Employee:
    def __init__(self, gname, gsalary):
        self.name = gname
        self.salary = gsalary

harry = Employee("harry", 34)
print(harry.name)
print(harry.salary)