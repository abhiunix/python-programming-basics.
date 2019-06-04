#list compr with conditional statements.
#To find the squares of the number range from 0 to 8.
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)
#to use else in the list comprhnsn then be careful with the syntax.
#squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
#the above statement will give the syntax error.
#to write the correct code, you have to follow the below syntax.

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)

#Quiz: Extract First Names
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# write your list comprehension here
first_names = [name.split()[0].lower() for name in names]
print(first_names)

#Quiz: Multiples of Three
#Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [i*3 for i in range(1,21)]
print(multiples_3)

#Quiz: Filter Names by Scores
#Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
# write your list comprehension here
passed =[name for name, score in scores.items() if score >= 65]

print(passed)