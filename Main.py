import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import psycopg2

root = Tk()
root.title("Necu BD")

canvas = Canvas(root, height=600, width=1650)
canvas.pack()

frame = Frame()
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

# Funciones guardar

def Guardar_nuevo_cliente(nombre,apellido,rut,direccion,telefono):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO cliente (nombre,apellido,rut,direccion,telefono) VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(query, (nombre,apellido,rut,direccion,telefono))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_empleado(nombre,apellido,rut,sueldo):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO empleado (nombre,apellido,rut,sueldo) VALUES(%s,%s,%s,%s)'
    cursor.execute(query, (nombre,apellido,rut,sueldo))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_producto(nombre,descripcion,valor,stock):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO producto (nombre,descripcion,valor,stock) VALUES(%s,%s,%s,%s)'
    cursor.execute(query, (nombre,descripcion,valor,stock))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_proveedor(producto_id):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = sql='INSERT INTO proveedor (producto_id) VALUES(%s)'
    cursor.execute(query, (producto_id))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_boleta(cliente_id,detalle_venta,monto_neto,monto_iva,monto_total, fecha, cod_pago):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO boleta (cliente_id,detalle_venta,monto_neto,monto_iva,monto_total, fecha, cod_pago) VALUES(%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(query, (cliente_id,detalle_venta,monto_neto,monto_iva,monto_total, fecha, cod_pago))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_pedido(fecha, total, cliente_id):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO pedido (fecha, total, cliente_id) VALUES(%s,%s,%s)'
    cursor.execute(query, (fecha, total, cliente_id))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_despacho(fecha,hora_salida,hora_entrega,cliente_id,empleado_id):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO despacho (fecha,hora_salida,hora_entrega,cliente_id,empleado_id) VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(query, (fecha,hora_salida,hora_entrega,cliente_id,empleado_id))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_pago(estado):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO pago (estado) VALUES(%s)'
    cursor.execute(query, (estado))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

def Guardar_nuevo_factura(proveedor_id,producto_id,cod_pago,tipo_producto,monto_total):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor = conn.cursor()
    query = 'INSERT INTO factura (proveedor_id,producto_id,cod_pago,tipo_producto,monto_total) VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(query, (proveedor_id,producto_id,cod_pago,tipo_producto,monto_total))
    conn.commit()
    showinfo("Necu BD",
    "Datos Insertados")
    conn.close()

# Funciones guardar

# Funciones Mostrar

def mostrar_boletas(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM boleta ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_despachosxdespachador(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT nombre, COUNT(*) "Cantidad Despachos" FROM empleado JOIN despacho USING (empleado_id) GROUP BY nombre'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_ventas_dias(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT fecha, COUNT(*) "Ventas día" FROM pedido GROUP BY fecha ORDER BY fecha;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_productos(x): ##LISTADO PRODUCTOS Y CONTROL DE STOCK
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    #query= 'SELECT producto_id, stock, CASE when stock >= 10 then '' when stock < 5 then 'comprar a proveedor' else '' END Control_Stock FROM producto;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_cliente_frecuente(x): ##considerando que en necu con más de 10 compras se vuelve cliente frecuente
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'select count (b.cliente_id), cl.nombre from boleta b join cliente cl using (cliente_id)group by cl.nombre having count (b.cliente_id) > 10;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_boletasxcliente(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'select count (b.cliente_id), cl.nombre from boleta b join cliente cl using (cliente_id) group by cl.nombre;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_id_producto(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT producto_id,nombre FROM producto join proveedor using(producto_id) ORDER BY producto_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=4,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_id_producto2(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT producto_id,nombre FROM producto join proveedor using(producto_id) ORDER BY producto_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_id_proveedor(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT proveedor_id,nombre FROM producto join proveedor using(producto_id) ORDER BY producto_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=0)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_cod_pago(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT cod_pago FROM pago ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=2)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_id_cliente(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT cliente_id FROM cliente ORDER BY cliente_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_id_empleado(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT empleado_id FROM empleado ORDER BY empleado_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=0)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_clientes(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM cliente ORDER BY cliente_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def mostrar_empleados(v5):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM empleado ORDER BY empleado_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v5, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

# Funciones Mostrar

# Funciones Buscar

def buscar_cliente(cliente_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necu_db'
    )
    cursor = conn.cursor()
    query = 'SELECT * FROM cliente WHERE cliente_id=%s'
    cursor.execute(query, (cliente_id))

    row=cursor.fetchall()

    listbox = Listbox(frame, width=40, height=1)
    listbox.grid(columnspan=4,column=30)

    for x in row:
        listbox.insert(END,x)

    conn.commit()
    conn.close()

# Funciones Buscar

# Funciones Eliminar 

def elimnar_cliente(cliente_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necu_db'
    )
    cursor = conn.cursor()
    query ='DELETE FROM cliente WHERE cliente_id=%s'
    cursor.execute(query, (cliente_id))
    row=cursor.fetchall()
    conn.commit()
    conn.close()


# Funciones Eliminar

#Ventanas

def ventana2():
    v2=Toplevel()
    v2.geometry("300x200")
    v2.title("Insertar datos")
    espacio1=Label(v2,text="Cliente").grid(row=0,column=0)
    label1 = Label(v2,text="Ingrese Nombre: ").grid(row=1,column=0)
    label2 = Label(v2,text="Ingrese apellido: ").grid(row=2,column=0)
    label3 = Label(v2,text="Ingrese rut: ").grid(row=3,column=0)
    label4 = Label(v2,text="Ingrese direccion: ").grid(row=4,column=0)
    label5 = Label(v2,text="Ingrese telefono: ").grid(row=5,column=0)
    espacio2 = Label(v2).grid(row=6,column=0)
    espacio3 = Label(v2).grid(row=7,column=0)
    espacio4 = Label(v2).grid(row=0,column=1)
    espacio5 = Label(v2).grid(row=6,column=1)
    espacio6 = Label(v2).grid(row=7,column=1)
    entry_nom = Entry(v2)
    entry_nom.grid(row=1,column=1)
    entry_ape = Entry(v2)
    entry_ape.grid(row=2,column=1)
    entry_rut = Entry(v2)
    entry_rut.grid(row=3,column=1)
    entry_dir = Entry(v2)
    entry_dir.grid(row=4,column=1)
    entry_tel = Entry(v2)
    entry_tel.grid(row=5,column=1)  

    boton_guardar_cliente = Button(v2,text="Guardar cliente",command=lambda:Guardar_nuevo_cliente(
        entry_nom.get(),
        entry_ape.get(),
        entry_rut.get(),
        entry_dir.get(),
        entry_tel.get()
    ))
    boton_guardar_cliente.grid(row=6,column=1)

def ventana3():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Lista de clientes")
    labelv3 = Label(v3,text="| Id || Nombre || Apellido || Rut || Direccion || Telefono |").grid(row=0,column=0)
    mostrar_clientes(v3)

def ventana4():
    v4 = Toplevel()
    v4.geometry("300x200")
    v4.title("Insertar Datos")
    espacio1=Label(v4,text="Empleado").grid(row=0,column=0)
    label1 = Label(v4,text="Ingrese Nombre: ").grid(row=1,column=0)
    label2 = Label(v4,text="Ingrese Apellido: ").grid(row=2,column=0)
    label3 = Label(v4,text="Ingrese Rut: ").grid(row=3,column=0)
    label4 = Label(v4,text="Ingrese Sueldo: ").grid(row=4,column=0)
    espacio2 = Label(v4).grid(row=6,column=0)
    espacio3 = Label(v4).grid(row=7,column=0)
    espacio4 = Label(v4).grid(row=0,column=1)
    espacio5 = Label(v4).grid(row=6,column=1)
    espacio6 = Label(v4).grid(row=7,column=1)
    entry_nom = Entry(v4)
    entry_nom.grid(row=1,column=1)
    entry_ape = Entry(v4)
    entry_ape.grid(row=2,column=1)
    entry_rut = Entry(v4)
    entry_rut.grid(row=3,column=1)
    entry_sue = Entry(v4)
    entry_sue.grid(row=4,column=1)

    boton_guardar_empleado = Button(v4,text="Guardar Empleado",command=lambda:Guardar_nuevo_empleado(
        entry_nom.get(),
        entry_ape.get(),
        entry_rut.get(),
        entry_sue.get()
        ))
    boton_guardar_empleado.grid(row=5,column=1)

def ventana5():
    v5 = Toplevel()
    v5.geometry("300x200")
    v5.title("Lista de clientes")
    labelv5 = Label(v5,text="| Id || Nombre || Apellido || Rut || Sueldo |").grid(row=0,column=0)
    mostrar_empleados(v5)

def ventana6():
    v6 = Toplevel()
    v6.geometry("300x200")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Producto").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Nombre: ").grid(row=1,column=0)
    label2 = Label(v6,text="Ingrese Descripcion: ").grid(row=2,column=0)
    label3 = Label(v6,text="Ingrese Valor: ").grid(row=3,column=0)
    label4 = Label(v6,text="Ingrese Stock: ").grid(row=4,column=0)
    espacio2 = Label(v6).grid(row=6,column=0)
    espacio3 = Label(v6).grid(row=7,column=0)
    espacio4 = Label(v6).grid(row=0,column=1)
    espacio5 = Label(v6).grid(row=6,column=1)
    espacio6 = Label(v6).grid(row=7,column=1)
    entry_nom = Entry(v6)
    entry_nom.grid(row=1,column=1)
    entry_des = Entry(v6)
    entry_des.grid(row=2,column=1)
    entry_val = Entry(v6)
    entry_val.grid(row=3,column=1)
    entry_sto = Entry(v6)
    entry_sto.grid(row=4,column=1)

    boton_guardar_producto = Button(v6,text="Guardar Producto",command=lambda:Guardar_nuevo_producto(
        entry_nom.get(),
        entry_des.get(),
        entry_val.get(),
        entry_sto.get()
        ))
    boton_guardar_producto.grid(row=5,column=1)

def ventana7():
    v6 = Toplevel()
    v6.geometry("300x200")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Proveedor").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id_producto: ").grid(row=1,column=0)
    
    id_prod = Entry(v6)
    id_prod.grid(row=1,column=1)
    mostrar_id_producto(v6)


    boton_guardar = Button(v6,text="Guardar Proveedor",command=lambda:Guardar_nuevo_proveedor(id_prod.get()))
    boton_guardar.grid(row=2,column=1)

def ventana8():
    v6 = Toplevel()
    v6.geometry("400x600")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Factura").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id del proveedor: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese Id del producto: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese el codigo del pago: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese el tipo de producto: ").grid(row=4,column=0)
    label1 = Label(v6,text="Ingrese el monto total: ").grid(row=5,column=0)
    proveedor_id = Entry(v6)
    proveedor_id.grid(row=1,column=1)
    producto_id = Entry(v6)
    producto_id.grid(row=2,column=1)
    cod_pago = Entry(v6)
    cod_pago.grid(row=3,column=1)
    tipo_producto = Entry(v6)
    tipo_producto.grid(row=4,column=1)
    monto_total = Entry(v6)
    monto_total.grid(row=5,column=1)
    label1 = Label(v6,text="| Id_producto || Nombre |").grid(row=9,column=1)
    mostrar_id_producto2(v6)
    label1 = Label(v6,text="| Id_provedor || Nombre |").grid(row=9,column=0)
    mostrar_id_proveedor(v6)
    label1 = Label(v6,text="| Cod_pago |").grid(row=9,column=2)
    mostrar_cod_pago(v6)


    boton_guardar = Button(v6,text="Guardar Factura",command=lambda:Guardar_nuevo_factura(
        proveedor_id.get(), 
        producto_id.get(), 
        cod_pago.get(), 
        tipo_producto.get(), 
        monto_total.get()
        ))
    boton_guardar.grid(row=6,column=1)

def ventana9():
    v6 = Toplevel()
    v6.geometry("400x300")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Boleta").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id_Cliente: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese Detalle de la venta: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese Monto neto: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese Monto iva: ").grid(row=4,column=0)
    label1 = Label(v6,text="Ingrese Monto total: ").grid(row=5,column=0)
    label1 = Label(v6,text="Ingrese Fecha: ").grid(row=6,column=0)
    label1 = Label(v6,text="Ingrese Codigo del pago: ").grid(row=7,column=0)
    
    cliente_id = Entry(v6)
    cliente_id.grid(row=1,column=1)
    detalle_venta = Entry(v6)
    detalle_venta.grid(row=2,column=1)
    monto_neto = Entry(v6)
    monto_neto.grid(row=3,column=1)
    monto_iva = Entry(v6)
    monto_iva.grid(row=4,column=1)
    monto_total = Entry(v6)
    monto_total.grid(row=5,column=1)
    fecha = Entry(v6)
    fecha.grid(row=6,column=1)
    cod_pago = Entry(v6)
    cod_pago.grid(row=7,column=1)

    label1= Label(v6,text="| Cod_pago |").grid(row=9,column=2)
    label1= Label(v6,text="| Id_cliente |").grid(row=9,column=1)
    mostrar_cod_pago(v6)
    mostrar_id_cliente(v6)
    
    boton_guardar = Button(v6,text="Guardar Boleta",command=lambda:Guardar_nuevo_boleta(
        cliente_id.get(),
        detalle_venta.get(),
        monto_neto.get(),
        monto_iva.get(),
        monto_total.get(), 
        fecha.get(), 
        cod_pago.get()
        ))
    boton_guardar.grid(row=8,column=1)

def ventana10():
    v6 = Toplevel()
    v6.geometry("300x200")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="pago").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Estado del pago: ").grid(row=1,column=0)
    
    estado = Entry(v6)
    estado.grid(row=1,column=1)
    
    boton_guardar = Button(v6,text="Guardar Pago",command=lambda:Guardar_nuevo_pago(estado.get()))
    boton_guardar.grid(row=8,column=1)

def ventana11():
    v6 = Toplevel()
    v6.geometry("400x300")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Pedido").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id la fecha del pedido: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese el monto total del pedido: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese el ID del cliente : ").grid(row=3,column=0)   
    fecha = Entry(v6)
    fecha.grid(row=1,column=1)
    total = Entry(v6)
    total.grid(row=2,column=1)
    cliente_id = Entry(v6)
    cliente_id.grid(row=3,column=1)
    label1= Label(v6,text="| Id_cliente |").grid(row=9,column=1)
    mostrar_id_cliente(v6)
    
    boton_guardar = Button(v6,text="Guardar Pedido",command=lambda:Guardar_nuevo_pedido(
        fecha.get(), 
        total.get(), 
        cliente_id.get()))
    boton_guardar.grid(row=4,column=1)

def ventana12():
    v6 = Toplevel()
    v6.geometry("450x300")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Despacho").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese la fecha del despacho: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese la hora de salida del despacho: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese la hora de entrega del despacho: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese el id del cliente asociado al despacho: ").grid(row=4,column=0)
    label1 = Label(v6,text="Ingrese el id del empleado asociado al despacho: ").grid(row=5,column=0)
    
    fecha = Entry(v6)
    fecha.grid(row=1,column=1)
    hora_salida = Entry(v6)
    hora_salida.grid(row=2,column=1)
    hora_entrega = Entry(v6)
    hora_entrega.grid(row=3,column=1)
    cliente_id = Entry(v6)
    cliente_id.grid(row=4,column=1)
    empleado_id = Entry(v6)
    empleado_id.grid(row=5,column=1)
    mostrar_id_cliente(v6)
    mostrar_id_empleado(v6)
    label1 = Label(v6,text="| Id_cliente |").grid(row=7,column=1)
    label1 = Label(v6,text="| Id_empleado |").grid(row=7,column=0)
    
    boton_guardar = Button(v6,text="Guardar Despacho",command=lambda:Guardar_nuevo_despacho(
        fecha.get(), 
        hora_salida.get(), 
        hora_entrega.get(), 
        cliente_id.get(), 
        empleado_id.get()
        ))
    boton_guardar.grid(row=6,column=1)

