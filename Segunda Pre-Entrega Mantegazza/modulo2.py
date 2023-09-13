import re
import json

def register(database):
    #Ingresar usuario
    username = input("Enter your username: ")
    #El programa va a seguir preguntando por un usuario hasta que no tenga igual o mas de 8 caracteres
    while len(username) < 8:
      print("Username must contain at least 8 characters.")
      username = input("Enter your username: ")

    #Ingresar contrasena
    password = input("Enter your password: ")
    #El programa va a seguir preguntando por la contrasena hasta que no cumpla con los requisitos
    while len(password) < 8 or bool(re.search(r'\d', password)) == False or bool(re.search(r'[A-Z]', password)) == False or bool(re.search(r'\W', password)) == False:
      print("Password must contain at least:\n- 8 characters\n- 1 number\n- 1 uppercase letter\n- 1 special character")
      password = input("Enter your password: ")

    #Guardamos usuario y contrasena en el diccionario database
    database[username] = password

def save_in_json(database):
    with open("./database.json", 'w') as f:
        json.dump(database, f, indent=4)

def read_database(database):
    print("The database contains:")
    #Bucle que itere la base de datos y devuelva usuario:contrasena en formato clave:valor
    for key, value in database.items():
        print(f"Username: {key} | Password: {value}")

def login(database):

    #Ingresar usuario
    username = input("Enter your username: ")
    #Si el usuario esta en la base de datos pasa a preguntar la contrasena
    if username in database:
        pass
    #Si el usuario no esta en la base de datos lo va a seguir preguntando hasta que lo encuentre
    else:
        while username not in database:
            username = input("User not found, enter again: ")

    #Ingresar contrasena
    password = input("Enter your password: ")
    #Si la contrasena coincide con el value de la base datos, inicias sesion
    if password == database[username]:
        print("Welcome!")

    #Si la contrasena no coincide te va a seguir preguntando hasta que lo haga, y ahi, inicias sesion
    else:
        while password != database[username]:
            password = input("Wrong password, enter again: ")
        print("Welcome!")


db = {}
register(db)
read_database(db)
login(db)
save_in_json(db)