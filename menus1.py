def menu():
	cart = []
	
print("\nWelcome to Jessica's e-store") 
print("1. View Product")
print("2, Add to cart")
print("3. Remove from Cart")
print("4. View Cart")
print("5. Checkout")
print("6. Exit")
select = input("Choose an option: ")
	
if select == '1':
	select_product()
elif select == '1':
	product_name = input("Enter the product name to add to cart: ")
	add_to_cart(cart,prouct_name)
		
elif select == '3':
	product_name = input("Enter the product name to removefrom cart: ")
	remove_from_cart(cart,product_name)
elif '4':
	selectview_cart()
elif '5':
	checkoyt(cart)
elif '6':
	print("Thank you for visiting Jessica's e-store")
else:
	print("Invalid selection..... please try again.")
menu()
def __init__(self, name, price):
        self.name = name
        self.price = price
def __str__(self):
        return f"{self.name} - ${self.price}"

laptop = Product("Laptop", 1000)
phone = Product("Phone", 500)
headphones = Product("Headphones", 100)

product_catalogue = [laptop, phone, headphones]

def view_products():
    print("Product Catalogue:")
    for product in product_catalogue:
        print(product)

view_products()

def add_to_cart(cart, product_name):
    for product in product_catalogue:
        if product.name.lower() == product_name.lower():
            cart.append(product)
            print(f"{product.name} has been added to your cart.")
            return
    print(f"{product_name} not found in product catalogue.")

cart = []
add_to_cart(cart, "Phone")
add_to_cart(cart, "Laptop")

def view_cart(cart):
    if not cart:
        print("Your cart is currently empty.")
    else:
        print("Your Shopping Cart:")
        for product in cart:
            print(product)
    print()  

view_cart(cart)

def calculate_total(cart):
    total = sum(product.price for product in cart)
    return total

def checkout(cart):
    total = calculate_total(cart)
    if cart:
        print(f"Thank you for shopping with us! Your total is ${total}.")
        cart.clear()
    else:
        print("Your cart is empty. Please add items to your cart before checkout.")

checkout(cart)
view_cart(cart) 

