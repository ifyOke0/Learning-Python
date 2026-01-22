# Ask the user for a username and password
# Allow only 3 attempts
# If the credentials are correct, print a success message and exit
# if the user fails 3 times, lock them out.

# GO!!

defaultUser = "Itadori"
defaultPass = "itaJJK_0"
print("Welcome User, Please Answer the following")

tries = 0
while tries < 3:
    query1 = input("Type in your username: ")
    query2 = input("Enter Password: ")

    tries += 1

    if query1 == defaultUser and query2 == defaultPass:
        print(f"Welcome {query1}!")
        break
    elif query1 == defaultUser and query2 != defaultPass:
        print(f"Invalid Password, {tries} attempt, {3 - tries} left.")
    elif query1 != defaultUser and query2 == defaultPass:
        print(f"Incorrect Username, {tries} attempt, {3 - tries} left.")
    elif query1 != defaultUser and query2 != defaultPass:
        print(f"Wrong credentials, {tries} attempt, {3 - tries} left.")
else:
    print("Out of Attempts")
