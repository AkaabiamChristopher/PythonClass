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
            view_product()
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
menu()
