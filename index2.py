### Try 1
"""
equation = "130 + 145 = 275"
for symbol in equation:
    if symbol not in "11":
        print(symbol)

print("Hello", end=" ")
print("World!")
"""

#### Try 2
'''
print("Python", "is", "fun", sep="🔥")
'''

### Try 3
##:Use with for file handling to ensure files are closed properly
'''
# - better ✔
with open("file.txt", "r") as file:
    content = file.read()

# - traditional method 👎🏾
file = open("file.txt", "r")
content = file.read()
file.close()
'''

### Try 4
##:Use function parameters and return values instead of modifying global state.
'''
# - better ✔
def add_numbers(a, b):
    return a + b

# - traditional method 👎🏾
total = 0
def add_to_total(num):
    global total
    total += num
'''

###: Try 5
##:Catch specific exceptions and handle them appropriately
'''
# - better ✔
try:
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero.")

# - traditional method 👎🏾 __catch's exceptions without handling them properly.
try:
    result = 10 / x
except Exception as e:
    pass
'''

#### Try 6
##:Inline Expressions
'''
name = "Henry"
age = 18
print(f"{name} will be {age + 5} years old in 5 years.")
'''

### Try 7
##:Use loops and functions to eliminate duplication.
'''
users = ["Herr Goethe", "Frau Merkel", "Frau Ine", "Herr Geoff"]

# - better ✔

def greet_users(users):
    for user in users:
        print(f"Hallo, {user}!")

greet_users(users)

# - traditional method 👎🏾

print(f"Hallo, {users[0]}!")
print(f"Hallo, {users[1]}!")
print(f"Hallo, {users[2]}")
print(f"Hallo, {users[3]}!")
'''

##:Debugging with `=``
'''
x = 10
y = 20
print(f"{x = }, {y = }, sum = {x + y}")
'''


##:Dictionary Get Method to Avoid KeyErrors
'''
data = {"name": "Alice"}
print(data.get("age", "Not found"))
'''

##Unpacking Multiple Values
'''
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c) #great for splitting list dynamically
'''


##:Set for Finding Unique Items
'''
nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums) #removes duplicates instantly
print(unique_nums)'''


##:Swap Two Variables Without a Temp Variable
'''
a, b = 5, 10
a, b = b, a

print(a)
print(b)  #faster and cleaner than using a temporary variable'''


###:Pairing Elements from two lists
##:zip() creates key value pairs(dictionaries)
'''
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")'''


##:Unzipping Data into Separate Lists
'''
pairs = [("Alice", 85), ("Bob", 91), ("Henry", 78)]
names, scores = zip(*pairs)

print(names)
print(scores)'''


##:Creating a Dictionary from two lists
'''
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

#person = dict(keys, values)      #Error!__at most one argument
person = dict(zip(keys, values))  ##Work
print(person)
'''


##:Iterating Over Multiple Lists Together
'''
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = ["x", "y", "z"]

for a, b, c in zip(list1, list2, list3):
    print(a, b, c)
'''


##:Transposing a Matrix (Rows - Columns)
'''
matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
transposed = list(zip(*matrix))

print(transposed)
'''


##:Sorting Multiple Lists Together
'''
students = ["Alice", "Bob", "Henry"]
marks = [92, 85, 192]

sorted_data = sorted(zip(marks, students), reverse=True)
print(sorted_data)
'''


##:Number Formatting
'''
pi = 3.1415926535
large_number = 1234567890
print(f"Pi: {pi:3f}, Large Number: {large_number:,}")
'''


##:Dynamic Width Alignment
'''
name = "Bob"
score = 95
print(f"| {name:<10} | {score:^5} |")
'''

##:List Comprehensions
'''
nums = [x**2 for x in range(5)] #more concise than loops
print(nums)
'''


##:Join a List Into a String
'''
words = ["Python", "is", "fun"]
sentence = " ".join(words) #Avoids inefficient string concatenation
print(sentence)
'''


##:Use Enumerate Instead of Range(len())
'''
items = ['apple', 'banana', 'cherry']
for index, item in enumerate(items):
    print(index, item)
'''

###:Defaultdict from collections
##:Defaultdict makes it easy to handle missing keys in dictionaries by assigning a default value.
'''
from collections import defaultdict

count = defaultdict(int)
words = ['apple', 'banana', 'apple']

for word in words:
    count[word] += 1

print(count)
'''

