#object oriented programming in python

#class - A blueprint or template that defines the structure and behaviour of objects
#Example>> class Car:
"""class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")"""

#objects - An instance of a class. It represents a specific entity or concept
#example >> my_car = Car("Toyota", "Red")

#Attributes - The data variables associated with a class. They store information about the object's state
    #example >>> print(my_car.brand)  # Output: Toyota
                    #my_car.color = "Blue" 

#methods - this are fuctions that are within a class

#constructor('--init--')

class Item:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("phone",100,21)
print(item1.calculate_total_price())

item2 = Item("laptop", 1000, 61)
print(item2.calculate_total_price())

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
