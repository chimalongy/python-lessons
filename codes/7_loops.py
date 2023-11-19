# While loop
# executes a block of code while a condition is true
value = 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is not equal to "+ str(value))


# FOR LOOP iterates over a sequence

names = ["Dave", "Sarah", "John"]

# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sarah":
#         break
#     print(x)
# for x in names:
#     if x == "Sarah":
#         continue
#     print(x)

# for x in range(4):
#     print(x)
# for x in range(2, 4):
#     print(x)
for x in range(0, 101, 5):
    print(x)
else:
    print("glad that\'s over")

names = ["Dave", "Sarah", "John"]
actions = ['code', "eat", "sleep"]

for name in names:
    for action in actions:
        print(name + " " + action+".")
