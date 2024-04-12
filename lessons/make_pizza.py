"""Practice instantiating Pizza class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)

# def price(pizza_order: Pizza) -> float:
#     """Calculate and return cost of pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else: 
#         cost = 5.0
#     # charge .75 per topping
#     cost += .75 * pizza_order.toppings
#     # charge $1 for gluten free
#     if pizza_order.gluten_free: 
#         cost += 1.0
#     return cost

print(my_pizza.price())
print(sals_pizza.price())

class Pet:
   
    name: str
    breed: str
 
    def __init__(self, pet_name: str, pet_breed: str):
        self.name = pet_name   
        self.breed = pet_breed

    def speak(self):
        if self.breed == "dog":
            print("Woof!")
        else:
            print("*silence*")
           
a1: Pet = Pet("Fido", "dog")
a2: Pet = Pet("Fluffy", "cat")
print(a1.speak())