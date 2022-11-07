from tkinter import messagebox
import mysql.connector

# Clase para conectarse a la base y ejecutar sentencias SQL
class Registro_datos():

    # metodo para conectarse con la base
    def __init__(self):
        self.conexion = mysql.connector.connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "1234",
        db = "DISQUERIA_TSIT40"
    )

    # metodo que inserta un nuevo album
    def inserta_album(self,codigo_album, nombre, interprete, genero, cant_temas, discografica, formato,
        fecha_lanzamiento, precio, cantidad, caratula):
        if self.conexion.is_connected:
            cursor = self.conexion.cursor()
            nuevo_album = ''' INSERT INTO ALBUM (COD_ALBUM,NOMBRE,ID_INTERPRETE,ID_GENERO,CANT_TEMAS,
            ID_DISCOGRAFICA,ID_FORMATO,FEC_LANZAMIENTO,PRECIO,CANTIDAD,CARATULA) 
            VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''.format(codigo_album, nombre, interprete,
            genero,cant_temas,discografica,formato,fecha_lanzamiento,precio,cantidad,caratula)
            cursor.execute(nuevo_album)
            self.conexion.commit()
            cursor.close()
            messagebox.showinfo("DISQUERIA","ALBUM REGISTRADO CON EXITO")
        else:
            messagebox.showwarning ("DISQUERIA","NO SE PUDO REGISTRAR EL ALBUM")

    # metodo para mostrar los datos de la BBDD
    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        mostrar_base = "SELECT * FROM ALBUM ORDER BY NOMBRE ASC" 
        cursor.execute(mostrar_base)
        registro = cursor.fetchall()
        return registro

    # metodo para buscar albumes por nombre
    def busca_nombre_album(self, nombre_album_buscado):
        cursor = self.conexion.cursor()
        mostrar_album = "SELECT * FROM ALBUM WHERE NOMBRE LIKE {}".format(nombre_album_buscado)
        cursor.execute(mostrar_album)
        nombre_encontrado = cursor.fetchall()
        cursor.close()     
        return nombre_encontrado 

    # metodo para eliminar albumes
    def fn_elimina_album(self,nombre):
        eliminar=messagebox.askokcancel("Disquería",(f"Esta seguro que desea eliminar Album,{nombre}"))    
        if eliminar == True:
            cursor = self.conexion.cursor()
            eliminar_album= "DELETE FROM ALBUM WHERE NOMBRE = {}".format(nombre)
            cursor.execute(eliminar_album)
            self.conexion.commit()    
            cursor.close()
        else:
            messagebox.showerror("Disquería",(f"El album {nombre}, no pudo ser eliminado"))
   
    # metodo para actualizar datos de albumes
    def actualizar_datos_album(self,datos):
        cursor = self.conexion.cursor()
        
        actualizar_datos = '''UPDATE ALBUM 
                            SET COD_ALBUM = %s,NOMBRE= %s,ID_INTERPRETE= %s,ID_GENERO= %s,CANT_TEMAS= %s,ID_DISCOGRAFICA= %s,ID_FORMATO= %s,
                            FEC_LANZAMIENTO= %s,PRECIO= %s,CANTIDAD= %s,CARATULA= %s
                            WHERE ID_ALBUM = %s'''
        
        cursor.execute(actualizar_datos,datos)
        self.conexion.commit()
        cursor.close()

    # metodo para buscar genero
    def buscar_interpretes(self):
        cursor = self.conexion.cursor()
        buscar_interprete = "SELECT ID_INTERPRETE,NOMBRE, APELLIDO FROM INTERPRETE" # ORDER BY NOMBRE ASC
        cursor.execute(buscar_interprete)
        interpretes_obtenidos = cursor.fetchall()        
        lista_interpretes=[]
        for x in interpretes_obtenidos:
            lista_interpretes.append(str(x[0])+" - "+x[1]+" "+x[2])
        cursor.close()
        return (lista_interpretes)

    # metodo para buscar id_interprete
    def buscar_id_interprete(self,data):
        cursor = self.conexion.cursor()
        buscar_id_interp = "SELECT * FROM INTERPRETE WHERE ID_INTERPRETE = '{}'".format(data)
        cursor.execute(buscar_id_interp)
        id_interp_obtenidos = cursor.fetchall()
        cursor.close()
        return id_interp_obtenidos# [0]

    # metodo para buscar genero
    def buscar_genero(self):
        cursor = self.conexion.cursor()
        buscar_genero = "SELECT * FROM GENERO ORDER BY NOMBRE ASC"
        cursor.execute(buscar_genero)
        genero_obtenido = cursor.fetchall()
        genero_obtenido = [x[1] for x in genero_obtenido]
        cursor.close()
        return genero_obtenido

    # metodo para traer id de genero
    def buscar_id_genero(self,data):
        cursor = self.conexion.cursor()
        buscar_id_genero = "SELECT * FROM GENERO WHERE NOMBRE = '{}'".format(data)
        cursor.execute(buscar_id_genero)
        id_genero_obtenido = cursor.fetchall()
        cursor.close()
        return id_genero_obtenido [0][0]       

    # metodo para buscar formato
    def buscar_formatos(self):
        cursor = self.conexion.cursor()
        buscar_formato = "SELECT * FROM FORMATO ORDER BY TIPO ASC"
        cursor.execute(buscar_formato)
        formatos_obtenidos = cursor.fetchall()
        formatos_obtenidos = [x[1] for x in formatos_obtenidos]
        cursor.close()
        return formatos_obtenidos
    
    # metodo para traer id de formato
    def buscar_id_formato(self,data):
        cursor = self.conexion.cursor()
        buscar_id_formato = "SELECT * FROM FORMATO WHERE TIPO = '{}'".format(data)
        cursor.execute(buscar_id_formato)
        id_formato_obtenidos = cursor.fetchall()
        cursor.close()
        return id_formato_obtenidos [0][0]

    # metodo para buscar discograficas
    def buscar_discografica(self):
        cursor = self.conexion.cursor()
        buscar_discograficas = "SELECT * FROM DISCOGRAFICA ORDER BY NOMBRE ASC"
        cursor.execute(buscar_discograficas)
        discograficas_obtenidas = cursor.fetchall()
        discograficas_obtenidas = [x[1] for x in discograficas_obtenidas]
        cursor.close()
        return discograficas_obtenidas
    
    # metodo para traer id de discografica
    def buscar_id_discografica(self,data):
        cursor = self.conexion.cursor()
        buscar_id_disc = "SELECT * FROM DISCOGRAFICA WHERE NOMBRE = '{}'".format(data)
        cursor.execute(buscar_id_disc)
        id_disc_obtenidos = cursor.fetchall()
        cursor.close()
        return id_disc_obtenidos [0][0]

    # metodo para listado por genero
    def listado_genero (self):
        cursor = self.conexion.cursor()
        listar_por_genero ='''SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre,
         precio,formato.tipo FROM album, interprete, discografica,formato,genero 
         WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica
         AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero ORDER By genero.nombre asc'''
        cursor.execute(listar_por_genero)
        registro_genero = cursor.fetchall()
        return registro_genero

