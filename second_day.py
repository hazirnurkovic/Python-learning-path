#create an empty tuple
empty_tuple = ()

#create a tuple containing names of your sisters and your brothers (imaginary siblings)
sisters = ('Sister1', 'Sister2', 'Sister3')
brothers = ('Brother1', 'Brother2', 'Brother3')

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#How many siblings do you have?
print('I have', len(siblings), 'siblings')

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Father', 'Mother')
print(family_members)

#Unpack siblings and parents from family_members
    #(sister1, sister2, sister3, brother1, brother2, brother3, *parents) = family_members
    #print(sister1, sister2, sister3, brother1, brother2, brother3, parents)
siblings = family_members[:6]
parents = family_members[6:]
print("Siblings: ", siblings, "\nParents: ", parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Orange', 'Banana')
vegetables = ('Carrot', 'Cabbage', 'Spinach')
animal_products = ('Meat', 'Eggs', 'Milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_lt) // 2
print(food_stuff_tp[middle])

#Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three, last_three)

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
