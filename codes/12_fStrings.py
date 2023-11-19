# USED TO CREATE INSERT VARIABLES IN A STRING

person = "dave"
coins = 3

# Method 1
message = "\n%s has %s coins left" % (person, coins)
print(message)

# Method 2
message = "\n{} has {} coins left".format(person, coins)
print(message)


# Method 3
message = "\n{1} has {0} coins left".format(coins, person)
print(message)

# Method 4

message = f"\n{person}  has {coins} coins left."
print(message)
message = f"\n{person.lower()}  has {coins*3} coins left."
print(message)
