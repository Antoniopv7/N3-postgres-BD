import psycopg2
import Libreria as li

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Seleccione una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

salir = False
opcion = 0

while not salir:
    print("Bienvenido a la Base de datos de Necu")
    print("Que desea hacer:")
    print("")
    print("1. Insertar Datos")
    print("2. Mostrar Datos")
    print("3. Actualizar Datos")
    print("4. Borrar Datos")
    print("5. Salir")
    print("")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        menu_anterior = False
        x = 0
        while not menu_anterior:
            print("A seleccionado la funcion de Insertar datos")
            print("En que tabla desea insertar datos:")
            print("")
            print("1. Tabla cliente")
            print("2. Tabla empleado")
            print("3. Tabla despacho")
            print("4. Tabla factura")
            print("5. Tabla pago")
            print("6. Tabla boleta")
            print("7. Tabla producto")
            print("8. Tabla proveedor")
            print("9. Tabla pedido")
            print("10. Volver al menu anterior")
            print("")

            x = pedirNumeroEntero()

            if x==1:

            elif x==2:

            elif x==3:

            elif x==4:

            elif x==5:

            elif x==6:

            elif x==7:

            elif x==8:

            elif x==9:

            elif x==10:
                menu_anterior = True
                print("Volviendo al menu anterior")
                print("")
            else:
                print("seleccione una de las opciones")
        
    elif opcion == 2:
        menu_anterior = False
        x = 0
        while not menu_anterior:
            print("A seleccionado la funcion de mostrar datos")
            print("que registros desea ver:")
            print("")
            print("1. Listado de clientes")
            print("2. Listado de despachadores")
            print("3. Listado de despachos por despachador")
            print("4. Listado de ventas por dia")
            print("5. Listado de clientes frecuentes")
            print("6. Listado de clientes boletas")
            print("7. Listado y manutencion de productos")
            print("8. Volver al menu anterior")
            print("")
            
            x = pedirNumeroEntero()

            if x == 1:
                lista=["Id","Nombre","Apellido","Rut","Direccion","Telefono"]
                print(lista)
                li.listado_de_clientes()
                print("")
            elif x == 2:
                lista=["Id","Nombre","Apellido","Rut","Sueldo"]
                print("lista")
                li.listado_despachadores()
                print("")
            elif x == 3:
                print("")
            elif x == 4:
                print("")
            elif x == 5:
                print("")
            elif x == 6:
                print("")
            elif x == 7:
                print("")
            elif x == 8:
                menu_anterior = True
                print("Volviendo al menu anterior")
                print("")      
            else:
                print("seleccione una de las opciones")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        salir = True
    else:
        print ("Seleccione una de las opciones")

print ("")
print ("Usted esta saliendo de la Base de datos")