#Dictionaries
#A dictionary is a mutable data type that stores mappings of unique keys to values. 
#Here's a dictionary that stores elements and their atomic numbers.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

print("carbon" in elements)
print(elements.get("dilithium"))

#Quiz1
#Which of these could be used as the key for a dictionary? (Choose all that apply.) 
#Hint: Dictionary keys must be immutable, that is, they must be of a type that is not modifiable.
#Ans: str,int,floa, Not list.

#get with a Default Value
elements.get('dilithium')
elements.get('kryptonite', 'There\'s no such element!')


#Identity Operators
#Keyword	Operator
#is	evaluates if both sides have the same identity
#is not	evaluates if both sides have different identities

n = elements.get("dilithium")
print(n is None)
print(n is not None)

#Checking for Equality vs. Identity: == vs. is
#What will the output of the following code be?
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

#Ans:True,True,True,False

