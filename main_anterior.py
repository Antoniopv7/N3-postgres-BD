import psycopg2

#Conexion a la BD
connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
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
                n=False
                while(not n):
                    nombre=input("Ingrese el nombre del cliente: ")
                    if nombre != "":
                        n=True
                    else:
                        print("")
                        print("Error rellene la casilla con los datos pedidos")
                a=False
                while(not a):
                    apellido=input("Ingrese el apellido del cliente: ")
                    if apellido != "":
                        a=True
                    else:
                        print("")
                        print("Error rellene la casilla con los datos pedidos")
                r=False
                while(not r):
                    rut=input("Ingrese el rut del cliente: ")
                    if rut != "":
                        r=True
                    else:
                        print("")
                        print("Error rellene la casilla con los datos pedidos")
                d=False
                while(not d):
                    direccion=input("Ingrese la direccion del cliente: ")
                    if direccion != "":
                        d=True
                    else:
                        print("")
                        print("Error Rellene la casilla con los datos pedidos")
                t=False
                telefono = 0
                while(not t):
                    try:
                        telefono=int(input("Ingrese el numero telefonico del cliente: "))
                        t=True
                    except ValueError:
                        print("Error, introduzca un numero telefonico valido porfavor")
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
                n=False
                while(not n):
                    nombre=input("Ingrese el nombre del empleado: ")
                    if nombre != "":
                        n=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                a=False
                while(not a):
                    apellido=input("Ingrese el apellido del empleado: ")
                    if apellido != "":
                        a=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                r=False
                while(not r):
                    rut=input("Ingrese el rut del empleado: ")
                    if nombre != "":
                        n=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                a=False
                sueldo=0
                while(not a):
                    try:
                        sueldo=int(input("Ingrese el sueldo del empleado: "))
                        a=True
                    except ValueError:
                        print("Error, ingrese correctamente el sueldo")
                datos=(nombre,apellido,rut,sueldo)
                cursor.execute(sql,datos)
                connection.commit()
                print("Datos insertados")
                print("")

            elif x==3:
                sql='INSERT INTO despacho (fecha,hora_salida,hora_entrega,cliente_id,empleado_id) VALUES(%s,%s,%s,%s,%s)'
                f=False
                while(not f):
                    fecha=input("Ingrese la fecha del despacho: ")
                    if fecha != "":
                        f=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                h_s=False
                while(not h_s):
                    hora_salida=input("Ingrese la hora de salida del despacho: ")
                    if hora_salida != "":
                        h_s=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                h_e=False
                while(not h_e):
                    hora_entrega=input("Ingrese la hora de entrega del despacho: ")
                    if hora_entrega != "":
                        h_e=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                sql_id_cliente = 'SELECT cliente_id from cliente order by cliente_id'
                cursor.execute(sql_id_cliente)
                cliente_registro=cursor.fetchall()
                c=False
                while(not c):
                    try:
                        cliente_id=int(input(f"Ingrese el id del cliente asociado al despacho {cliente_registro}: "))
                        c = True
                    except ValueError:
                        print("Error, Ingrese un ID correcto")
                sql_id_empleado = 'SELECT empleado_id from empleado order by empleado_id'
                cursor.execute(sql_id_empleado)
                empleado_registro=cursor.fetchall()
                e=False
                empleado_id=0
                while(not e):
                    try:
                        empleado_id=int(input(f"Ingrese el id de empleado asociado al despacho {empleado_registro}: "))
                        e = True
                    except ValueError:
                        print("Error, Ingrese un id correcto")
                datos=(fecha,hora_salida,hora_entrega,cliente_id,empleado_id)
                cursor.execute(sql,datos)
                connection.commit()
                print("Datos insertados")
                print("")

            elif x==4:
                sql= 'INSERT INTO factura (proveedor_id,producto_id,cod_pago,tipo_producto,monto_total) VALUES(%s,%s,%s,%s,%s)'
                sql_id_proveedor= 'SELECT proveedor_id from proveedor order by proveedor_id'
                cursor.execute(sql_id_proveedor)
                registro_proveedor=cursor.fetchall()
                p=False
                while(not p):
                    try:
                        proveedor_id=int(input(f"Ingrese el id de proveedor asociado a la factura {registro_proveedor}: "))
                        p=True
                    except ValueError:
                        print("")
                        print("Error, Ingrese un id correcto")
                sql_id_producto= 'SELECT producto_id from producto order by producto_id'
                cursor.execute(sql_id_producto)
                registro_producto=cursor.fetchall()
                pd=False
                while(not pd):
                    try:
                        producto_id=int(input(f"Ingrese el id de producto asociado a la factura {registro_producto}: "))
                        pd=True
                    except ValueError:
                        print("")
                        print("Error, Ingrese un id correcto")
                sql_cod_pago= 'SELECT cod_pago from pago order by cod_pago'
                cursor.execute(sql_cod_pago)
                registro_pago=cursor.fetchall()
                c=False
                while(not c):
                    try:
                        cod_pago=int(input(f"Ingrese el codigo de pago asociado a la factura {registro_pago}: "))
                        c=True
                    except ValueError:
                        print("")
                        print("Error, Ingrese un id correcto")
                sql_tipo_producto='SELECT producto_id,nombre from producto order by nombre'
                cursor.execute(sql_tipo_producto)
                registro_tp=cursor.fetchall()
                tp=False
                while(not tp):
                    print(f"dependiendo del id producto asociado a la factura {registro_tp}")
                    tipo_producto=input("Ingrese el tipo de producto asociado a la factura: ")
                    if tipo_producto != "":
                        tp=True
                    else:
                        print("")
                        print("Error rellene esta casilla con los datos pedidos")
                mt=False
                while(not mt):
                    try:
                        monto_total=int(input("Ingrese el monto total asociado a la factura: "))
                        mt=True
                    except ValueError:
                        print("")
                        print("Ingrese un monto valido porfavor")
                datos=(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total)
                cursor.execute(sql,datos)
                connection.commit()
                print("Datos insertados")
                print("")

            elif x==5:
                sql='INSERT INTO pago (estado) VALUES(%s)'
                e=False
                while(not e):
                    estado=input("Ingrese el estado del pago Selecionando [REALIZADO] si el pago esta hecho o [EN ESPERA] si el pago esta pendiente: ")
                    if estado == "REALIZADO":
                        e=True
                    elif estado == "EN ESPERA":
                        e=True     
                    else:
                        print("porfavor ingrese los datos que se le solicitan")
                cursor.execute(sql,estado)
                connection.commit()
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
            print("4. Tabla pago")
            print("5. Tabla producto")
            print("6. Tabla proveedor")
            print("7. Tabla pedido")
            print("8. Volver al menu anterior")
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
            print("4. Tabla pago")
            print("5. Tabla producto")
            print("6. Tabla proveedor")
            print("7. Tabla pedido")
            print("8. Volver al menu anterior")
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
                sql='DELETE FROM despacho WHERE despacho_id=%s'
                sql_id='SELECT despacho_id FROM despacho ORDER BY despacho_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                despacho_id=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,despacho_id)
                connection.commit()
                print("Registro eliminado")
                print("")

            elif x==4:
                sql='DELETE FROM pago WHERE cod_pago=%s'
                sql_id='SELECT cod_pago FROM pago ORDER BY cod_pago'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                pago_id=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,pago_id)
                connection.commit()
                print("Registro eliminado")
                print("")

            elif x==5:
                sql='DELETE FROM producto WHERE producto_id=%s'
                sql_id='SELECT producto_id FROM producto ORDER BY producto_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                producto_id=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,producto_id)
                connection.commit()
                print("Registro eliminado")
                print("")

            elif x==6:
                sql='DELETE FROM proveedor WHERE proveedor_id=%s'
                sql_id='SELECT proveedor_id FROM proveedor ORDER BY proveedor_id'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                proveedor_id=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,proveedor_id)
                connection.commit()
                print("Registro eliminado")
                print("")

            elif x==7:
                sql='DELETE FROM pedido WHERE codigo=%s'
                sql_id='SELECT codigo FROM pedido ORDER BY codigo'
                cursor.execute(sql_id)
                registro=cursor.fetchall()
                codigo=input(f"Ingrese el id del registro a eliminar {registro}: ")
                cursor.execute(sql,codigo)
                connection.commit()
                print("Registro eliminado")
                print("")

            elif x==8:
                menu_anterior = True
                print("Volviendo al menu anterior")
                print("")

            else:
                print("seleccione una de las opciones")

    elif opcion == 5:
        salir = True

    else:
        print ("Seleccione una de las opciones")

print ("")
print ("Usted esta saliendo de la Base de datos")