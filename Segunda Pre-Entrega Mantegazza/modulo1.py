class Product:
    def __init__(self, prod_name, price):
        self.prod_name = prod_name
        self.price = price
    
    def __str__(self):
        return self.prod_name

class Clients:
    
    def __init__(self, name, last_name, email, dni):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.dni = dni
        self.cart = []
        self.purchase_history = []
        
    
    def add_to_cart(self, product):
        self.cart.append(product)
        
    def show_cart(self):
        print("Shopping cart: ")
        for product in self.cart:
            print(f"{product} - ${product.price}")
    
    def purchase(self):
        if self.cart:
            self.purchase_history.append(self.cart.copy())
            self.cart = []
        else:
            print("Cart is empty. Nothing to purchase.")
            
    def calculate_total(self):
        total = sum(product.price for product in self.cart)
        return total