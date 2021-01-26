global lista
lista = list()

class cajaregistradora:
    codigo_barras = ""
    nombre_producto = ""
    precio = [0]

    @staticmethod    
    def registrarproducto():
        print("Ingrese el producto")
        print("--------------------------------------------------")

        registro = cajaregistradora()

        registro.codigo_barras = input("Ingrese el codigo de barras del producto: ")
        registro.nombre_producto = input("Ingrese el nombre del producto: ")
        registro.precio = float(input("Ingrese el precio del producto: "))

        lista.append(registro)

    @staticmethod
    def verlista():
        print("Listado de productos agregados a la compra")
        print("--------------------------------------------------")

        for registro in lista:
            print(registro.codigo_barras, "-", registro.nombre_producto, "-", registro.precio)

        print("")
        print("")

    @staticmethod
    def subtotal():
        print("")

        suma_total = 0

        for registro in lista:
            suma_total += registro.precio

        print("El total de su compra es de ", "=", suma_total)

    @staticmethod
    def pago():
        print("Ingrese cuanto ha pagado el cliente: ")

        pago = float(input())
        suma_final = 0

        for registro in lista:
            suma_final += registro.precio

        if pago > suma_final:
            print("Su cambio es: ", (pago - suma_final))
        elif pago < suma_final:
            print("Le falta pagar: ", (suma_final - pago))
        elif pago == suma_final:
            print("Muchas gracias por su compra")
            print("--------------------------------------------------")

def menu():
    opcion = 0
    salir = 5

    while opcion != salir:
        print("--------------------------------------------------")
        print("Menu principal")
        print("--------------------------------------------------")
        print("1.- Registrar producto de la compra")
        print("2.- Ver lista de productos registrados")
        print("3.- Ver subtotal")
        print("4.- Ingresar pago del cliente")
        print("5.- Finalizar")
        print("--------------------------------------------------")
        opcion = input("Seleccione la accion a efectuar: ")
        print("--------------------------------------------------")

        if opcion == "1":
            cajaregistradora.registrarproducto()
        elif opcion == "2":
            cajaregistradora.verlista()
        elif opcion == "3":
            cajaregistradora.subtotal()
        elif opcion == "4":
            cajaregistradora.pago()
        elif opcion == "5":
            print("Muchas gracias por su compra")
            break

menu()
