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
    pay_rate = 0.8 
    all=[]
    def __init__(self, name: str, price, quantity):
        #Run validation to the received arguments(making sure there is no negative value provided)
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"

        #Assign to self object
        self.name=name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price= self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

item1 = Item("phone",100,21)
print(item1.calculate_total_price())
print(Item.__dict__)# Used to view class attributes
print(item1.__dict__)#used to view attributes belonging to a particular object
print(Item.pay_rate)

item2 = Item("laptop", 1000, 61)
print(item2.calculate_total_price())

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

item1.apply_discount()
print(item1.price)
print(item1.calculate_total_price())



item1 = Item("phone", 100, 1)
item2 = Item("laptop", 1000, 6)
item3 = Item("cable", 10, 5)
item4 = Item("mouse", 80, 7)
item5 = Item("keyboard", 75, 4)

print(Item.all)

for i in Item.all:
    print(i)
