#Enumerate
#enumerate is a built in function that returns an iterator of tuples containing indices and values of
#a list. You'll often use this when you want the index along with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

#Quiz: Enumerate
#Use enumerate to modify the cast list so that each element contains the name followed by the 
#character's corresponding height. For example, the first element of cast should change from 
#"Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

#forLoop

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])


print(cast)