############ Assignment 7 #########
## Think of at least three kinds of your favorite rice, store three rice names in a list,
# and use loop to print the name of each rice.
favorite_Rice = ["foreign rice", "pepper rice", "local rice"]
for rice in favorite_Rice:
    print(rice)

### Print a sentence using the name of the rice,
## for each rice you should have one line of output containing a simple statement like;
# "I like pepper rice..."
for tee in favorite_Rice:
    print(f"I like {tee.title()} !")

###Add a line at the end of your program, outside the for loop,
##an additional sentence, such as I really love eating rice!
print("\nI like eating rice!!!")