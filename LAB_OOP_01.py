
class Drink:

    def __init__(self, name:str, price:float, size:str) -> None:

        self.name = name
        self.price = price
        self.size = size

    def display_info (self):
        print(f"{self.name} ({self.size}) - {self.price} SAR")

latte = Drink("Latte", 18, "Medium")
espresso  = Drink("Espresso", 12, "Small")
cappuccino  = Drink("Cappuccino", 22, "Large")
print("=== Coffee Shop Menu ===")
latte.display_info()
espresso.display_info()
cappuccino.display_info()