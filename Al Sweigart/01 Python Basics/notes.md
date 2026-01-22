# Learning with Al Sweigart - Automate the boring stuff with Python
REPL, explained;
Read Evaluate Print Loop, this lets us run or execute Python instructions one at time and instantly shows it's output.

### Basic Math Operators in Python 

| Operator |           Operation           |               Example               |
|:---------|:-----------------------------:|:-----------------------------------:|
| **       | Exponent(raised to the power) |             2 ** 3 = 8              |
| %        |       Modulus/Remainder       |       22 % 8 i.e 2 rem 6 = 6        |            
| //       |   Integer division/round up   | 22 // 8 = 2.75, 2.75 rounds up to 2 |
| /        |           Division            |            22 / 8 = 2.75            |                       
| *        |        Multiplication         |             3 * 5 = 15              |                         
| -        |          Subtraction          |              5 - 2 = 3              |                           
| +        |           Addition            |             5 + 5 = 10              |                          

```py
exponent = 8 ** 4
modulus = 13 % 2
round_up = 93 // 5
divide = 169 / 13
multiply = 12 * 12
subtract = 256 - 13
add = 101 + 102
# print(round_up)
```

The order of Operations in python are called **Precedence**, think, **BODMAS** in Python, __i.e__, **PEDMAS**, in that order, the 
former taking precedence; The __(**)__ is evaluated first, then __(*)__, __(/)__, __(//)__, __(%)__ operators are evaluated next; from left 
to the right. And the __(+)__, __(-)__ operators are evaluated last _(also from left to right)_.

**Parenthesis ()**, are used to override the order of things, operations in brackets __()__, are treated first, 
_also from left to the right_.

Whitespace in between values do not matter and are ignored in Python **_(except for indentation -starting on a new line)_**,
but a single space is convention and is overlooked.

```py
try1= 2 + 2
try1 = 9   +   9
print(try1)
```

### Integer, **Floating-Points _(Floats)_**, and String Data Types
A data type is a category for values, and every value belongs to exactly one datatype.

### Common Data Types
**Integers _(int)_** -2, -1, 0, 1, 2, 3, .... <br>
**floating-points _(floats)_** -1.25, -1.0, -0.5, ... <br>
**Strings _(str)_** "a", 'b', "c", 'D' 'Hello!'....

Strings are always surrounded in single or double quotes __('')__, or __("")__; **_i.e_**, 
`'Hello'`, `"Good morning"`, so Python knows where the strings begin and ends, `(' ', or " ")` are called empty strings.

```py
greetings = "Hello cruel world"
regards = 'Wish you the very same'
empty = " "
print(empty)
```

### String Concatenation and Replication
__(+)__ sign is a mathematical operator that sums two or more values of integer types;
**However**, **_(+)_** sign is also used for **concatenating** or **joining** strings.

```py
friend1 = 'Middleman'
friend2 = "Miles"
friends = friend1 + friend2  # 'Middleman' + "Miles"
print(friends)
```
The __(*)__ operator, when used on one string value and one integer value, it becomes the string replication operator.

```py
friend3 = 'Angel' * 5
print(friend3)
```

### Storing values in variables

A **variable** is like a _box_, this lets us store a single value.
**Assignments** __(=)__; assigns a value of any known datatype to a variable.

```py
light_yrs = 40
print(light_yrs)

nummer = 2
print(nummer)
print(light_yrs + nummer + light_yrs)

nummer = nummer + 10
print(nummer)
```

A variable is created when a value is stored or assigned to it.
After that, the variable name can be called as their expressions or by name with other variables and values. When a variable is assigned a new value, the old value is forgotten.

```py
nummer = 2
print(nummer)
nummer = nummer + 10
print(nummer)
```

### Variable Names

An ideal Variable name describes the data it contains. One can name a variable
almost anything, under certain rules ofcourse; Python have some restrictions when it
comes to name variables. A good Variable in Python follows these rules;

__one word no spaces__ (eg; variable name | variableName) <br>
use only letters, numbers and the underscore(_) character no hyphens(-). <br>
variables names can't begin with a number (eg; 15boxes | box15)

Variable names are _case-sensitive_, in the sense that _box_, **BOX**, `Box`, _`bOX`_, are
different variables. It is a Python convention to start variables with lowercase
letters. __(eg; Find = 'works ✅' but find = "is preferred")__.

**camelCasing** or **under_score** as variable naming styles are advised.


**When there are no more lines of code to execute, the Python program terminates, and stops running.
When a Python file is ran, it starts from the top, working it's way down, executes the inputted commands
until the last line, then the Python program exits.**

### Comments
```py
# This entire area is commented and won't be executed when ran.
```
Python ignores comments, and can be used to leave notes or to explain what a particular line of code does to others.

```py
# (#) for single line comments

"""
for multiple lines
for multiple lines
for multiple lines
"""

```

### Print() Function
The `print()` function displays the string value inside it's parenthesis on the screen when you run the code.

```py
print('Hello, treacherous world!')
print('How many fingers am I holding up?')  # Then run
```

### Input() Function
The `input()` function waits for the user to type some text on the keyboard and press
**ENTER**. Here the function asks for a particular datatype, Strings **_(str)_** most times; and
you can fill it in directly in the terminal.

```py
myOtherName = input("What is your name? ")  # Stores value to the variable 'myOtherName
print('Your name is ' + myOtherName)
'''
NOTE!!! input() functions are only available in versions of Python3, may not work if running Python2
'''
```

### Len() Function
The `len()` function, you can pass in a string value **(or a variable containing string)**,
and the function evaluates to the integer value of the total number of characters
**(letters)** in that string.

```py
frankOceanSaid = 'I can never make him love me'
print(len(frankOceanSaid))
'''
print() : shows us the output, len(), counts and gives the number of characters
'''
```

### Integer + String concatenation errors

```py
# print('I am ' + 29 + 'years old') # 29 is an integer(int), can only concatenate strings(str).
```

Python gives an **~~error~~** cuz' the __(+)__ operator can only be used to add two integers
together or concatenate two strings. You can't add an integer to a string, doesn't
follow Pythons grammar rules. One can alter the code to print **_integers(int)_** as
**_stings(str)_**.

### The `str()`, `int()`, and `float()` Functions
___str()___ : this converts to the string version of the integer within <br>
__int()__ : also useful for rounding down a floating-point(floats) number

```py
num = 33
print('I am ' + str(num) + 'years old')

str(-3.14)  # Python sees a string, equivalent to 'A', and can't be calculated
str(0)
int('42')
int('-99')
int(7.7) # clearly a float datatype, outputs 7.7 ".7 is > .5", rounds down to 8.
float('3.14')
float(10) # turns to 10.0
```

### Text and number equivalence
An integer can be equal to a floating point number

44 == '44' :False, '44', is a string <br>
44 == 44.0 :True, integers(int) rounds down to 44 <br>
44.0 == 0044.000 :True, ignores the zero's before 44, they are insignificant

Integers and floats are mathematically numbers.


## FIRST PROGRAM
#### This program says hello and asks for users name.
```py
print('Hello, cruel world!')
print('What is your name?')

myName = input()
print('It is good to meet you, ' + myName)

print('The length of my name has got to be: ')
print(len(myName))

print('How old are you?')
myAge = input()
print('I will be ' + str(int(myAge) + 1) + ' in a year!')
```

[next >>>](../02%20Flow%20Control/01%20notes.md)