# functions are defined with lowercase
def hello():
    print("👋👋 Hello world")


hello()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(7, 4)


print(total)

# unknown amount of parameters


def multipleItems(*args):
    print(args)
    print(type(args))


multipleItems("Dav", "comes", "3")


def multnamed(**kwargs):
    print(kwargs)
    print(type(kwargs))


multnamed(first="Dave", last="Grey")
