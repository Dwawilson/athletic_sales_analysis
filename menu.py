# Create an empty list to store the customer's order
order = []

# Print the menu
print("Welcome to the restaurant!")
print("Menu:")

# Print the menu items here...

# Define menu_items as a dictionary
menu_items = {
    1: {"name": "Hotchips", "price": 5.99},
    2: {"name": "Hotdogs", "price": 4.99},
    3: {"name": "Fire Chicken", "price": 8.99},
    4: {"name": "Beef Wrap Bacon", "price": 7.99}
}

# Prompt the customer for their selection
menu_selection = input("Please enter the number of the item you'd like to order: ")

# Convert menu_selection to an integer
menu_selection = int(menu_selection)

# Get the item name from the menu_items dictionary
item_name = menu_items[menu_selection]["name"]

# Ask the customer for the quantity
quantity = input(f"How many {item_name}s would you like to order? (Default is 1): ")

# Check if quantity is a number
if not quantity.isdigit():
    quantity = 1
else:
    # Convert quantity to an integer
    quantity = int(quantity)

# Inside a continuous while loop
while True:
    # Prompt the customer if they would like to keep ordering
    decision = input("Would you like to keep ordering? (y/n): ").lower()
    
    # Check the customer's decision
    if decision == 'y':
        # Continue ordering
        continue
    elif decision == 'n':
        # Exit the loop
        break
    else:
        # Handle invalid input
        print("Invalid input. Please enter 'y' to continue ordering or 'n' to finish.")
