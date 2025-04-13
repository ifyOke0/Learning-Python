################## ASSIGNMENT!!!!!  ################
##Store the names of your friends [5] in a list
##Print a message to them, personalising the messages

friends = ['Miles', 'Destiny', 'Daniel', 'Esther', 'Peter']
tag = [15, 22, 19, 100, 12]

to_Miles = f"Hello {friends[0]}, my birthday is on the {tag[0]}th of January!"
print(to_Miles)

to_Destiny = f"Guten Tag {friends[1]}, kommst du gleich in {tag[1]} Minuten nach Hause?"
print(to_Destiny)

to_Daniel = f"Happy birthday {friends[2]}!, you're turning {tag[2]} today."
print(to_Daniel)

to_Esther = f"Hey {friends[3]} please count to {tag[3]} (a hundred)"
print(to_Esther)

to_Peter = f"Good Morning Mr; {friends[-1]}, the meeting doesn't start until {tag[-1]} o'clock today."
print(to_Peter)
