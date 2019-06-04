#Tricky one
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

#three
#What will the output of the following code be?
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

#two
animals = {'dogs': [20, 10, 15, 8, 32, 15], 
 'cats': [3,4,2,8,2,4], 
 'rabbits': [2, 3, 3], 
 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals['dogs'][3])