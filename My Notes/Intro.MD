### Intro to Python

```py
print("This is Henry, Henry is speaking")
print('Python is very fun')
```

### Variables and Values

```py
our_message = 'Hallo, Ich heise Henry, und du?'
print(our_message)

a,b,c = 1,2,3
print(a)
print(b)
print(c)
```

### Variable Formatting

```py
name = "emmanuel"
print(name.title())
print(name.upper())
print(name.lower())
```

### Striping White Space

```py
meiene_Sprache = '   Python'
print(meiene_Sprache)
print(meiene_Sprache.lstrip())
print(meiene_Sprache.rstrip())
print(meiene_Sprache.strip())
```

### Avoiding syntax error with strings

```py
# python_message = 'One of Python's strength is it's diverse community.'
# print(python_message) #Error

python_message = "One of Python's_strength is its_diverse_community._"
print(python_message) correct
```

### Concatenate

```py
vorName = "Henry"
nachName = "Okeke"
alt = "18"
vollName = vorName +" "+ nachName

print("Mein Vorname is " + vorName)
print("Mein Nachname is " + nachName)
print("Meine Alter is " + alt)
print("Mein Name in voll is " + vollName)
```

### Avoiding Type Errors With STR() Function

```py
alt = 18
student_Nachrischten = "Glucklishes " + str(alt) + "ste geburstag, Henry"
print(student_Nachrischten)
```

### Lists

```py
authors = ['Shakespeare', 'Achebe', 'King Arthur', 'Osamu Dazia']
print(authors)
print(authors[2])
print(authors[-1])

# Using Individual Values From a list
nachrischten = authors[-1] + "'s No Longer Human, has got to be my favorite book, Ever"
print(nachrischten)
```

### Modifying Elements in a list

```py
auto = ["BMW", "camery", "Honda", "Audi"]
print(auto)

auto[1] = "Lexus"
print(auto)
```

### Adding Elements to lists, List-Appending

```py
gods = ["Poseidon", "Aphrodite", "Athens", "Zeus"]
print(gods)

gods.append("Thor")
print(gods)
```

### Inserting Elements to Lists `.insert([index], "_object")`

```py
element = ["Poseidon", "Aphrodite", "Athens", "Zeus"]
print(element)
element.insert(2, "Apollo")
print(element)
```

### Removing from Lists Using Del

```py
modules = ["Poseidon", "Aphrodite", "Athens", "Zeus"]
print(modules)
del modules[0]
print(modules)
```

### Removing an Element Using `pop()`

```py
titans = ["Poseidon", "Aphrodite", "Athens", "Zeus"]
print(titans)
titans.pop()
print(titans)

popped_Titans = titans.pop()
print(titans)
print(popped_Titans)

phones = ["samsung", "motorola", "nubia" "pixel", "xiaomi"]
current_used = phones.pop()
print("My current Phone is a " + current_used.title() + " Redmi note 20 5g")

first_used = phones.pop(0)
print("My first ever Phone was a " + first_used.title() + " galaxy S10")
```

### Removing an Item by `value(name)`

```py
rulers = ["Poseidon", "Aphrodite", "Athens", "Zeus"]
print(rulers)
rulers.remove("Zeus")
print(rulers)

powerful = "Zeus"
rulers.remove(powerful)
print(rulers)
```

### Conditional Logic `(if-elif-else)` Intro, Indentation & Short Circuiting

```py
if(6 > 11):
    print("true")
else:
    print("false")

# BOOLEAN
is_licenced = False
good_vision = True

if is_licenced or good_vision:
  print("You can drive!")
else:
  print("You can't drive!")

# IF Statement
alt = 20
if alt  >= 18:
  print("You can now vote!")
  print("Go now to the INEC Office to register")

# IF-ELSE Statement
age = 17
if age  >= 18:
  print("You are old enough to vote")
  print("Have you been registered?")
else:
  print('Sorry, you are too young to vote')
  print("Please, register to vote as soon as you turn eighteen (18)")

print("Thank you.")


# IF-ELIF-ELSE Statement
age = 17
if age < 4:
  print("You get a free admission to the donations list")
elif age <= 17:
  print("Your admission cost is $5")
else:
  print("Your admission cost is $10")
```

### TESTING MULTIPLE CONDITIONS

```py
requested_toppings = ["mushroom", "pickles", "extra cheese"]

if 'pickles' in requested_toppings:
  print("....adding pickles")
if 'ketchup' in requested_toppings:
  print("...adding ketchup")
if 'mushroom' in requested_toppings:
  print("...adding mushroom")
print("\n Finished making pizza")
```