def ventana13():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Despachos por despachador")
    labelv3 = Label(v3,text="| Nombre || Cantidad de despachos |").grid(row=0,column=0)
    mostrar_despachosxdespachador(v3)

def ventana14():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Ventas por dia")
    labelv3 = Label(v3,text="| Fecha || Cantidad de ventas |").grid(row=0,column=0)
    mostrar_ventas_dias(v3)

def ventana15():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Productos y manutencion")
    labelv3 = Label(v3,text="| Id_producto || Nombre || Stock |").grid(row=0,column=0)
    mostrar_productos(v3)

def ventana16():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Clientes frecuentes")
    labelv3 = Label(v3,text="| Cantidad de compras || Nombre |").grid(row=0,column=0)
    mostrar_cliente_frecuente(v3)

def ventana17():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Listado de boletas")
    labelv3 = Label(v3,text="| Client id || Detalle venta || Monto neto || Monto iva || Monto total || fecha || Codigo de pago |").grid(row=0,column=0)
    mostrar_boletas(v3)

def venta18():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Listado de boletas")
    labelv3 = Label(v3,text="Cliente").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el ID cliente a eliminar").grid(row=0,column=1)
    id_cliente= Entry(v3).grid(row=1,column=1)

#Ventanas  

#label frame
cliente = Label(frame,text="Cliente").grid(row=0,column=0)
espacio = Label(frame).grid(row=0,column=1)
espacio = Label(frame).grid(row=0,column=2)
espacio = Label(frame).grid(row=1,column=1)
espacio = Label(frame).grid(row=1,column=2)
empleado = Label(frame,text="Empleado").grid(row=0,column=3)
espacio = Label(frame).grid(row=0,column=4)
espacio = Label(frame).grid(row=0,column=5)
espacio = Label(frame).grid(row=1,column=4)
espacio = Label(frame).grid(row=1,column=5)
producto = Label(frame,text="Producto").grid(row=0,column=6)
espacio = Label(frame).grid(row=0,column=7)
espacio = Label(frame).grid(row=0,column=8)
espacio = Label(frame).grid(row=1,column=7)
espacio = Label(frame).grid(row=1,column=8)
Proveedor = Label(frame,text="Proveedor").grid(row=0,column=9)
espacio = Label(frame).grid(row=0,column=10)
espacio = Label(frame).grid(row=0,column=11)
espacio = Label(frame).grid(row=1,column=10)
espacio = Label(frame).grid(row=1,column=11)
Factura = Label(frame,text="Factura").grid(row=0,column=12)
espacio = Label(frame).grid(row=0,column=13)
espacio = Label(frame).grid(row=0,column=14)
espacio = Label(frame).grid(row=1,column=13)
espacio = Label(frame).grid(row=1,column=14)
Boleta = Label(frame,text="Boleta").grid(row=0,column=15)
espacio = Label(frame).grid(row=0,column=16)
espacio = Label(frame).grid(row=1,column=17)
espacio = Label(frame).grid(row=1,column=16)
espacio = Label(frame).grid(row=1,column=17)
Pago = Label(frame,text="Pago").grid(row=0,column=18)
espacio = Label(frame).grid(row=0,column=19)
espacio = Label(frame).grid(row=1,column=20)
espacio = Label(frame).grid(row=1,column=19)
espacio = Label(frame).grid(row=1,column=20)
Pedido = Label(frame,text="Pedido").grid(row=0,column=21)
espacio = Label(frame).grid(row=0,column=22)
espacio = Label(frame).grid(row=1,column=23)
espacio = Label(frame).grid(row=1,column=22)
espacio = Label(frame).grid(row=1,column=23)
Despacho = Label(frame,text="Despacho").grid(row=0,column=24)
espacio = Label(frame).grid(row=2,column=0)
espacio = Label(frame).grid(row=2,column=3)
espacio = Label(frame).grid(row=2,column=24)
espacio = Label(frame).grid(row=2,column=21)
espacio = Label(frame).grid(row=2,column=12)
espacio = Label(frame).grid(row=2,column=18)
espacio = Label(frame).grid(row=2,column=15)
espacio = Label(frame).grid(row=4,column=0)
#label frame

