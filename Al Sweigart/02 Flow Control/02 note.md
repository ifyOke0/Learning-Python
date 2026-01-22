# Cont'd Flow Control

### Current Program
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

##### Program Execution
Executing this current instructions, notice how Python starts from the top, working it's way down towards the last line. Python be like, run the variable `age`, and the variable `password`, then the following indented codes (blocks). Starting from the first `if` statement *(see how it's further to the left, think of it like the container for whatever **indented or spaced out** logic that comes after it)*, then the `print`, the new `if` block, **with it's `print` command and it's `else` condition**.<br>

If you run this little script, you'd probably observer how python didn't throw errors for submitting values other than the ones instructed; unless you submitted values of different data types, i.e, letters _(string)_ for the variable `age`, whereas asks for _int_ values. Even if you input in a number other than `"10"`, Python quits the program, cuz the rest of the code execution relies heavily on the `age` variable being equal to `"10"`. And, in cases when you submit the wrong password, you'll get the already defined response.

```txt
You can try putting an `else` condition on the container, i.e, the `if` statement. Let it print a response for when a number other than "10" is submitted.
(note: the `else` condition for the container, must start, alligned to the left side, just as the container `if`, not as the indented or spaced out ones)
```
#### Executed.
[Back to previous](01%20notes.md)