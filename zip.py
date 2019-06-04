#You could unpack each tuple in a for loop like this.
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
#In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
#This would create the same letters and nums tuples we saw earlier.

#eg
#Convert list into dictionary.
some_list = [('d', 4), ('e', 5), ('f', 6)]
cast=[]
cast= dict(some_list)
print(cast)

#eg
#Quiz: Zip Coordinates
#Use zip to write a for loop that creates a string specifying the label and coordinates of each point
#and appends it to the list points. Each string should be formatted as label: x, y, z. 
#For example, the string for the first coordinate should be F: 23, 677, 4.

x_coords = [23, 53, 2, -12, 95, 103, 14, -5]
y_coords = [677, 233, 405, 433, 905, 376, 432, 445]
z_coords = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for label,x_coord,y_coord,z_coord in zip(labels,x_coords,y_coords,z_coords):
	points.append("{}: {}, {}, {}".format(label,x_coord,y_coord,z_coord))
for point in points:
	print(point)

#Quiz: Zip Lists to a Dictionary
#Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = []

for casts in zip(cast_names,cast_heights):
    cast = dict(zip(cast_names, cast_heights))
print(cast)

#Quiz: Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names, heights = zip(*cast)
print(names)
print(heights)

#Quiz: Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. 
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# replace with your code
print(type(data))
data_transpose = tuple(zip(*data))
print(data_transpose)