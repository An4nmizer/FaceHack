
import time
print("")
print("")
tx=10
print("Para usar esta herramienta es necesario crear un usuario y clave")

print("CREACION DE LA CUENTA")
user=input("Ingresa el nombre de usuario que utilizaras : ")
key=input("Ingresa tu clave : ")
print("")
print("Inicio de sesión")
print("")
u=input("Ingresa tu usuario : ")
while u!=user:
    u=input("Usuario incorrecto, intente nuevamente : ")
print("")
passw=input("Ingrese su clave :")
while passw!=key:
    passw=input("Clave incorrecta, intente nuevamente : ")

print("")
print("Espere...")
time.sleep(5)
print("")
print("")

print("BIENVENIDO ",user,end="")
print(" !!! ")

print("    ___                           _                        _              ")
print("   | __|  __ _     __      ___   | |_     __ _     __     | |__     o O O ")
print("   | _|  / _` |   / _|    / -_)  | ' \   / _` |   / _|    | / /    o      ")
print("  _|_|_  \__,_|   \__|_   \___|  |_||_|  \__,_|   \__|_   |_\_\   TS__[O] ")
print("_| +++ |_|+++|_|++++++|_|++++++|_|+++++|_|+++++|_|++++|_|++++++| {======| ")
print("+`-0-0-++`-0-0-++`-0-0-++`-0-0-++`-0-0-++`-0-0-++`-0-0-++`-0-0-'./o--000' ")

print("1.FB brute force hacking")
print("2.Salir")
opc=input("Selecciona una opcioón : ")
opc=int(opc)

if opc==1:
    ID=input("Ingresa el ID de la victima : ")
    print("Recopilando informacion, espere...")
    time.sleep(tx)
    print("")
    print("Se enviará un mensaje a : ")
    ID="https://facebook.com/"+ID
    print(ID)
    print("Le informaremos sobre la situación proporcionandole la siguiente información : ")
    print("")
    print("-Región : México")
    print("-Número de télefono : +52 55 1338 4517")
    print("-Dispositivo movil : Huawei P smart 2019")
    print("-Ubicación : Naucalpan, México")


elif opc==2:
    print("Gracias por usar la aplicación :D!!")
    
    

