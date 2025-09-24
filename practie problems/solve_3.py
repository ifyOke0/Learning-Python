################## ASSIGNMENT 3 ########################
#Imagine a soldier that was shot down in a game,
#create a variable called soldier_color and assign it a value of green,yellow or red
soldier_Color = input("Guess soldier's color(Red-Green-Blue): ")
score = 0
##Write an if-Statement to test whether the soldier's color is green,
# if it is, print a message that the player just earned 5 points
if(soldier_Color == 'Green' or soldier_Color == 'green'):
    score += 5
    print(f"Winner!, You've Earned {score} Points.")

###Choose Another Color, and write the program below using if-else chain
secondSoldier_Color = input("Enter second soldier's color(Red-Green-Blue): ")

#If the soldier's color is the chosen color, print a statement that the player just earned 10 points.
##If the soldier's color isn't the color, print a statement that the player just earned 15 points
if(secondSoldier_Color == 'Red' or secondSoldier_Color == 'red'):
    score += 10
    print(f"Winner!, You've Earned {score} Points.")
else:
    score = 0
    print(f"Wrong Color!, You've Earned {score} Points")

print("\nWell-done")