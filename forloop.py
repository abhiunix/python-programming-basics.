#forLoop
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

#Using the range() Function with for Loops
for i in range(3):
    print("Hello!")

#range(start=0, stop, step=1)
#Creating and Modifying Lists
#In addition to extracting information from lists, as we did in the first example above, 
#you can also create and modify lists with for loops. 
#You can create a list by appending to a new list at each iteration of the for loop like this:

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())


#Modifying a list is a bit more involved, and requires the use of the range() function.
#We can use the range() function to generate the indices for each value in the cities list. 
#This lets us access the elements of the list with cities[index] so that we can modify the values in the cities list in place.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()