# Cont'd, Flow Control
This analogy stuck; "Based on how expressions evaluate, a program can decide to skip instructions, repeat them, or choose one of several instructions to run".

### Flowcharts
A flowchart is a **visual diagram** that represents the steps of a process or algorithm in sequential order. Thought out steps one goes through to see a task is done. It involves the use of shapes and arrows to show information or actions flow from one point to another.

Each flowchart has a meaning:

- **Oval (ellipse)**: Start or end of a process
- **Rectangle**: A process or operation (what you want done, like "Add two numbers")
- **Diamond**: A decision point (yes/no, true/false)
- **Parallelograms**: Input or output (like "Enter value" or "Display result")
- **Arrows**: Shows the direction of flow

Flow control statements can decide which Python instructions to execute under which conditions.

![Flowchart-example-image](/assets/flowchartEG.png "Shows a decision-making process")
In a flowchart, there is usually more than one way to go from start to end. Same goes for lines of _(python)_ codes.

### Boolean Values
The _Boolean_ data tyoe has only two values, `True` and `False`. (_Boolean_ valeus starts with capital letters, and are named after mathematician __George Boole__). _Boolean_ values can be stored in variables and can be used in expressions.

```python
henryScore = 99
middleManScore = 101

result = middleManScore < henryScore 
print(result)  #False
```
### Comparison Operators
_Comparison Operators_, also called relational operators, compare two values and evaluate down to a single _Boolean_ value.

| Operator | Meaning                  |
|:---------|:-------------------------|
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| ">"      | Greater than             |
| <=       | Less thn or equal to     |
| ">="     | Greater than or equal to |

These operators evaluate to `True` or `False` depending on the values you give them. `==` (equals to) evaluates to `True` when the values on both sides are the same, and `!=` (not equal to) evaluates to `True` when the two values are different. The == and the != operators can work with values of any data types. 

```python
firstRating = 100
secondRating = 100

print(secondRating == firstRating)  #True

secondRating = 99
print(secondRating == firstRating)  #False

print(secondRating != firstRating)  #True

print('hello' == "hello")  #True  :despite double quotes
print('hello' == "Hello")  #False :different casing

print('dog' != 'cat')  #False :not equal
print(True != False)   #True  :not equal

print(42 == 42.0)      #True
print(42 == '42')      #False : 42 is an integer, '42' a string

# The <, >, <=, and >= operators, on the other hand, 
# work properly only with integer and floating-point values.

print(42 < 100)  #True  :less than 100
print(42 > 100)  #False :less than 100
print(42 < 42)   #False :Both are equal

headCount = 42
print(headCount <= 42)  #True :not less than, but equal to 42

hisAge = 30
print(hisAge >= 10)     #True :not equal to, but greater than 10
```

### The Difference Between The `==` And `=` Operators
The double equals sign `==` is different from the normal equal sign `=`, it's easy to confuse them for the other.

- The `==` operator (equal to) asks whether two values are the same as each other.
- The `=` operator (also known as the assignment operator) puts the value on the right into the variable on the left.

### _Boolean_ Operators
The three _Boolean_ operators (and, or, and not) are used to compare _Boolean values. Like the comparison operators, they evaluate these expressions down to a _Boolean_ value.

#### Binary _Boolean_ Operators
The `and` and `or` operators always take two _Boolean_ values (or expressions), so they're considered _binary_ operators.
`and` operator evaluates an expression to `True` if **both** _Boolean_ values are `True`; otherwise, it evaluates to `False`.

```python
try1 = 'name'
try2 = 'Name'
# try1 and try2  >>>> False

"""
True and True  >>>> True
True and False >>>> False
"""
```

#### Truth Table
A _truth table_ shows every possible result of a _Boolean_ operator. In binary `True - 1` and `False - 0`.

<h6>The `and` Operator's Truth Table</h6>

| Expression | Evaluates to... |
|------------|:---------------:|
| 1 `and` 1  |        1        |
| 1 `and` 0  |        0        |
| 0 `and` 1  |        0        |
| 0 `and` 0  |        0        |

`or` operator evaluates an expression to `True` if **either** of the two _Boolean_ values is `True`. If they are both `False`, it evaluates to `False`.

```python
"""
False  or True  >>>> True
False or False >>>> False
"""
```

<h6>The `or` Operator's Truth Table</h6>

| Expression | Evaluates to... |
|------------|:---------------:|
| 1 `or` 1   |        1        |
| 1 `or` 0   |        1        |
| 0 `or` 1   |        1        |
| 0 `or` 0   |        0        |

`not` operator operates on only one _Boolean_ value (or expression). This makes it a unary operator. The `not` operator simply outputs the opposite _Boolean_ value.

```python
"""
not True >>>> False
not not not not True  >>>> True :false-true-false-true - True
"""
```

<h6>The `not` Operator's Truth Table</h6>

| Expression | Evaluates to... |
|------------|:---------------:|
| `not` 1    |        0        |
| `not` 0    |        1        |


### Mixing _Boolean_ and Comparison Operators
`NB:` The `and`, `or`, and `not` operators are called _boolean operators because they always operate on the _Boolean_ values `True` and `False`. Expressions like `4 < 5` are not _Boolean_ values, they are expressions that evaluate down to _Boolean_ values, i.e `(True` and `False)`.

```python
print((4 < 5) and (5 < 6))   #True
print((4 < 5) and (9 < 6))   #False
print((1 == 2) or (2 == 2))  #True

"""
You can also use multiple Boolean operators in an expression, 
along with the comparison operators. 
"""
print((2 + 2) == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
#      True        and not   False    and True
#      True        and True           and True
# True
```
`NB:` Like the math operators, Python have an order of operations. Python evaluates the `not` operators, and then `or` operators.

### Elements of Flow Control
Flow control statements often start with a part called the **condition** and are always followed by a block of code called the clause.

#### Conditions
Conditions always evaluate down to a _Boolean_ value, `True` or `False`. A flow control statement decides what to do based on whether its condition is `True` or `False`.

#### Blocks of Code
Lines of *Python* code can be grouped together in **blocks**. The indentations (paragraphs, starting on a new line and tab spaces) tell when a block begins and ends. There are three (3) rules for blocks.

- Blocks begin when the indentation increases.
- Blocks can contain other blocks
- Blocks end when the indentation decreases to zero or to a containing block's indentation.

```python
# Let's understand indented code

# age = 10
# password = 'nemo'
age = int(input("How old are you? "))
password = input("What's the password? ")

if age == 10:
    print("10 fishes")
    if password == 'nemo':
        print("Access granted")
    else:
        print("Wrong password")
```
