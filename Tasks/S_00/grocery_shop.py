# Define the products available in the grocery shop as a tuple of tuples
products = (
    ("bread", 1.0),
    ("rice", 3.4),
    ("sugar", 0.8),
    ("milk", 0.9),
    ("tea", 1.8),
    ("coffee", 2.7)
)

# Define a function to display the available products
def display_products():
    print("Available products:")
    for i, product in enumerate(products):
        print(f"{i+1}. {product[0]} - ${product[1]:.2f}")

# Define the shopping cart as an empty dictionary
cart = {}

# Display the available products
display_products()

# Loop to allow the user to add products to their cart
while True:
    # Ask the user to enter the product number
    product_number = input("Enter product number to add to cart (or 'q' to quit): ")
    # If the user enters 'q', break out of the loop
    if product_number.lower() == 'q':
        break
    # Convert the input to an integer and subtract 1 to get the index of the selected product
    product_index = int(product_number) - 1
    # Get the selected product from the products tuple
    selected_product = products[product_index]
    # Ask the user to enter the quantity
    quantity = int(input(f"Enter quantity for {selected_product[0]}: "))
    # Add the selected product and quantity to the cart dictionary
    cart[selected_product[0]] = quantity

# Display the items in the cart and the total cost
print("Items in the cart:")
total_cost = 0
for product, quantity in cart.items():
    price = [p[1] for p in products if p[0] == product][0]
    cost = price * quantity
    total_cost += cost
    print(f"{product} x {quantity} = ${cost:.2f}")

# Display the total cost
print(f"Total cost: ${total_cost:.2f}")

# Ask the user if they want to modify or remove a product in the cart
while True:
    choice = input("Do you wish to modify or remove a product from the cart? (m:modify/r:remove/n:no): ")
    if choice.lower() == 'n':
        break
    elif choice.lower() == 'm':
        # Ask the user to enter the product to modify
        product_to_modify = input("Enter the name of the product to modify: ")
        # If the product is not in the cart, ask the user to try again
        if product_to_modify not in cart:
            print("That product is not in the cart.")
        else:
            # Ask the user to enter the new quantity
            new_quantity = int(input(f"Enter the new quantity for {product_to_modify}: "))
            # Update the quantity in the cart dictionary
            cart[product_to_modify] = new_quantity
            # Display the updated items in the cart and the total cost
            print("Updated items in the cart:")
            total_cost = 0
            for product, quantity in cart.items():
                price = [p[1] for p in products if p[0] == product][0]
                cost = price * quantity
                total_cost += cost
                print(f"{product} x {quantity} = ${cost:.2f}")
            # Display the updated total cost
            print(f"Updated total cost: ${total_cost:.2f}")
    elif choice.lower() == 'r':
        # Ask the user to enter the product to remove
        product_to_remove = input("Enter the name of the product to remove: ")
        # If the product is not in the cart, ask the user to try again
        if product_to_remove not in cart:
            print("That product is not in the cart.")
        else:
            # Remove the product from the cart dictionary
            del cart[product_to_remove]
            # Display the updated items in the cart and the total cost
            print("Updated items in the cart:")
            total_cost = 0
            for product, quantity in cart.items():
                price = [p[1] for p in products if p[0] == product][0]
                cost = price * quantity
                total_cost += cost
                print(f"{product} x {quantity} = ${cost:.2f}")
            # Display the updated total cost
            print(f"Updated total cost: ${total_cost:.2f}")
    else:
        print("Invalid choice. Please try again.")