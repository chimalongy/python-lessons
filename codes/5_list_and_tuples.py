# LIST
# List hold multiple values

users = ["Chima", "Longy", "Sara", "John"]
data = ['Dave', 42, True]
# a list can contain any datatype

print("Dave" in users)
print(users[0])
print(users[-2])

print(users.index("Longy"))

print(users[-3:-1])

users.append("Victor")


users += ["Victoria", "Oluchi"]
print(users)
# users.extend(data)
print(users)

# Remove items
print("***************************************")
users.remove("John")
print(users)

# Remove the last item
print(users.pop())

# delete a list

# del data

# clear list
data.clear()


# sorting list// lowercase comes after the upper case

users.sort()
print(users)

# to make sort to come in lower case first
users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]

nums.reverse()
print(nums)
nums.sort(reverse=True)
print(nums)

# tuple are like constant list... there values does not change

mytuple = tuple(("Chima", "Longy", "070"))
print(type(mytuple))
