leerUsuario = open("login.txt", "rt", encoding='utf8')
leerClave = open("clave.txt", "rt", encoding='utf8')


datosUsuario = leerUsuario.read()
datosClave = leerClave.read()


def login():
    intentos_restantes = 2
    while intentos_restantes > 0:
        usuario = input("Ingrese su usuario: ").strip()
        password = input("Ingrese su contraseña: ").strip()
       
        if usuario == datosUsuario and password == datosClave:
            menu()
            return  # Salir de la función si las credenciales son correctas
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"Credenciales incorrectas. Te quedan {intentos_restantes} intento.")
            else:
                print("Has excedido el número máximo de intentos.")
                exit()


def menu():
    print("*** Datos Persona ***")
    print("1. Listar")
    print("2. Agregar Personas")
    print("3. Salir")


login()    
