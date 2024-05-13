leerUsuario = open("login.txt", "rt", encoding='utf8')
leerClave = open("clave.txt", "rt", encoding='utf8')


datosUsuario = leerUsuario.read()
datosClave = leerClave.read()

def agregar_personas():
    archdni = open("dni.txt", "at")
    contndni = input("indicar dni para agregar: ")
    archdni.write("\n" + contndni)
    archdni.close()
    archjnombre = open("nombre.txt", "at")
    contjnombre = input("indicar nombre para agregar: ")
    archjnombre.write("\n" + contjnombre)
    archjnombre.close()
    archjapellido = open("apellido.txt", "at")
    contjapellido= input("indicar apellido para agregar: ")
    archjapellido.write("\n" + contjapellido)
    archjapellido.close()
    
    

def listar_personas():
    archlistardni = open("dni.txt", "rt", encoding='utf8')
    archlistarnombre = open("nombre.txt", "rt", encoding='utf8')
    archlistarapellido = open("apellido.txt", "rt", encoding='utf8')
    contlista = []
    while True:
        dni = archlistardni.readline().strip()
        nombre = archlistarnombre.readline().strip()
        apellido = archlistarapellido.readline().strip()
        if not dni:  # Si se llega al final del archivo
            break
        contlista.append(f"{dni}\t{nombre}\t{apellido}")
    archlistardni.close()
    archlistarnombre.close()
    archlistarapellido.close()
    return contlista

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

def salir():
    print("Gracias por su visita")

def error():
    print("Opción incorrecta")

def menu():
    print("*** Datos Persona ***")
    print("1. Listar")
    print("2. Agregar Personas")
    print("3. Salir")

def opcion():
    opcion = int(input("Ingrese opción: "))
    while True:
        if opcion == 1:
            contlista = listar_personas()
            print("\n".join(contlista))  # Muestra el resultado de listar_personas()
            break
        elif opcion == 2:
            agregar_personas()
            break
        elif opcion == 3:
            break
        else:
            print("Opción incorrecta")

login()
opcion()
