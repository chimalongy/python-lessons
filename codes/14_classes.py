# classes are blue prints for creating objects
# names start with capital letters
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


mycar = Vehicle("Tesla", "Model 3")
print(mycar.make)
print(mycar.model)
mycar.moves
mycar.get_make_model()

# inheritance.. this is when a class in dependent on another class


class Airplane(Vehicle):
    def moves(self):
        prints("flies above")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass  # inherits everything in the vehicle class
