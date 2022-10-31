import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='maytecarolina')



    def inserta_producto(self,codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql='''INSERT INTO albunes (cod_album, nombre, id_interprete and id_genero , cant_temas , id_discografica , id_formato , fec_lanzamiento , precio , cantidad , caratula) 
        VALUES('{}', '{}','{}', '{}','{}' ,'{}','{}','{}','{}','{}','{}','{}')'''.format(cod_album, nombre, id_interprete and id_genero , cant_temas , id_discografica , id_formato , fec_lanzamiento , precio , cantidad , caratula)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_albunes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM albunes " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM albunes WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM albunes WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  

