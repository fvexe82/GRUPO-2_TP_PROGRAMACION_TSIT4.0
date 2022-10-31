import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='DISQUERIA_TSIT40', 
                                            user = 'root',
                                            password ='maytecarolina')



    def InsertarAlbum(self,album):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "insert into album values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

                data = (album.getCod_album(),
                album.getNombre(),
                album.getId_interprete(),
                album.getId_genero(),
                album.getCant_temas(),
                album.getId_discografica(),
                album.getId_formato(),
                album.getFec_lanzamiento(),
                album.getPrecio(),
                album.getCantidad(),
                album.getCaratula())

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Álbum insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)


    def ListarAlbumes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT id_album, cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album, interprete, discografica,formato,genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero ORDER By interprete.apellido desc"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

    def busca_album(self, album):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM album WHERE NOMBRE = {}".format(album)
        cursor.execute(sql)
        nombreX = cursor.fetchall()
        cursor.close()     
        return album 

    def elimina_album(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM ALBUM WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  

