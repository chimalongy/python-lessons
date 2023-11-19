# RECURSIVE FUNCTIONS.
# this is when a function calls itself


def addOne(num):
    if (num >= 9):
        return num+1
    total = num +1
    print(total)
    
    return addOne(total)


addOne(0)