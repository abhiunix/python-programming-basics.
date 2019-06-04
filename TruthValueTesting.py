#Truth Value Testing
#Here are most of the built-in objects that are considered False in Python:
#constants defined to be false: None and False
#zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
#empty sequences and collections: '"", (), [], {}, set(), range(0)
#Example:

errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")

#eg2
points = 174  # use this as input for your submission

# establish the default prize value to None

prize = None
# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)