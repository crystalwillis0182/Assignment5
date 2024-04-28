class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2023"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items:", sum(item.item_quantity for item in self.cart_items))
            for item in self.cart_items:
                print("{} {} @ ${} = ${}".format(item.item_name, item.item_quantity, item.item_price, item.item_price * item.item_quantity))
            print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("\nItem Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))

def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart.")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit.")
    while True:
        choice = input("Choose the option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(item_name, item_description, item_price, item_quantity))
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def main():
    customer_name = input("Enter the customer's name: ")
    current_date = input("Enter today's date: ")
    
    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)
    
    shopping_cart = ShoppingCart(customer_name, current_date)
    
    print_menu(shopping_cart)

if __name__ == "__main__":
    main()