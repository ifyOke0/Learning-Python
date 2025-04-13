########## ASSIGNMENT 6 ###########
## Store 7 names of any state in your country in alist
my_States = ["Anambra", "Bauchi", "Cross-river", "Delta", "Edo"]

##Print the message; The first three states in the list are...,
# Then use slice to print the first three states
print("The first three states in the list are...")
for i in my_States[0:3]:
    print(i)

##..also the three states from the middle of the list
#--and also the last three states in the list
print("\nThe three states in the middle of the list are...")  #three from the middle
for hey in my_States[1:4]:
    print(hey)

print("\nThe last three states in the list are...")    #Last three
for x in my_States[-3:]:
    print(x)

