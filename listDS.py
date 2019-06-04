#list

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])
print(list_of_random_things[len(list_of_random_things) - 1])
print(list_of_random_things[-1])
print(list_of_random_things[-2])
list_of_random_things[2]='replace'
print(list_of_random_things)

#list_of_random_things[len(list_of_random_things)] will give an error of out of range.


#Slice and Dice with Lists
print(list_of_random_things[1:2])
print(list_of_random_things[:2])
print(list_of_random_things[1:])
