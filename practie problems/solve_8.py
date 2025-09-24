####### ASSIGNMENT 8 ########
##Make the list of phones
#--and make a copy of the list of the phones and call it my friend's phones
phones = ["Tecno", "Infinix", "Oppo", "Xiaomi"]
print(phones)

friends_Phones = phones[:]
print(friends_Phones)

##Add a new phone to the original list--also add a new phone to the friend's list
phones.insert(0, "Samsung")

friends_Phones.append("Iphone")

##Prove that you have two separate lists and print a message with the separate lists
print(phones)
print(friends_Phones)
