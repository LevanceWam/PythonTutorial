print("Hello world Vance is here")
print('o-------')
print(' |||||')
# this way we can have 10 * instead of having to type it out
print('*' * 10)

# price will change because it goes from top to bottom and it goes from the last declared so it will print 20
price = 10
price = 20
rating = 4.9
name = 'vance'
is_published = False
print(price)


# Create a new patient named john smith 20 years old and if he is a new patient.

firstName = 'John'
lastName = 'Smith'
age = 20
new_patient = True

print('Patient Info: ', firstName, lastName, age, 'is a new patient', new_patient)

# input is python's way of asking questions
new_name = input('What is your name? ')
print('Hi ' + new_name)

# Create 2 prompts asking the user's name and favorite color

ask_name = input('What is your name buddy? ')
ask_color = input ('What is your favorite color guy? ')
print(ask_name + ' loves ' + ask_color)

# Type conversion
birth_year = input('Birth Year: ')
print(type(birth_year))
# int() turns a string into a integer
# float() turns a string into a number with a decimal
# bool() turns a string into a boolean value
# type() let's you know what kind of variable you have
current_age = 2020 - int(birth_year)
print(type(current_age))
print(current_age)

# Ask for the users weight (nicely) and convert it to kilograms
weight = input('What is your weight in pounds? ')
kilogram = int(weight) * 0.45
print(type(kilogram))
print(' Your converted weight is: ', kilogram, 'kg')

# Strings
# strings for multiple length example tripe quotes
course = '''
Hi Vance, 

Here is our first email to you.

Thank you,
The Support Team

'''

course2 = 'Python for Beginners'
# indexes do not start with 1 they start with 0 so P will be 0
print(course2[0])
# this will go backwards from the start of the index
print(course2[-2])
# this way we can call more than one index we are going to go from 0 - 4 but it will only show up to the third index
print(course2[0:4])
# By only using 1 number and leaving the other blank we will take away characters in the index so if we type in 2
# indexes 0,1 will be missing
print(course2[2:])
# if we do it from the opposite side of the colon it will start from 0 to the number you chose in the index
print(course2[:6])

# cloning the course2 variable
another = course2[:]
print(another)

# test what would happen if we printed a variable with this [1:-1] I believe index 0 will only show up
new_name = 'Chelsea'
print(new_name[1:-1])
# I was wrong it took out the first and last indexes

# Formatted Strings
first_name = 'Johnny'
last_name = 'Walker'
# This is not the ideal way to do this
message = first_name + ' [' + last_name + '} is a coder'
# let's try this with a formatted string.
# formatted strings start with a f like below
# the curly braces acts as placeholders for the variables we want to add into the string
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)

# String Method
course3 = 'Python for Beginners'
# len() gives you the number of characters in a string
print(len(course3))
# .upper will make the string all caps
print(course3.upper())
# .lower will make the string lower case
print(course3.lower())
# We can find a characters index by using .find
print(course3.find('P'))
# lets use the .replace method *note that this is a very case sensitve method
print(course3.replace('Beginnners', 'Absolute Beginners'))
print(course3.replace('P', 'J'))
# Checking for the existence of characters in the string *note this is also very case sensitive
# the "in" operator produces a boolean value, Do we have it or not
print('Python' in course3)

# Arithmetic Operations
# Division and Modules
# if we add 2 slashes we will get the whole number only not the decimal
print(10 / 3)
print(10 // 3)
# module will return the reminder of the divison
print(10 % 3)
# exponent or the power to
print(10 ** 3)
# Augmented assigned operator (shortcuts to writing the equations)
x = 10
x = x + 3
print(x)
# this is the same as line 127
x += 3
print(x)
# Now lets subtract
x -= 3
print(x)

# Operator Precedence
y = 10 + 3 * 2
# will equal 16
print(y)
# order that the operators will go
# parenthesis (priority)
# exponenation (2**3)
# multiplication or division
# addition or subtraction

y = (2 + 3) * 10 - 3
# this should equal 47
print(y)
# I was correct



