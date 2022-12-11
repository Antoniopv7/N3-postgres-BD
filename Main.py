import psycopg2

#Conexion a la BD
connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='BDproyect'
    )

# Utilizacion del cursor
cursor=connection.cursor()

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
            print("A seleccionado la funcion de insertar datos")
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
                #sentencia
                sql = 'INSERT INTO cliente (cliente_id,nombre,apellido,rut,direccion,telefono) VALUES(%s,%s,%s,%s,%s,%s)'
                #solicitud de datos
                correcto=False
                cliente_id = 0
                while(not correcto):
                    try:
                        cliente_id=int(input("Ingrese el id del cliente: "))
                        correcto=True
                    except ValueError:
                        print("Error, introduzca un numero entero")
                nombre=input("Ingrese el nombre del cliente: ")
                apellido=input("Ingrese el apellido del cliente: ")
                rut=input("Ingrese el rut del cliente: ")
                direccion=input("Ingrese la direccion del cliente: ")
                a=False
                telefono = 0
                while(not a):
                    try:
                        telefono=int(input("Ingrese el numero telefonico del cliente: "))
                        a=True
                    except ValueError:
                        print("Error, introduzca un numero entero")
                #recoleccion de datos
                datos=(cliente_id,nombre,apellido,rut,direccion,telefono)
                #hacer uso del metodo execute
                cursor.execute(sql,datos)
                #guardar registro
                connection.commit()
                #registros insertados
                print('Datos insertados')

            elif x==2:
                print("")
            elif x==3:
                print("")
            elif x==4:
                print("")
            elif x==5:
                print("")
            elif x==6:
                print("")
            elif x==7:
                print("")
            elif x==8:
                print("")
            elif x==9:
                print("")
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
                sql='SELECT * FROM cliente'
                cursor.execute(sql)
                registro=cursor.fetchall()
                for fila in registro:
                    print(fila)
                print("")
            elif x == 2:
                lista=["Id","Nombre","Apellido","Rut","Sueldo"]
                print(lista)
                sql='SELECT * FROM empleado'
                cursor.execute(sql)
                registro=cursor.fetchall()
                for fila in registro:
                    print(fila)
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
        menu_anterior = False
        x = 0
        while not menu_anterior:
            print("A seleccionado la funcion de actualizar datos")
            print("En que tabla desea actualizar los datos:")
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
                print("")
            elif x==2:
                print("")
            elif x==3:
                print("")
            elif x==4:
                print("")
            elif x==5:
                print("")
            elif x==6:
                print("")
            elif x==7:
                print("")
            elif x==8:
                print("")
            elif x==9:
                print("")
            elif x==10:
                menu_anterior = True
                print("Volviendo al menu anterior")
                print("")
            else:
                print("seleccione una de las opciones")
    elif opcion == 4:
        menu_anterior = False
        x = 0
        while not menu_anterior:
            print("A seleccionado la funcion de Eliminar datos")
            print("En que tabla desea eliminar datos:")
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
                print("")
            elif x==2:
                print("")
            elif x==3:
                print("")
            elif x==4:
                print("")
            elif x==5:
                print("")
            elif x==6:
                print("")
            elif x==7:
                print("")
            elif x==8:
                print("")
            elif x==9:
                print("")
            elif x==10:
                menu_anterior = True
                print("Volviendo al menu anterior")
                print("")
            else:
                print("seleccione una de las opciones")
    elif opcion == 5:
        salir = True
    else:
        print ("Seleccione una de las opciones")

cursor.close()
connection.close()
print ("")
print ("Usted esta saliendo de la Base de datos")