"""
Looping and Dictionaries
5.1 Create a dictionary that represents a simple inventory of items and their quantities.
5.2 Use a for loop to iterate through the dictionary and print a message for each item, including
its name and quantity.
5.3 Write a function that takes a quantity as input and updates the quantities of all items in the
dictionary to that value.
5.4 Use a while loop to continuously ask the user for an item name and quantity and update the
dictionary until the user decides to exit.
"""

inventory = {
    "Apple" : 10,
    "Banana" : 20,
    "Orange" : 15,
    "Grapes" : 5,
    "Mango" : 8
}

for item, quantity in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}")

def update_quantities(quantity):
    for item in inventory:
        inventory[item] = quantity

while True:
    item = input("Enter item name (or 'exit' to quit): ")
    if item.lower() == "exit":
        break
    quantity = int(input("Enter quantity: "))
    inventory[item] = quantity

print("Updated Inventory:")
for item, quantity in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}")