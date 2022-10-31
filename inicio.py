from tkinter import BOTTOM, RIGHT, X, Y, Entry, IntVar, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,messagebox,IntVar
from conexion import Registro_datos

class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Se crea objeto de la clase Registro_datos del modulo conexion que se conecta con la BBDD
        self.base_datos = Registro_datos()

        # Frame titulo                           
        self.frame1 = Frame(master)
        self.frame1.pack(side="top")

        # Frame para mostrar base de datos
        self.frame3 = Frame(master)
        self.frame3.pack(side="bottom",padx=30,pady=30)
      
        # Frame para control
        self.frame4 = Frame(master)
        self.frame4.pack(side="top",pady=30)

        # variable para buscar datos de la base
        self.buscar = StringVar(self.frame4)

           
        self.pantalla_inicio()
        
    # Metodo que crea la pantalla de inicio o principal
    def pantalla_inicio(self):
        
        # Frame 1
        Label(self.frame1, text = 'INFORMACION ALBUMES - INTERPRETES',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
           
        # Frame 3
        # se crean las barras para poder corrermpor la tabla
        # barra eje x
        self.barra_lado_x = Scrollbar(self.frame3, orient = HORIZONTAL)
        self.barra_lado_x.pack(side=BOTTOM,fill=X)

        # barra eje y 
        self.barra_lado_y = Scrollbar(self.frame3, orient =VERTICAL)
        self.barra_lado_y.pack(side=RIGHT,fill=Y)

        # Se crea tabla para mostrar datos y se ubica en frame3
        self.tabla = ttk.Treeview(self.frame3,height=10,yscrollcommand=self.barra_lado_y.set,xscrollcommand=self.barra_lado_x.set)
        self.tabla.pack()
        
        # comando para que la barra corra cuando hay datos para ver
        self.barra_lado_x.config(command=self.tabla.xview)
        self.barra_lado_y.config(command=self.tabla.yview)

        # Se enumeran las columnas 
        self.tabla['columns'] = ('Codigo_album','Nombre','id_Interprete','ID_Genero','Cant_temas','Discografica',
            'Formato','fec_lanzamiento','Precio','Cantidad','Caratula')

        self.tabla.column('#0', minwidth=100, width=120,anchor='center')
        self.tabla.column('#1', minwidth=100, width=100,anchor='center')
        self.tabla.column('#2', minwidth=100, width=100,anchor='center')
        self.tabla.column('#3',minwidth=100,width=100,anchor='center')
        self.tabla.column('#4',minwidth=100,width=100,anchor='center')
        self.tabla.column('#5',minwidth=100,width=100,anchor='center')
        self.tabla.column('#6', minwidth=100, width=100, anchor='center' )
        self.tabla.column('#7',minwidth=100,width=100,anchor='center')
        self.tabla.column('#8',minwidth=100,width=120,anchor='center')
        self.tabla.column('#9', minwidth=100, width=100 , anchor='center')
        self.tabla.column('#10', minwidth=100, width=100, anchor='center')
        self.tabla.column('#11', minwidth=100, width=100, anchor='center')

        self.tabla.heading('#0', text='ID_Album', anchor ='center')
        self.tabla.heading("Codigo_album", text="Codigo_album", anchor='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('id_Interprete', text='id_Interprete', anchor ='center')
        self.tabla.heading('ID_Genero',text='ID_Genero',anchor='center')
        self.tabla.heading('Cant_temas',text='Cant_temas',anchor='center')
        self.tabla.heading('Discografica', text='Discografica', anchor ='center')
        self.tabla.heading('Formato',text='Formato',anchor='center')
        self.tabla.heading('fec_lanzamiento',text='fec_lanzamiento',anchor='center')
        self.tabla.heading('Precio', text='Precio', anchor ='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor ='center')
        self.tabla.heading('Caratula', text='Caratula', anchor ='center')

        # style es para dar estilo a la tabla, formato de las columnas y el color de la seleccion de la fila
        estilo = ttk.Style(self.frame3)
        estilo.theme_use('clam')    
        estilo.map('Treeview',background=[('selected', 'light blue')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila

       #Frame 4
        Label(self.frame4, text = 'CONTROL DE ALBUMES',font=(15),relief="groove",bd=5).grid(columnspan=3,column=0,row=0,padx=20,pady=20)
        Button(self.frame4,command = self.mostrar_todo, text='Listado Albumes').grid(column=0,row=1,padx=10,pady=15)     
        Button(self.frame4,command= self.nuevo_album, text='Nuevo Album').grid(column=2,row=1,padx=10)
        ttk.Separator(self.frame4,orient=HORIZONTAL).grid(columnspan=3,column=0,row=2,pady=5,sticky=("N","S","E","W"))
        Label(self.frame4, text= 'Buscar por Nombre:').grid(column=0,row=3,sticky="E")
        Entry(self.frame4,textvariable=self.buscar).grid(column=1,row=3, pady=5, padx=5)
        Button(self.frame4,command = self.buscar_nombre, text='Buscar').grid(column = 2, row=3,rowspan=1, padx=10,pady=5)
        Button(self.frame4,command = self.actualizar_album, text='Actualizar Datos').grid(column = 2, row=4,rowspan=1, padx=10,pady=10)
        ttk.Separator(self.frame4,orient=HORIZONTAL).grid(columnspan=3,column=0,row=6,pady=5,sticky=("N","S","E","W"))
        Button(self.frame4,command = self.eliminar_fila, text='Eliminar').grid(column = 1,row=7,pady=10)
        Button(self.frame4, text="Salir",width=5,command= lambda:Registro.salir_aplicacion(self)).grid(column=2,row=7)

    # Ventana que contiene Labels que indican que datos ingresar en los Entrys para cargar los datos de un nuevo album
    def nuevo_album(self):
        # Se crea una nueva ventana para cargar albumes
        self.ventana_datos_album = Tk()
        self.ventana_datos_album.title('Registro de Albumes')
        self.ventana_datos_album.config(background='navy')

        # varibles donde registrar los ingresos de datos para ingresar un nuevo album
        self.codigo_album = StringVar(self.ventana_datos_album)
        self.nombre = StringVar(self.ventana_datos_album)
        self.interprete = StringVar(self.ventana_datos_album)
        self.genero = StringVar(self.ventana_datos_album)
        self.cant_temas = StringVar(self.ventana_datos_album)
        self.discografica = StringVar (self.ventana_datos_album)
        self.formato = StringVar(self.ventana_datos_album)
        self.fecha_lanzamiento = StringVar(self.ventana_datos_album)
        self.precio = StringVar(self.ventana_datos_album)
        self.cantidad = StringVar(self.ventana_datos_album)
        self.caratula = StringVar(self.ventana_datos_album)
        
        # indicaciones para cargar datos de albumes
        Label(self.ventana_datos_album, text = 'Codigo Album',fg='white', bg ='navy').grid(column=0,row=1, pady=10)
        Label(self.ventana_datos_album, text = 'Nombre',fg='white', bg ='navy').grid(column=0,row=2, pady=10)
        Label(self.ventana_datos_album, text = 'Interprete',fg='white', bg ='navy').grid(column=0,row=3, pady=10)
        Label(self.ventana_datos_album, text = 'Genero', fg='white',bg ='navy').grid(column=0,row=4, pady=10)
        Label(self.ventana_datos_album, text = 'Cant_temas',fg='white', bg ='navy').grid(column=0,row=5, pady=10)
        Label(self.ventana_datos_album, text = 'Discografica',fg='white', bg ='navy').grid(column=0,row=6, pady=10)
        Label(self.ventana_datos_album, text = 'Formato',fg='white', bg ='navy').grid(column=0,row=7, pady=10)
        Label(self.ventana_datos_album, text = 'Fecha lanzamiento \n aaaa-mm-dd',fg='white', bg ='navy').grid(column=0,row=8,pady=10)
        Label(self.ventana_datos_album, text = 'Precio',fg='white', bg ='navy').grid(column=0,row=9, pady=10)
        Label(self.ventana_datos_album, text = 'Cantidad',fg='white', bg ='navy').grid(column=0,row=10, pady=10)
        Label(self.ventana_datos_album, text = 'Caratula',fg='white', bg ='navy').grid(column=0,row=11, pady=10)

        Entry(self.ventana_datos_album,textvariable=self.codigo_album).grid(column=1,row=1, padx =5)
        Entry(self.ventana_datos_album,textvariable=self.nombre).grid(column=1,row=2)
        Entry(self.ventana_datos_album,textvariable=self.interprete).grid(column=1,row=3)
        Entry(self.ventana_datos_album,textvariable=self.genero).grid(column=1,row=4)
        Entry(self.ventana_datos_album,textvariable=self.cant_temas).grid(column=1,row=5)
        ttk.Combobox(self.ventana_datos_album,state="readonly",values=self.base_datos.buscar_discografica(),textvariable=self.discografica).grid(column=1,row=6) 
        Entry(self.ventana_datos_album,textvariable=self.formato).grid(column=1,row=7)
        Entry(self.ventana_datos_album,textvariable=self.fecha_lanzamiento).grid(column=1,row=8)
        Entry(self.ventana_datos_album,textvariable=self.precio).grid(column=1,row=9)
        Entry(self.ventana_datos_album,textvariable=self.cantidad).grid(column=1,row=10)
        Entry(self.ventana_datos_album,textvariable=self.caratula).grid(column=1,row=11)
        
        # boton para ingresar un nuevo albun a la base
        Button(self.ventana_datos_album,command=lambda: self.agregar_datos(),text='Registrar Album').grid(column=0,row=12, pady=10, padx=5)
        
        # boton para volver a la pantalla principal
        Button(self.ventana_datos_album,command= self.ventana_datos_album.destroy, text="Volver").grid(column=2,row=12,pady=10,padx=5)
        
        self.ventana_datos_album.mainloop()
        
    # Fn para sacar el ID de la discografica para que se cargue como int en la sentencia SQL
    def obtener_id_discografica(self):
        self.id_disc=self.discografica.get()
        self.lista_codigo=[]
        for i in self.id_disc:
            if not i == " ":
                self.lista_codigo.append(i)
                print(self.lista_codigo[0])
        return int(self.lista_codigo[0])
      
    # Funcion que recibe los datos ingresados en la funcion nuevo_album y a travez de base_datos.inserta_album los ingresa en la BBDD
    def agregar_datos(self):
        self.tabla.get_children()
        codigo_album = self.codigo_album.get()
        nombre = self.nombre.get()
        interprete = self.interprete.get()
        genero = self.genero.get()
        cant_temas = self.cant_temas.get()
        discografica = self.obtener_id_discografica()
        formato = self.formato.get()
        fecha_lanzamiento = self.fecha_lanzamiento.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        caratula = self.caratula.get()
        
        self.base_datos.inserta_album(codigo_album, nombre,interprete,genero,cant_temas,discografica,formato,fecha_lanzamiento,precio,cantidad,caratula)
        self.ventana_datos_album.destroy()

    # Funcion para salir de la aplicacion
    def salir_aplicacion(self):
        salir=messagebox.askokcancel("Disquería","Desea salir de la aplicación?")
        if salir == True:
            self.master.destroy()

    # Funcion para buscar albumes por nombre
    def buscar_nombre(self):
        nombre_album = self.buscar.get()
        nombre_album = str("'" + nombre_album + "%'")
        nombre_buscado = self.base_datos.busca_nombre_album(nombre_album)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:12])
        self.buscar.set("")
     
    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_datos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert("",i, text = registro[i][0:1], values=registro[i][1:12])
            
    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            nombre = ("'"+ str(self.nombre_borrar) + "'")       
            self.base_datos.fn_elimina_album(nombre)
            self.tabla.delete(fila)


    def obtener_fila(self,event):
        item_seleccionado = self.tabla.focus()
        if not item_seleccionado:
            return
        data = self.tabla.item(item_seleccionado)
        self.nombre_borrar = data['values'][1]

    def actualizar_album(self):    
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila) 


# funcion que crea la ventana principal
def main():
    ventana_inicio = Tk()
    ventana_inicio.title("Registro de Albumes e Interpretes")
    ventana_inicio.config(bg='gray')
    ventana_inicio.state('zoomed')
    w, h = ventana_inicio.winfo_screenwidth(),ventana_inicio.winfo_screenheight()
    ventana_inicio.geometry("%dx%d+0+0" % (w, h))

    app = Registro(ventana_inicio)
    app.mainloop()

if __name__=="__main__":
    main()        

