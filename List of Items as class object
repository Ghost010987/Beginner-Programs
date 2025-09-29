# Practice OOP (object oriented programming)

class Item:
    # Class level list to store all the items created.
    all_items = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Append the created item into the class-level list
        Item.all_items.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    @classmethod
    def calculate_inventory_value(cls) -> float:
        """ Calculate the total value of all items in inventory. """
        return sum(item.calculate_total_price() for item in cls.all_items)
    
    def __repr__(self):
        """ Unambiguous string repersentation for debugging/printing. """
        return f"Item(Name='{self.name}', Price={self.price}, Quantity={self.quantity})"
    
# ------------------------ User Input Section --------------------------------

print(" Enter item details. Type 'done' as the name when finished. \n")

while True:
    name = input("Item name (or 'done' to finish): ").strip()
    if name.lower() == "done":
        break

    try:
        price = float(input("Item price: "))
        quantity = int(input("Item quantity: "))
        Item(name, price, quantity)
    except ValueError:
        print("X invalid input please enter numeric value for price and quantity.")
        continue

# ------------------------------------Output Section ----------------------------
print("\nAll items in inventory: ")
for item in Item.all_items:
    print(f"{item} | Total Price: {item.calculate_total_price()}")

print(f'\nTotal inventory value: {Item.calculate_inventory_value()}')
