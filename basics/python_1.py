import math

print("python first code")

def first_code(n):
    print(n)
    
first_code(4)

# to open python shell in terminal write "python" and to exit type "ctrl z"

# data types in python : mutable and immutable

username = "zaid"  # here is string is immutable
print(username)   # ans: zaid

username = "khan"
print(username)  # ans : khan


#immutable means which cannot be changed
# here "zaid" is not changed in to "khan" a new refernce "khan" is sepereately created, obj "zaid" is still the same
# usernmae -> zaid (obj 1 in memory)   after change   username -> khan (obj2 in memory) [no attribute is pointing to zaid now hence it will be deleted]


x = 10  # integer is also immutable meaning it cannot be changed
print(x)  # ans : 10
y = x
print(y)  # ans : 10
x = 12
print(y)  # ans : 10

# here x and y were referring to same obj "10" than we changed x -> 12 but y was still referring to "10" and not "12" (x and y are referring to objects which we call there value)


# strings  (immutable)
fruit = "apple"
print("length of string fruit is: ",len(fruit))  # ans : 5
print("0th value in fruit :", fruit[0])  # ans : a
print("slicing in string value fruit from index 1 to 3: ", fruit[1:3])  # ans : pp 
# fruit[0] = "A" (this will not work as string is immutable and cannot be changed)

# lists (mutable)
my_list =  [123, "zaid", False]
print(my_list)
print(my_list[0])  # ans : 123
print("length of list : ", len(my_list))  # ans : 3

# dictionaries (mutable)
myD = {"name" : "zaid", "surname": "khan", "age": 20, "isMarried": False}
print(myD)
print(myD["age"])  # ans : 20
print("length of dictionary: ",len(myD)) # ans : 4

# tuples (immutable)
myTup = (1, "zaid")
print(myTup)
print("length of tuple: ", len(myTup))


a = "zaid"
a = 10
a = False
# here "a" is just a reference that is pointing to the data "a" does not have any data type
# but False "zaid" 10 this all data in memory have datatypes string , number, boolean

 
# numbers in python
x = 2
y = 3
z = 4
equation = x + (y * z)  # here (*) operation will happen first
num1 = int(2.23)  # output = 2
num2 = int(40) # output = 40.00
name1 = "chai"
name2 = "Code"
ans = name1 + name2  # concatenation of both (opearator overloading)
print(ans)  # output = chaiCode
print(z ** 2) # output = 16 (square of '4') 
name3 = 'Hello\nWorld'
str(name3) # ouput = 'hello world'(world is in next line) (str gives human readable output)
print(name3 ) # ouput = hello world (world is in next line) (print internally uses str)
repr(name3) # output = "'Hello\nWorld'"  (repr prints the exact statement)
x = 2
y = 3
z = 4
print(x<y<z) # output = True (x<y<z  => x < y && y < z  in simple means)
print(1 == 2 < 3) # output = False (1 == 2 && 2 < 3)

# now lets see some operations using math library
num1 = math.floor(3.5)
print(num1)  # output = 3 (nearest lower round-off value) (always towards bottom)
num1 = math.floor(-3.5)
print(num1)  # output = -4
num2 = math.trunc(3.5)
print(num2)  # output = 2 (nearest to zero round-off value) (always towards zero)
num2 = math.trunc(-3.5)
print(num2)  # output = -2

#operations on sets
setone = {1,2,3,4}
interception = setone & {1,3,5,6}
print(interception)  # output = {1,3} both are common elements on both side
union = setone | {5,3,0}
print(union)  # output = {0, 1, 2, 3, 4, 5}  combination of all elements on both side
example = setone - {1,2,3,4}
print(example)  # output = set()  (instead of {} the output is set()..... because {} denotes dictonary not set )

booolean = True + 3
print(booolean)  # output = 4 (becoz True i treated as 1 , and False is treated as 0)