#button frame
boton_v2 = Button(frame, text="Insertar cliente",command=lambda:ventana2()).grid(row=1,column=0)
boton_v4 = Button(frame, text="Insertar empleado",command=lambda:ventana4()).grid(row=1,column=3)
boton_v6 = Button(frame, text="Insertar Producto",command=lambda:ventana6()).grid(row=1,column=6)
boton_v7 = Button(frame, text="Insertar Proveedor",command=lambda:ventana7()).grid(row=1,column=9)
boton_v8 = Button(frame, text="Insertar Factura",command=lambda:ventana8()).grid(row=1,column=12)
boton_v9 = Button(frame, text="Insertar Boleta",command=lambda:ventana9()).grid(row=1,column=15)
boton_v10 = Button(frame, text="Insertar Pago",command=lambda:ventana10()).grid(row=1,column=18)
boton_v11 = Button(frame, text="Insertar Pedido",command=lambda:ventana11()).grid(row=1,column=21)
boton_v12 = Button(frame, text="Insertar Despacho",command=lambda:ventana12()).grid(row=1,column=24)


boton_v3 = Button(frame, text="Mostrar clientes",command=lambda:ventana3()).grid(row=3,column=0)
boton_v5 = Button(frame, text="Mostrar empleados",command=lambda:ventana5()).grid(row=3,column=3)
boton_v13 = Button(frame, text="Mostrar Despachos por despachador",command=lambda:ventana13()).grid(row=3,column=24)
boton_v14 = Button(frame, text="Mostrar Ventas por dia",command=lambda:ventana14()).grid(row=3,column=21)
boton_v15 = Button(frame, text="Mostrar Productos y manutencion",command=lambda:ventana15()).grid(row=3,column=12)
boton_v16 = Button(frame, text="Cliente Frecuente",command=lambda:ventana16()).grid(row=3,column=18)
boton_v17 = Button(frame, text="Mostrar Listado de boletas",command=lambda:ventana17()).grid(row=3,column=15)
boton_v18 = Button(frame, text="Eliminar Cliente",command=lambda:ventana18()).grid(row=5,column=0)
#button frame

root.mainloop()