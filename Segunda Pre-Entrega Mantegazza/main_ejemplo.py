from modulo1 import *

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