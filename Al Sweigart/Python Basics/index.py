# Learning with Al Sweigart - Automate the boring stuff with Python
"""
REPL, explained;
Read Evaluate Print Loop, this lets us run or execute Python instructions one at time and instantly shows it's output.

Basic Math Operators in Python
-Operator      -Operation                        -Example
 **            Exponent(raised to the power)     2 ** 3 = 8
 %             Modulus/Remainder                 22 % 8 i.e 2 rem 6 = 6
 //            Integer division/round up         22 // 8 = 2.75, 2.75 rounds up to 2
 /             Division                          22 / 8 = 2.75
 *             Multiplication                    3 * 5 = 15
 -             Subtraction                       5 - 2 = 3
 +             Addition                          5 + 5 = 10
"""
exponent = 8 ** 4
modulus = 13 % 2
round_up = 93 // 5
divide = 169 / 13
multiply = 12 * 12
subtract = 256 - 13
add = 101 + 102
# print(round_up)

"""
The order of Operations in python are called Precedence, think, BOD-MAS in Python, i.e, PED-MAS -in that order, the 
former taking precedence; The (**) is evaluated first, then (*), (/), (//), (%) operators are evaluated next; from left 
to the right. And the (+), (-) operators are evaluated last (also from left to right).

Parenthesis (), are used to override the order of things, operations in brackets (), are treated first, 
also from left to the right.

Whitespace in between values do not matter and are ignored in Python (except for indentation -starting on a new line),
but a single space is convention and is overlooked.
"""
# try1= 2 + 2
# try1 = 9   +   9
# print(try1)

"""
Integer, Floating-Points (Floats), and Sting Data Types
A data type is a category for values, and every value belongs to exactly one datatype.

Common Data Types
Integers (int) -2, -1, 0, 1, 2, 3, ....
floating-points (floats) -1.25, -1.0, -0.5, ...
Strings (str) "a", 'b', "c", 'D' 'Hello!'....

Strings are always surrounded in single or double quotes '', or ""; i.e, 
'Hello', "Good morning", so Python knows where the strings begins and ends,
(' ', or " ") are called empty strings.
"""
greetings = "Hello cruel world"
regards = 'Wish you the very same'
empty = " "
# print()

"""
String Concatenation and Replication
(+) sign is a mathematical operator that sums two or more values of integer types;
However, (+) sign is also used for concatenating or joining strings.
"""
friend1 = 'Middleman'
friend2 = "Miles"
friends = friend1 + friend2 # 'Middleman' + "Miles"
# print(friends)

"""
The (*) operator, when used on one string value and one integer value, it becomes the string replication operator.
"""
friend3 = 'Angel' * 5
# print(friend3)














