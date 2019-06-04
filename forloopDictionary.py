#forLoop in Dictionary.
#Iterating Through Dictionaries with For Loops
#When you iterate through a dictionary using a for loop, doing it the normal way (for n in some_dict) 
#will only give you access to the keys in the dictionary - which is what you'd want in some 
#situations. In other cases, you'd want to iterate through both the keys and values in the dictionary. 
#Let's see how this is done in an example. Consider this dictionary that uses names of actors as keys 
#and their characters as values.

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for key in cast:
    print(key)

#Iterating through it in the usual way with a for loop would give you just the keys.
#If you wish to iterate through both keys and values, you can use the built-in method items like this:
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

#items is an awesome method that returns tuples of key, value pairs, 
#which you can use to iterate over dictionaries in for loops.

#Quiz: Fruit Basket - Task 1
#You would like to count the number of fruits in your basket. In order to do this, you have 
#the following dictionary and list of fruits. Use the dictionary and list to count the total number of 
#fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary.

#Iterate through the dictionary
for fruit, count in basket_items.items():
	if fruit in fruits:
		result+=count
#if the key is in the list of fruits, add the value (number of fruits) to result
print(result)


#eg2
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count

for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} items that are not fruits.".format(fruit_count, not_fruit_count))
