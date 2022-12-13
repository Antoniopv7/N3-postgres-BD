import psycopg2

#Conexion a la BD
connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='NecuDB'
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
                sql='INSERT INTO cliente (nombre,apellido,rut,direccion,telefono) VALUES(%s,%s,%s,%s,%s)'
                #solicitud de datos
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
                datos=(nombre,apellido,rut,direccion,telefono)
                #hacer uso del metodo execute
                cursor.execute(sql,datos)
                #guardar registro
                connection.commit()
                #registros insertados
                print('Datos insertados')
                print("")
            elif x==2:
                sql='INSERT INTO empleado (nombre,apellido,rut,sueldo) VALUES(%s,%s,%s,%s)'
                nombre=input("Ingrese el nombre del empleado: ")
                apellido=input("Ingrese el apellido del empleado: ")
                rut=input("Ingrese el rut del empleado: ")
                a=False
                sueldo=0
                while(not a):
                    try:
                        sueldo=int(input("Ingrese el sueldo del empleado: "))
                        a=True
                    except ValueError:
                        print("Error, Ingrese un numero porfavor")
                datos=(nombre,apellido,rut,sueldo)
                cursor.execute(sql,datos)
                connection.commit()
                print("Datos insertados")
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
                sql='SELECT * FROM cliente ORDER BY cliente_id'
                cursor.execute(sql)
                registro=cursor.fetchall()
                for fila in registro:
                    print(fila)
                print("")
            elif x == 2:
                lista=["Id","Nombre","Apellido","Rut","Sueldo"]
                print(lista)
                sql='SELECT * FROM empleado ORDER BY empleado_id'
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
                sql='UPDATE cliente SET nombre=%s,apellido=%s,rut=%s,direccion=%s,telefono=%s WHERE cliente_id=%s'
                sql_id='SELECT cliente_id FROM cliente ORDER BY cliente_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                id_cliente=input(f"Seleccione uno de los siguiente ID a modificar {registro}: ")
                nombre=input("Ingrese nombre: ")
                apellido=input("Ingrese apellido: ")
                rut=input("Ingrese rut: ")
                direccion=input("Ingrese direccion: ")
                a=False
                telefono=0
                while(not a):
                    try:
                        telefono=int(input("Ingrese el sueldo del empleado: "))
                        a=True
                    except ValueError:
                        print("ERROR, Ingrese un numero telefonico correcto")
                datos=(nombre,apellido,rut,direccion,telefono,id_cliente)
                cursor.execute(sql,datos)
                connection.commit()
                print("Datos actualizados correctamente")
                print("")    
            elif x==2:
                sql='UPDATE empleado SET nombre=%s,apellido=%s,rut=%s,sueldo=%s WHERE empleado_id=%s'
                sql_id='SELECT empleado_id FROM empleado ORDER BY empleado_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                id_empleado=input(f"Seleccione uno de los siguiente ID a modificar {registro}: ")
                nombre=input("Ingrese nombre: ")
                apellido=input("Ingrese apellido: ")
                rut=input("Ingrese rut: ")
                a=False
                sueldo=0
                while(not a):
                    try:
                        sueldo=int(input("Ingrese el sueldo del empleado: "))
                        a=True
                    except ValueError:
                        print("Error, Ingrese un numero porfavor")
                datos=(nombre,apellido,rut,sueldo,id_empleado)
                cursor.execute(sql,datos)
                connection.commit()
                print("Datos actualizados correctamente")
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
                sql='DELETE FROM cliente WHERE cliente_id=%s'
                sql_id='SELECT cliente_id FROM cliente ORDER BY cliente_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                cliente_id=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,cliente_id)
                connection.commit()
                print("Registro eliminado")
                print("")
            elif x==2:
                sql='DELETE FROM empleado WHERE empleado_id=%s'
                sql_id='SELECT empleado_id FROM empleado ORDER BY empleado_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                empleado_id=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,empleado_id)
                connection.commit()
                print("Registro eliminado")
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