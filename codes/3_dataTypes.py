# STRING DATATYPES

# LITERAL ASSIGNMENT
import math
firstName = "Chima"
lastName = "Longy"

# print(type(firstName))
# print(type(firstName) == str)
# print(isinstance(first, str))

# constructor
pizza = str('Pepperoni')

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# CONCATINATION

fullName = firstName + " " + lastName
print(fullName)

# CASTING A NUMBER TO A STRING

decade = str(1950)
print(type(decade))

print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# MULTIPLE LINE
multiline = '''
        Hey how are you?

        I was just checking in.
                                All good.
'''

print(multiline)

# Escaping Special Characters

sentence = "I\'m baack at work!\tHey!\n\nWere\'s at\\located?"

print(sentence)

# String Methods
print(firstName)
print(firstName.lower())
print(firstName)
print(firstName.upper())

print(multiline.title())
print(multiline.replace("good", "okay"))
print(len(multiline))
multiline += "                               "
print(len(multiline))
multiline = "                       "+multiline
print(len(multiline))

# remove all white space

print(multiline.strip())

# Build a menu

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".")+"$1".rjust(4))
print("Muffin".ljust(16, ".")+"$1".rjust(4))
print("Cheesecake".ljust(16, ".")+"$1".rjust(4))

# String index value

print(firstName[0])  # string indexes start with 0
print(firstName[1])  # string indexes start with 0
print(firstName[-1])  # string last indexe
# Prining a range
print(firstName[1:-1])  # values in a range dont show in the range
print(firstName[1:])  # values in a range dont show in the range

print(firstName.startswith("k"))
print(firstName.endswith("a"))


# BOOLLEAN DATA TYPE
myValue = True
myValue2 = False

x = bool(False)

print(type(x))
print(isinstance(myValue, bool))

# NUMERIC DATA TYPES

# INTEGERS
price = 100
bestprice = int(80)
print(type(price))

# FLOAT TYPE
gpa = 3.8
y = float(gpa)

# complex type
comp_value = 5+3j
print(type(comp_value))
print((comp_value.real))
print((comp_value.imag))

# Built in functions of a number
print(abs(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