# Strings in python
greet = "Hello World"
first_letter = greet[0]
print(first_letter)  # ouput = H
slice_greet = greet[0:5]  # 0 for first letter and 5 for the last letter
print(slice_greet)  # output = "Hello"
print(greet.upper())  # output = HELLO WORLD
print(greet.lower())  # output = hello world
print(greet.find("World"))  # output = 6 (gives the starting index from whrere the word "World" begins)

greet1 = "   Hello World  "
print(greet1)  # output = '  Hello World  '
print(greet1.strip())  # output = 'Hello World'

greet2 = "Good Morning"
print(greet2.replace("Morning", "Evening"))  # otput = Good Evening

# string to list conversion
chai = "Lemon, Green, Yellow, Masala"
print(chai.split())  # output = ['Lemon,', 'Green,', 'Yellow,', 'Masala']  (here splitting is automatically done on basis on spaces)
print(chai.split(", "))  # output = ['Lemon', 'Green', 'Yellow', 'Masala'] (here splitting is done based on ", ")

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)  # output = I ordered {} cups of {} chai
print(order.format(quantity, chai_type))  # output = I ordered 2 cups of Masala chai

# list to string conversion
chai_variety = ["Masala", "Lemon", "Yellow", "Green"]
print("".join(chai_variety))  # output = MasalaLemonYellowGreen
print(", ".join(chai_variety))  # output = Masala, Lemon, Yellow, Green

statement = "He said , \"Good Morning\" "
print(statement)  # output = He said , "Good Morning"  (by using \ we can put "" inside a string)
chai = r"Masala\nChai"
print(chai)  # output = Masala\nChai  (using r"" gives raw string in output)


# Lists in python
tea_varities = ["black", "green", "yellow", "Oolong"]
print(tea_varities)  # output = ['black', 'green', 'yellow', 'Oolong']
print(tea_varities[0])  # output = black
print(len(tea_varities))  # output = 4
print(tea_varities[1:3])  # output = ['green', 'yellow']
tea_varities[3] = "Herbal"  # replacing a value in list
print(tea_varities)  # output = ['black', 'green', 'yellow', 'Herbal']
# tea_varities[2:3] = "Lemon"
# print(tea_varities)  # output = ['black', 'green', 'L', 'e', 'm', 'o', 'n', 'Herbal']
# to solve above issue
tea_varities[2:3] = ["lemon"]
print(tea_varities)  # output = ['black', 'green', 'lemon', 'Herbal']

#replacing multiple values
tea_varities[2:4] = ["masala", "yellow"]
print(tea_varities)  # output = ['black', 'green', 'masala', 'yellow']

# printing list using loop
for tea in tea_varities:   # this will print values one by one in every line
    print(tea)

for tea in tea_varities:  # here instead of printing in new line it will print after placing "-"
    print(tea, end="-")
print("\n")

# to add new value in list
tea_varities.append("Oolong")
print(tea_varities)  # output = ['black', 'green', 'masala', 'yellow', 'Oolong']
tea_varities.insert(3, "Lemon")  # to insert value in between the list
print(tea_varities)  # output = ['black', 'green', 'masala', 'Lemon', 'yellow', 'Oolong']

#to remove value from the list
tea_varities.pop()
print(tea_varities)  # output = ['black', 'green', 'masala', 'yellow']
# tea_varities.remove("green")  this method removes value from between the list

nums = [x for x in range(11)]
print(nums)  # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [x**3 for x in range(11)]
print(square)


# dictonary in python
student = {"name":"zaid", "rollno": 21, "marks":67, "isPassed":True}
print(student["name"])  # output = zaid
print(student.get("isPassed"))  # output = True

# loops in dictionary
for stu in student:  
    print(stu)  # this will give only the keys in output (name, rollno, marks, ispassed)

print("\n")

for st in student:
    print(st, student[st])   # this will print both key and value
    
# for key,value in student.items():
#    print(key,value)   # another way to print both key and value