###:F-Strings
##:Formatted strin literals
##{f-strings} make formatting strings easier and more readable than the traditional format() method.
'''name = 'Henry'
age = 18
print(f"My name is {name} and I'm {age} years old.")'''


###:Zip
##:Zip functions allows you to pair elements from multiple
##..iterables into tuples, which is useful for parallel iteration.
'''
names = ['Alice', 'Emma', 'Jane']
scores = [85, 90, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
'''

###:Set Operators
##:Sets are ideal for removing duplicates and performing
##..mathematical equations like Union, Intersection, and difference.
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 & set2) #Intersection - common numbers
print(set1 | set2) #Union - without repetition
'''

###:Enumerate
##:Instead of manually tracking indexes when looping, enumerate allows you to
##..access both the index and value of an iterable in a clean way.
'''
names = ['Alice', 'Bob', 'Henry']
for index, name in enumerate(names, start=1):
    print(index, name)
'''

###:Unpacking
##:Python's multiple assignment and unpacking features make variables assignments
##..cleaner, especially with tuples and lists.
'''
a, b = 5, 10
first, *middle, last = [1, 2, 3, 4, 5]
'''

###:List Comprehensions
##:List comprehensions offer a concise way to create lists. They're...
##..faster and more readable than traditional loops
#--Traditional way
'''
squares = []
for x in range(10):
    squares.append(x**2)

#--List comprehension
squares = [x**2 for x in range(10)]
'''

##:Lambda Functions for Short, Anonymous Functions
#:If you need a small function for a quick operation, use a lambda function
'''
multiply = lambda x, y: x * y
print(multiply(2, 3))
'''

##:Use Generators for Large Data Handling
#:When dealing with large datasets, use generators to save money.
'''
def count_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1
'''

###:Use importlib for Dynamic Imports
##:If you need import modules dynamically at runtime, use the importlib module:
'''
import importlib
my_module = importlib.import_module('module_name')
##..Useful when you don't know which module will be needed until runtime.
'''

###:Avoid `from module import *` to Prevent Namespace Pollution
##:Using wildcard imports (*) can cause name conflicts and make your code harder to
##..debug. It's better to explicitly import what you need.
'''
from math import sqrt
'''

##:Selective Imports to Save Memory
#:Instead of importing the entire module, selectively import only what you need to
#..optimize memory usage.
'''
from math import sqrt, pi
'''

###:Use all to Control Wildcard Imports
##:If you use module import *, you can specify which objects should be
##..imported using all in your module:
'''
_all_ = ['function1', 'Class2']
'''

###:Lazy Imports Inside Functions
##:To prevent unnecessary imports or resolve circular dependencies, import modules
##..inside functions.
'''
def my_function():
    import datetime
    return datetime.datetime.now()
'''


###:Import Multiple Modules in One Line
##:For small scripts or to keep imports tidy, import multiple modules on a single line.
'''
import os, sys, json
'''

###:Relative Imports for Better Package Management
##:In large projects, use relative imports to make code modular and avoid name clashes.
'''
from .subpackage import module
##..This is especially useful when you have well organized packages.
'''


###:Use Aliases to Shorten Module Names
##:When dealing with long module names, use aliases to shorten them for clearer code
'''
import numpy as np
import pandas as pd
##..This reduces repetitive typing and keeps your code more readable
'''


###:Secure Random Choice from a List
##:This program securely chooses a random item from a list
'''
import secrets

# List of items
items = ['apple', 'banana', 'cherry', 'date']

#Securely choose a random item
random_item = secrets.choice(items)
print(f"Random Chosen Item: {random_item}")
'''

##:...secure random integer
#:This program generate a secure random integer between two numbers.
'''
import secrets

# Generate a secure random integer between 1 and 100
random_init = secrets.randbelow(100) + 1
print(f"Secure Random Integer: {random_init}")
'''


##:...Generate a Secure URL-safe Token
#:This program generates a secure URL-safe token, which is useful for
#..generating things like secure reset links
'''
import secrets

# Generate a secure URL-safe token
url_safe_token = secrets.token_urlsafe(16)
print(f"URL-safe Token: {url_safe_token}")
'''


##:Generate a Secure Token
#:This program generates a secure random token.
'''
import secrets

# Generate a secure random token
token = secrets.token_hex(16)
print(f"Secure Token: {token}")
'''
