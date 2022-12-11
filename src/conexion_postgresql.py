import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='BDproyect'
    )

    print("Conexion exitosa")
    cursor=connection.cursor()   
    cursor.execute("SELECT * FROM cliente")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)