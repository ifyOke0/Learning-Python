############ ASSIGNMENT 2 #############
##You are having a party, make a list of three people you would like to invite
invited_Friends = ["Miles", "Chubby", "Lemar"]
print(invited_Friends)

##One of them can't make it, Print a message stating the name of the person that can't
cant_makeIt = invited_Friends.pop(1)
print(f"\nSorry guys!, Unfortunately {cant_makeIt} couldn't make it to the party.")

##Replace the name of the one, who can't make it with the one who can make it
invited_Friends.insert(1, "Henry")
print(invited_Friends)

##You found a bigger hall!, Print a message informing current guests
gen_Message = "\nHello y'all!"
gen_Message += f"\nSup {invited_Friends[0]}, What's up {invited_Friends[1]}, {invited_Friends[2]}"
gen_Message += "\nThe party will take place at a newly allocated hall, more info's later.\n"
print(gen_Message)

##Add three more guests, one at the beggining[0], middle[?], and end of your list
invited_Friends.insert(0, "Maxwell")  #Beginning
invited_Friends.insert(2, "Thomas")   #Middle
invited_Friends.insert(5, "Joseph")    #End
print(invited_Friends)

##The event planner failed with getting the bigger hall,
#use pop() method to remove three guests, each time inform him/her of their exclusion

guest1 = invited_Friends.pop(0) #First Uninvited Guest
print(f"\nDear {guest1}, I was unable to allocate a hall as intended, you've sadly been uninvited.")

guest2 = invited_Friends.pop(1) #Second Uninvited Guest
print(f"Dear {guest2}, I was unable to allocate a hall as intended, you've sadly been uninvited.")

guest3 = invited_Friends.pop(3) #Third Uninvited Guest
print(f"Dear {guest3}, I was unable to allocate a hall as intended, you've sadly been uninvited.\n")

##Print a message to the remaining three informing them they're still invited
print(invited_Friends)
print(f"\nHey {invited_Friends[0]}, What's up {invited_Friends[1]}, Sup {invited_Friends[2]}, Ok Guys!, Party at my place 🥳🤘🏾")

##After the Party use del to remove the last three names so you have an empty list
#del invited_Friends[:] #or
invited_Friends.clear()
print(invited_Friends) ##### DONE 🔥🔥🔥🔥
