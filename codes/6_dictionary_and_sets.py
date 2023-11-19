# Dictionaries
# use to store data value in key value pairs

band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(len(band))  # length of a dictionary

# Access items
print(band['vocals'])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key value pairs as tuples
print(band.items())

# verify if a key exists

print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

# Remove Items

print(band.pop("bass"))

print(band)

band['drums'] = "kick"

# Delete items

del band["vocals"]
band2.clear()
del band2

# Nested Dictionary
member1 = {
    "name": "Samson",
    "role": "Singer"
}
member2 = {
    "name": "Oreva",
    "role": "Drumer"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# SET doe not accept duplicates
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 2, 3, 4))

print(nums)
print(nums2)

# True is a duplicate of 1 and false is a duplicate of 0

# check if a value is in a set
print(2 in nums)
# add a new element

nums.add(8)

# Add elements from one set to another
nums3 = {8, 9, 10}
nums.update(nums3)

#merging to sets

nums.union(nums3)
