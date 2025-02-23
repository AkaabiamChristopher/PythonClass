product_catalogue = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Headphones", "price": 100}
]

def view_products():
    print("Product Catalogue:")
    for product in product_catalogue:
        print(f"{product['name']} - ${product['price']}")
def add_to_cart(cart, product_name):
    for product in product_catalogue:
        if product["name"].lower() == product_name.lower():
            cart.append(product)
            print(f"{product['name']} has been added to your cart.")
            return
    print(f"{product_name} not found in product catalogue.")
def view_cart(cart):
    if not cart:
        print("Your cart is currently empty.")
    else:
        print("Your Shopping Cart:")
        for product in cart:
            print(f"{product['name']} - ${product['price']}")
    print()  
def remove_from_cart(cart, product_name):
    for product in cart:
        if product["name"].lower() == product_name.lower():
            cart.remove(product)
            print(f"{product['name']} has been removed from your cart.")
            return
    print(f"{product_name} not found in your cart.")
def calculate_total(cart):
    return sum(product['price'] for product in cart)
def checkout(cart):
    total = calculate_total(cart)
    if cart:
        print(f"Thank you for shopping with us! Your total is ${total}.")
        cart.clear()
    else:
        print("Your cart is empty. ")
def menu():
    cart = []
    while True:
        print("\nWelcome to Jessica's E-Store!")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_products()
        elif choice == '2':
            product_name = input("Enter the product name to add to cart: ")
            add_to_cart(cart, product_name)
        elif choice == '3':
            product_name = input("Enter the product name to remove from cart: ")
            remove_from_cart(cart, product_name)
        elif choice == '4':
            view_cart(cart)
        elif choice == '5':
            checkout(cart)
        elif choice == '6':
            print("Thank you for visiting Jessica's E-Store!")
            break
        else:
            print("Invalid option. Please choose again.")