# add key and value in dictionary
student["year"] = "third"
print(student)  # output = {'name': 'zaid', 'rollno': 21, 'marks': 67, 'isPassed': True, 'year': 'third'}

# to remove key and value from dictioary
student.pop("year")  #  you have to pass the key in this function
print(student)  # output = {'name': 'zaid', 'rollno': 21, 'marks': 67, 'isPassed': True}

# student.popitem()   # this method will automatically remove the key value pair

nums = {x:x for x in range(11)}
print(nums)  # output = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
square = {x:x**2 for x in range(11)}
print(square)  # output = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
square.clear()  # to clear all values in dictionary
print(square)  # output = {}

# keys and values accessed seperately:
keys = ["masala", "yellow", "Oolong"]
defaut_value = "Delicious"
new_dict = dict.fromkeys(keys, defaut_value)
print(new_dict)  # output = {'masala': 'Delicious', 'yellow': 'Delicious', 'Oolong': 'Delicious'}


#tuples in python  (similar to lists but immutable -> cannot be changed in memory)
tea_types = ("black", "yellow", "green")
print(tea_types)  # output = ('black', 'yellow', 'green')
print(tea_types[1])  # output = yellow
print(len(tea_types))  # output = 3

tea_types1 = ("herbal", "masala")
all_tea = tea_types + tea_types1
print(all_tea)  # output = ('black', 'yellow', 'green', 'herbal', 'masala')
# tuple can have duplicate values

# tea_types[0] = "masala"  (this will give error as value cannot be changed in tuples)


# conditionals problems in python

# Age group categorization
age = int(input("provide me your age: "))   # here defining datatype is necesarry otherwise output can be in correct

if age >= 120:
    print("invalid age")
    exit()

if age < 13:
    print("user is child")
elif age < 20:
    print("user is teenager")
elif age < 60:
    print("user is adult")
else:
    print("user is a senior citizen")

# Movie ticket pricing (different conditional syntax)
age1 = int(input("enter your age: "))
day = input("enter day: ")

price = 12 if age1 < 12 and day == "wednesday" else 22   # syntax -> price = value_if_true if condition else value_if_false

print(price)


# loops problem in python

# given a list of numbers count how many are positive:

n = int(input("Enter size of list: "))

numbers = []

for i in range(n):
    num = int(input(f"enter number {i+1}: "))
    numbers.append(num)
    
negative_count=0

for num in numbers:
    if num < 0:
        negative_count += 1

print("final list: ", numbers)
print("number of negative integers in the list: ",negative_count)

# multiplication table (skip 5th iteration)
n = 10

for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i*n)

# return first non-repeated character:
input_str = "teetercdacb"

for char in input_str:
    if input_str.count(char) == 1:
        print("first non repeated character is: ", char)
        break

# calculate factorial of a number (using while loop)
number = 5
fact =1

while number > 0:
    fact = fact * number
    number -= 1



# functions in python

# write a function that returns both area and circumference of a circle given the radius:

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    return area, circumference

a, c = circle(4)

print("Area: ",a)
print("Circumference: ",c)

# create a lambda function to compute the cube of a number

cube = lambda x : x ** 3  

print(cube(3)) 

# write a function that takes number of arguments and returns their sum (function with *args) 

def sum_all (*number):
    return sum(number)

print(sum_all(1,2))
print(sum_all(1,3,4))

# create a function that accepts any number of keyword arguments and prints them in the format key:value (function with **kwargs)

def print_kwargs(**param):
    for key, value in param.items():
        print(f"{key}: {value}")

print_kwargs(name="Zaid", age=19, city="Mumbai")
print_kwargs(name="jhon", surname="snow")



# closure in python

def outer(msg):
    def inner():
        print(msg)
    return inner

f = outer("Hello Python")
f()     #  output = Hello Python  (here eve though the outer function is over we just returned the inner function to f(), still the inner fucntion remembers the variable/values of outer function)



