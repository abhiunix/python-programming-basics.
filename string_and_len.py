#String().

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
print(username + " accessed the site " + url + " at " + timestamp + ".")
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

#len() function.
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name) + len(middle_names) + len(family_name) + 2
# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

#https://atom.io/packages/linter-python-pep8
