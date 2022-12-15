import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import psycopg2

root = Tk()
root.title("Necu BD")

canvas = Canvas(root, height=600, width=800)
canvas.pack()

frame = Frame()
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

# Funciones

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

#Funciones

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
    labelv3 = Label(v3,text="| Id | Nombre | Apellido | Rut | Direccion | Telefono |").grid(row=0,column=0)
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
    labelv5 = Label(v5,text="| Id | Nombre | Apellido | Rut | Sueldo |").grid(row=0,column=0)
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

#Ventanas

#label frame
cliente = Label(frame,text="Cliente").grid(row=0,column=0)
espacio1 = Label(frame).grid(row=0,column=1)
espacio1_2 = Label(frame).grid(row=0,column=2)
espacio2 = Label(frame).grid(row=1,column=1)
espacio2_2 = Label(frame).grid(row=1,column=2)
empleado = Label(frame,text="Empleado").grid(row=0,column=3)
espacio3 = Label(frame).grid(row=0,column=4)
espacio3_2 = Label(frame).grid(row=0,column=5)
espacio4 = Label(frame).grid(row=1,column=4)
espacio4_2 = Label(frame).grid(row=1,column=5)
producto = Label(frame,text="Producto").grid(row=0,column=6)
#label frame

#button frame
boton_v2 = Button(frame, text="Insertar cliente",command=lambda:ventana2()).grid(row=1,column=0)
boton_v3 = Button(frame, text="Mostrar clientes",command=lambda:ventana3()).grid(row=2,column=0)
boton_v4 = Button(frame, text="Insertar empleado",command=lambda:ventana4()).grid(row=1,column=3)
boton_v5 = Button(frame, text="Mostrar empleados",command=lambda:ventana5()).grid(row=2,column=3)
boton_v6 = Button(frame, text="Insertar Producto",command=lambda:ventana6()).grid(row=1,column=6)
boton_v7 = Button(frame, text="Mostrar")
#button frame

root.mainloop()