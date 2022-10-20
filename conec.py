import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port= 3306,
        user = 'root',
        password = "Octi1234",
        db = 'disqueria'
    )

    if conexion.is_connected():
        print("Conexión Sastifactoria...")

        Cursor = conexion.cursor()

        Cursor.execute("select * from tema")
        lista = Cursor.fetchall()

        for dato in lista:
            print(dato)


except:
    
    print("NO SE PUDO REALIZAR LA CONEXION CON LA BASE DE DATOS, INTENTAR NUEVAMENTE....")

finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexion Cerrada")


