# Write a small script that converts minutes to seconds, or hours to minutes.

ask = input("Do you want to convert minutes(min)\nor hours(hrs)? ")

if ask == "min" or ask == "minutes":
    minutes = int(input("Convert minutes to seconds(sec): "))
    print(str(minutes) + " Minutes to seconds is: " + str(int(minutes * 60)) + " seconds.")
elif ask == "hrs" or ask == "hours":
    hours = int(input("Convert hours(hrs) to minutes(min): "))
    print(str(hours) + " hours to minutes is: " + str(int(hours * 60)) + " minutes.")
else:
    print("Put in an adequate time format, min or hrs! and try again.")
