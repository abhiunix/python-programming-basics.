#forloopQuiz
#Write a for loop that iterates over the names list to create a usernames list. 
#To create a username for each name, make everything lowercase and replace spaces with underscores. 
#Running your for loop over the list:
#names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#should create the list:
#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
#HINT: Use the .replace() method to replace the spaces with underscores.
#Check out how to use this method in this Stack Overflow answer.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames=[]
for name in names:
    usernames.append(name.lower().replace(' ','_'))


print(usernames)

#Eg2
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)


#eg3
#Quiz: Modify Usernames with Range
#Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
#Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. 
#After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#remember in range value at stoping is always excluded. Hence here 4 is not considered.
for i in range(0,len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ','_')
print(usernames)