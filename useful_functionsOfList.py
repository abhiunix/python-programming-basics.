#Useful Functions for Lists II
#join method
#Join is a string method that takes a list of strings as an argument, 
#and returns a string consisting of the list elements joined by a separator string.
#eg1
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["García", "O'Kelly"])
print(name)


#eg2
#append method
#A helpful method called append adds an element to the end of a list.
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

#eg3
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#eg4 Join and sorted mix
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

#eg5 append and list
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))