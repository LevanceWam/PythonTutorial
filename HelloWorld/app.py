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