### LOOPS

```py
cars = ['royce', 'honda', 'BMW']
for i in cars:
  print(i)

for latter in "Apocalypto is awesome!!":
  print(latter)


# Nested Loops
for crabs in (1,2,3,4,5):
  for henry in ['a', 'b', 'c']:
    print(crabs, henry)

# While Loop
i = 0
while i <= 10:
  print(i)
  i += 1

while True:
  response = input("What's my name: ")
  if(response == 'Henry' or response == 'henry'):
    print("CORRECT!")
    break
  elif(response != 'Henry'):
    print("INCORRECT!!")
```

### USER INPUT

```py
message = input("Tell us your name: ")
print(message)

name = input("What's your name: ")
print("Hello " + Name + "!")

customer = "When you shop from us, you get a discount."
customer += "\nWhat's your name? "

name = input(customer)
print("\nThanks for shopping with us " + name + ", your discount is 50%.")
```

### DATA TYPES

`#int`
`#float`
`#bool (for boolean)`
`#tuple`
`#dict`
`#str`
`#list`
`#set`

### Integers and float

```py
paris = 5 - 2
print(paris)

number = 3 * (3 + 2)
print(number)

print(type(2 + 2))
print(type(2 / 4))

print(2 ** 3)
print(10 % 3)
```

### MATH FUNCTIONS

```py
#Round
print(round(3.9)) #nearest whole-number
print(abs(-20))

# Operator Presence (), **, /, *, +, -  ...PEDMAS
print(2 + 3 * 4)
print((20 - 3) + 2 ** 3)
```

### EXPRESSION VS STATEMENT

```py
denmark = 100       #Expression !_Declaring a value to a variable creates an expression
user = denmark / 5  #Statement !_Performing tasks with known variables creates a statement
print(user)
```

### AUGMENTED ASSIGNMENT OPERATOR

```py
super = 20
super = super + 10
super += 10
print(super)

# STRINGS
#print("Hello, and welcome")

long = '''
key
car
jaw
mouth
water
cable
fiend
friend
foe
'''
print(long)

first_name = "Henry "
middle_name = "Ifeanyi "
last_name = "Okeke "
full_name = first_name + middle_name + last_name
print("My names are " + full_name)
print("My names are " + full_name.upper())
print(f"My names are {full_name.upper()}")
```

### WORKING WITH PART OF A STRING\_\_\_slicing

```py
amazon_cart = ["Jacket", "tennis", "beanies"]
print(amazon_cart)

amazon_cart[0] = "Cars"
print(amazon_cart)

players = ["Natalie", "Jane", "Angel", "Calis", "Crystal"]
print(players[:4])

players = ["Natalie", "Jane", "Angel", "Calis", "Crystal"]
print(players[1:4])

players = ["Natalie", "Jane", "Angel", "Calis", "Crystal"]
print(players[2:])

players = ["Natalie", "Jane", "Angel", "Calis", "Crystal"]
print(players[-3:])
```

### LOOPING THROUGH A SLICE

```py
team = ["Natalie", "Jane", "Angel", "Calis", "Crystal"]
print("Here are my first three players;")
for AI in team[0:3]:
  print(AI + " You're chosen")
```

### COPYING A LIST

```py
my_foods = ['pizza', 'rice', 'noodles']
friends_foods = my_foods[:]

print("My favorite foods are;")
print(my_foods)

print("My friends favorite foods are;")
print(friends_foods)

my_foods.append("Beans")
friends_foods.append("Yam")

print(my_foods)
print(friends_foods)
```

### ORGANIZING A LIST --- SORTING A LIST

```py
cars = ["bmw", "audi", "toyota",  "subaru"]
cars.sort()
print(cars)
cars.sort(reverse=False)  #either true or false
print(cars)

# SORTING A LIST TEMPORARILY
cars = ["bmw", "audi", "toyota",  "subaru"]
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)
```

```py
# FINDING LENGTH FROM A LIST
auto = ["bmw", "audi", "toyota",  "subaru", "benz", "volkswagen"]
print(len(auto))

# UNPACKING A LIST
a,b,c,d, *safe, e = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(safe)
print(e)


student_that_paid = ["henry", 'michelle', 'chloe', 'alex', 'chloe']
print('chloe' in student_that_paid)

# ESCAPE CHARACTER
rain = 'it\'s raining heavily'
print(rain)

weather = "it's \"almost\" raining."
print(weather)
```
