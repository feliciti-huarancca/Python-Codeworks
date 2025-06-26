'''
My shopping cart is like a black hole—things go in, but I have no idea how they multiply.
It starts with one item, and suddenly, I'm buying a waffle maker and a inflatable pool float I'll never use. 😅🛒
'''

CART = [
    {'item': 'Waffle Maker', 'price': 29.99},
    {'item': 'Inflatable Pool Float', 'price': 15.99},
    {'item': 'Bluetooth Speaker', 'price': 49.99},
    {'item': 'Wireless Earbuds', 'price': 79.99},
    {'item': 'Smartphone Stand', 'price': 19.99},
    {'item': 'Portable Charger', 'price': 25.99},
    {'item': 'Yoga Mat', 'price': 39.99},
    {'item': 'Coffee Maker', 'price': 89.99},
    {'item': 'tv', 'price': 300},
    {'item': 'laptop', 'price': 1000},
    {'item': 'headphones', 'price': 50},
    {'item': 'book', 'price': 15},
    {'item': 'coffee mug', 'price': 10}
]

def display_details(cart):
    for item in cart:
        print(f'🛍️  {item['item']} | ${item['price']}')

def add_item_to_cart(cart, item, price):
    cart.append({'item': item, 'price': price})
    print(f'🛒  Added {item} to the cart.')

def remove_item_from_cart(cart, item_name):
    for item in cart:
        if item['item'].lower() == item_name.lower():
            cart.remove(item)
            print(f'🗑️  Removed {item_name} from the cart.')
            return

    print(f'❌  {item_name} not found in the cart.')

def save_cart_to_file(cart):
    try:
        with open('cart.txt', 'w') as file:
            for item in cart:
                file.write(f'{item['item']} | ${item['price']} \n')
    except Exception as e:
        print(f'An error ocurred while saving the cart: {e}')

def read_cart_from_file():
    try:
        with open('cart.txt', 'r') as file:
            print(f'****** Cart Content 🛒 ***\n{file.read()}')
    except FileNotFoundError as e:
        print(f'Cart file not found 🥹. Please add items first. Error: {e}')
    except Exception as e:
        print(f'An error ocurred while saving the cart: {e}')

def shopping_cart_system():
    try:
        while True:
            print('Welcome to the Shopping Cart System! Choose an option:\n')
            option = input('1. View Cart\n2. Add Item\n3. Remove Item\n4. Exit\nEnter your choice: ')

            if option == '1':
                display_details(CART)
            elif option == '2':
                item = input('Enter the item name: ')
                price = float(input('Enter the item price: '))
                add_item_to_cart(CART, item, price)
            elif option == '3':
                item_name = input('Enter the item name to remove: ')
                remove_item_from_cart(CART, item_name)
            elif option == '4':
                print('Exiting the Shopping Cart System. Goodbye! 👋')
                return
    except Exception as e:
        print(f'An error occurred: {e}')

#remove_item_from_cart(CART, 'laptop')
#display_details(CART)
#add_item_to_cart(CART, 'Smartwatch', 199.99)
#add_item_to_cart(CART, 'Wireless Mouse', 29.99)
#save_cart_to_file(CART)
#read_cart_from_file()

shopping_cart_system()
