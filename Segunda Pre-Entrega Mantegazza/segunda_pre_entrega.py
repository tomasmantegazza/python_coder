##Crear un programa que permita el modelamiento de Clientes en una página 
# de compras.

##La Clase Cliente debe tener mínimo 4 atributos y 2 métodos.

##Se debe utilizar el método __str__() para darle nombre a los objetos.

##Crear un paquete redistribuible con el programa creado.


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

#Crear y mostrar cliente
client1 = Clients("Tomas", "Mantegazza", "tomas@gmail.com", 43013500)
print(f"Client name: {client1.name}\nClient last name: {client1.last_name}\nClient email: {client1.email}\nDNI number: {client1.dni}\n")

#Crear productos
product1 = Product("Shirt", 20.0 )
product2 = Product("Hoodie", 40.0)

#Agregar productos al carrito y mostrar el carrito
client1.add_to_cart(product1)
client1.add_to_cart(product2)
client1.show_cart()

#Calcular el total de al compra e imprimirla
total = client1.calculate_total()
print(f"Total: ${total}\n")

#Terminar la compra
client1.purchase()
print("Purchase history:")
for purchase in client1.purchase_history:
    for product in purchase:
        print(f"{product} - ${product.price}")
