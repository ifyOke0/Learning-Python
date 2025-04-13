############ ASSIGNMENT 9 ############
##Store five countries you want to visit in a list -- make sure its not in alphabetical order, and print it
countries = ["Germany", "South africa", "America (USA)", "Egypt", "Italy"]
print(countries)

##Print the list in an alphabetical order
# -- print it in the original form again
for key in sorted(countries):
    print(key)  #Alphabetical Order
# print(sorted(countries)) #or

print(countries) #Original Order

##Print the list in reverse
# -- print it in the original form again
countries.reverse()
print(countries)  #In Reverse

countries.reverse()
print(countries) #Original Form

##Use len() and make a statement
#--indicating the number of countries you would like to visit
country_number = str(len(countries))
print(f"\nI would like to visit {country_number} countries.")