import psycopg2

connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='BDproyect'
    )

def listado_de_clientes():
    cursor=connection.cursor()   
    cursor.execute("SELECT * FROM cliente")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

def listado_despachadores():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM empleado")
    rows=cursor.fetchall()
    for row in rows:
        print(row)