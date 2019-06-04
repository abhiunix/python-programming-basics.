# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 5
guess = 5

if guess<5:
    result = "Oops!  Your guess was too low."
elif guess>5:
    result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"

print(result)

#Quiz: Tax Purchase
#Depending on where an individual is from we need to tax them appropriately.
#The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
#Use this information to take the amount of a purchase 
#and the corresponding state to assure that they are taxed by the right amount.
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)