import tkinter as tk
from tkinter import *
import psycopg2

root=Tk()
root.title("Necu BD")
root.geometry("800x600")

# Funciones
def Guardar_nuevo_cliente(e1,e2,e3,e4,e5):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'INSERT INTO cliente (nombre,apellido,rut,direccion,telefono) VALUES(%s,%s,%s,%s,%s)'
    int(e5)
    cursor.execute(query, (e1,e2,e3,e4,e5))
    print("Datos guardados")
    conn.commit()
    conn.close()
    mostrar_clientes()

def mostrar_clientes():
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

    listbox=Listbox(root, width=40, height=10)
    listbox.grid(column= 1, columnspan=4)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def buscar_cliente(cliente_id):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necu_db'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM cliente WHERE cliente_id=%s'
    cursor.execute(query, (cliente_id))

    row=cursor.fetchall()

    listbox=Listbox(root, width=40, height=1)
    listbox.grid(columnspan=4,column=30)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()
# Funciones

# agrega nombre del nuevo cliente
x=Label(root,text="Cliente").grid(row=0,column=0)
l1=Label(root,text="Ingrese Nombre: ").grid(row=1,column=0)
e1= Entry(root).grid(row=1,column=1)
l2=Label(root,text="Ingrese apellido: ").grid(row=2,column=0)
e2= Entry(root).grid(row=2,column=1)
l3=Label(root,text="Ingrese rut: ").grid(row=3,column=0)
e3= Entry(root).grid(row=3,column=1)
l4=Label(root,text="Ingrese direccion: ").grid(row=4,column=0)
e4= Entry(root).grid(row=4,column=1)
l5=Label(root,text="Ingrese telefono: ").grid(row=5,column=0)
e5= Entry(root).grid(row=5,column=1)
x=Label(root).grid(row=6,column=0)
x=Label(root).grid(row=7,column=0)
x=Label(root).grid(row=0,column=1)
x=Label(root).grid(row=1,column=1)
x=Label(root).grid(row=2,column=1)
x=Label(root).grid(row=3,column=1)
x=Label(root).grid(row=4,column=1)
x=Label(root).grid(row=5,column=1)
x=Label(root).grid(row=6,column=1)
x=Label(root).grid(row=7,column=1)

boton = Button(root, text="Agregar Cliente",command=lambda:Guardar_nuevo_cliente(get.e1))
boton.grid(row=2, column=2, sticky=W+E)


mostrar_clientes()

root.mainloop()