# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates with no issue
# set = {} unordered and immutable, but Add/Removes fine, can't duplicate
# tuple = () ordered and unchangeable/ Duplicates fine and faster than a list

# fruits = ["apple", "orange", "banana", "coconut", "kiwi", "pineapple", "tomato", "pomegranate", "mango", "melon", "papaya"]
# print(dir(fruits))
#^^ shows every attribute for a list

# print(help(fruits))
# ^^ gives you help for documentation

# rint(fruits[::-1])

#^^ [::2]gives every fruit but skips every second element

#[::-1] reverses the entire list

# for fruit in fruits:
   # print(fruit)
# print(len(fruits))

# print("apple" in fruits)
# print("cookies" in fruits)
## ^^ basic boolean statement

# fruits[0] = "pineapple"
# fruits[1] = "orange"
# fruits[2] = "banana"
# fruits[-1] = "papaya"
## ^^ changes values of these elements using indexing
# fruits.append("pineapple")
# fruits.append("apples")
# fruits.append("kiwi")
# ##^^appending adds to the end of the list
# fruits.remove("apple")
# ##removes specific items
# fruits.sort()
# ^ sorts the items alphabetically
# fruits.reverse()
#reverses list ^
# fruits.clear
#^ removes everything
# print(fruits.index("apple"))
# print(fruits)
# fruits.insert(0, "pineapple")
# #adding something into a spot and moving the rest over

# ##^puts everything in alphgabetical order

# cars = ["Ford", "Volvo", "BMW"]
#add 4 new cars
# cars.append("Nissan")
# cars.append("Volkswagen")
# cars.append("Subaru")
# cars.append("Jeep")
# #appends seem to be done separately, idk if they can be done in one line
# cars[-1] = "toyota"
# cars[2] = "Austin Martin"
# cars.insert(1, "mercedes")
# #select the spot you'll insert it in, then a comma, and then a string of what's going in
# cars.remove("Austin Martin")
# #make a print statement that lists the cars out that says "the lists of the cars in the list are: " 
# print (f"the cars on the list are:  {cars}")
# print("Ford" in cars)
### make an F string by putting an F right before "" without a space ###


# for car in cars:
#     requestCar = input("Enter a car: " )
#     cars.append(requestCar)
#     print(f'The cars in the list are: {cars}')
#     if len(cars) > 10:
#         print("you've reached the maximum number of cars")
#         break

#challenge
#create a friendlist
#add 4 friends
#replace the last friend with another
#replace the 3rd friend with another
#insert a new friend in the second location
# print out the list in an F-string
    # friends = ["Mendelson", "Phillips"]
    # for friend in friends: 
    #     friendRequest = input("Name a friend of yours: ")
    #     friends.append(friendRequest)
    #     print(f'your friends are:  {friends}')
    #     if len(friends) == 4:
    #         print("you've reached the max friend ammount, some other requests have been accepted however.")
    #     break
    # friends[-1] = "Castillo"
    # friends[2] = "Dowd"
    # friends.insert(2, "Silva")
    # print(f'your friends are currently {friends}')








##################sets##################
#sets are unordered and unindexed
# they are defined using curly brackets
#they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# print(fruits)
# print(dir(fruits)) #methods that can be used with sets
# print(help(fruits)) #documentation/methods that can be used with sets
# print(len(fruits))
# print("volvo" in fruits) #checks for an element
# print(fruits.add("Orange"))
# print(fruits.add("kiwi"))
# print(fruits)
# #add multiple elements
# print(fruits.update(["orange", "kiwi", "pineapple"]))
# print(fruits)
# #remove an element
# print(fruits.remove("banana"))
# print(fruits)
# print(fruits.pop()) #removes last element
# print(fruits)
# print(fruits.clear()) #clears the whole set
# print(fruits)


# social_security_numbers = {123456789, 987654321, 123466789}
# #remove last element in this set
# #add another social security number
# print(social_security_numbers.pop())
# print(social_security_numbers.add(123654987))
# print(social_security_numbers)
# social_security_numbers.add(123456789)
# print(social_security_numbers)

################tuples##############
#tupl;es are immutable and defined using parenthesis
#create a tuple called my_tuple with the following values:
#xample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2)) #counts how many times the entered value appears in the tuple
# # print(dir(example_tuple))
# # print(help(example_tuple))
# print(len(example_tuple))
# print(2 in example_tuple)
# #tuples are useful when storing values that shouldn't be changed such as the days of the week or the months of the year
# # if you want to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers peppers"
# #convert the string to a tuple
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# print(lymeric_tuple.count())


#loops with tuples
#for item in example_tuple: 
#    print(item)

###dictionary###
#dictionaries are unordered, changeable and indexable
#they are defined using curly bracketsd
#they have keys and values
# a colleciton of {key:value} pairs, no duplicates
#keys are unique
#values can be of any data type
capitals = {"Kenya": "Nairobi", 
            "Uganda": "Kampala", 
            "Tanzania": "Dodoma",
            "Rwanda": "Kigali", 
            "China":"Beijing",
            "USA": "Washington DC"}
print(capitals)
# print(dir(capitals)) #attributes that can be used with dictionaries
# print(help(capitals)) #documentation/methods that can vbe used with dictionaries
print(len(capitals))
print(capitals["Kenya"])
print(capitals.get("Kenya"))
#adding an item to the dictionary
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
#add three more countries and their capitals
capitals.update({"France":"Paris"})
capitals.update({"Brazil":"Rio de Janeiro"})
capitals.update({"Russia":"Moscow"})
print(capitals)
