#While Loops
#For loops are an example of "definite iteration" meaning that the loop's body is run a predefined 
#number of times. This differs from "indefinite iteration" which is when a loop repeats an unknown 
#number of times and ends when some condition is met, which is what happens in a while loop. Here's an 
#example of a while loop.


card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  <= 17:
    hand.append(card_deck.pop())
    print(sum(hand))
print(hand)

#This example features two new functions. sum returns the sum of the elements in a list, and pop is a 
#list method that removes the last element from a list and returns it.

#Components of a While Loop
#The first line starts with the while keyword, indicating this is a while loop.
#Following that is a condition to be checked. In this example, that's sum(hand) <= 17.
#The while loop heading always ends with a colon :.
#Indented after this heading is the body of the while loop. 
#If the condition for the while loop is #true, the code lines in the loop's body will be executed.
#We then go back to the while heading line, and the condition is evaluated again. This process of 
#checking the condition and then executing the loop repeats until the condition becomes false.
#When the condition becomes false, we move on to the line following the body of the loop, which will 
#be unindented.
#The indented body of the loop should modify at least one variable in the test condition. If the value 
#of the test condition never changes, the result is an infinite loop!




#Practice: Factorials with While Loops
#Find the factorial of a number using a while loop.

#A factorial of a whole number is that number multiplied by every whole number between itself and 1. 
#For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

#We can write a while loop to take any given number and figure out what its factorial is.

#Example: If number is 6, your code should compute and print the product, 720.

# Start with a sample number for first test - change this when testing your code more!
number = 6   
# We'll always start with our product equal to the number
product = number

# TODO: Write while loop header line - how will you tell it when to stop looping?
while  number > 1:
# TODO: Each time through the loop, what do we want to do to our number?
    number -= 1
# TODO: Each time, what do we want to multiply the current product by?
    product *= number
# TODO: Print out final product (how do we indicate this should happen after loop ends?)
print(product)

#withforLoop

# This is the number we'll find the factorial of - change it to test your code!
number = 6
# We'll start with the product equal to the number
product = number

# TODO: Write a for loop that calculates the factorial of our number 
for num in range(1, number):
    product *= num

# TODO: print the factorial of your number
print(product)

#Quiz: Count By
#Suppose you want to count from some number start_num by another number count_by until you hit a final 
#number end_num. Use break_num as the variable that you'll change each time through the loop. 
#For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

#Before the loop, what do you want to set break_num equal to? How do you want to change break_num each
#time through the loop? What condition will you use to see when it's time to stop looping?

#After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. 
#It is the case that break_num should be a number that is the first number larger than end_num.

start_num = 5 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2#provide some number to count by 
break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num < end_num:
    break_num+=count_by

print(break_num)

#Quiz: Count By Check
#Suppose you want to count from some number start_num by another number count_by until you hit 
#a final number end_num, and calculate break_num the way you did in the last quiz.

#Now in addition, address what would happen if someone gives a start_num that is greater than
#end_num. If this is the case, set result to "Oops! Looks like your start value is greater than
#the end value. Please try again." Otherwise, set result to the value of break_num.
start_num =5 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
if start_num>end_num:
    result="Oops! Looks like your start value is greater than the end value. Please try again."
else:
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
    break_num = start_num
    while break_num < end_num:
        break_num+=count_by
        result=break_num

print(result)

#Quiz: Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and 
#stores it in a variable nearest_square. A square number is the product of an integer multiplied by
# itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.
limit = 40
num=0
# write your while loop here
while (num+1)**2<limit:
    num+=1
nearest_square = num**2
     

print(nearest_square)
