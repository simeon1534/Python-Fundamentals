class Vehicle:
    owner = None

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money, owner):
        self.money = money
        if self.money >= self.price and self.owner is None:
            self.owner = owner
            result= f"Successfully bought a {self.type}. Change: {self.money - self.price:.2f}"
            return print(result)
        elif self.money < self.price:
            result = f"Sorry, not enough money"
            return print(result)
        elif self.owner is not None:
            result = f"Car already sold"
            return print(result)

    def sell(self):                         
        if self.owner is None:
            result = f"Vehicle has no owner"
            print(result)

        else:
            self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner} "
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(30000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
 
vehicle.sell()
print(vehicle)
