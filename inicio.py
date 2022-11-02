from tkinter import BOTTOM, RIGHT, X, Y, Entry,Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,messagebox,PhotoImage
from conexion import Registro_datos

class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        # Se crea objeto de la clase Registro_datos del modulo conexion que se conecta con la BBDD
        self.base_datos = Registro_datos()
       
        # Frame titulo                           
        self.frame1 = Frame(master)
        self.frame1.pack(side="top")

               # Frame para mostrar base de datos en una tabla
        #self.frame3 = Frame(master)
        #self.frame3.pack(side="bottom",padx=30,pady=30)
      
        # Frame para controles y opciones
        self.frame4 = Frame(master)
        self.frame4.pack(side="top",pady=30)

        # variable para buscar un album
        self.buscar = StringVar(self.frame4)
           
        # Llamada a la Fn pantalla inicio donde se ubican los frame   
        self.pantalla_inicio()
        
    # Venta de inicio o principal
    def pantalla_inicio(self): 
        # Frame 1
        Label(self.frame1, text = 'INFORMACION ALBUMES - INTERPRETES',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
               #Frame 4 - se ubicar los controles 
        Label(self.frame4, text = 'CONTROL DE ALBUMES',font=(15),relief="groove",bd=5).grid(columnspan=3,column=0,row=0,padx=20,pady=20)
        
        Button(self.frame4,command =self.mostrar_todo, text='Listado Albumes').grid(column=0,row=1,padx=10,pady=15)     
        Button(self.frame4,command= self.nuevo_album, text='Nuevo Album').grid(column=2,row=1,padx=10)
        

        Button(self.frame4,text="Listado por genero",command=self.mostrar_listado_genero).grid(column=0,row=2,padx=10,pady=15)
        #Button(self.frame4,text="Nuevo Genero").grid(column=2,row=2,padx=10,pady=15)

        ttk.Separator(self.frame4,orient=HORIZONTAL).grid(columnspan=3,column=0,row=4,pady=5,sticky=("N","S","E","W"))
        
        Label(self.frame4, text= 'Buscar por Nombre:').grid(column=0,row=5,sticky="E")
        Entry(self.frame4,textvariable=self.buscar).grid(column=1,row=5, pady=5, padx=5)
        Button(self.frame4,command =self.buscar_nombre, text='Buscar').grid(column = 2, row=5,rowspan=1, padx=10,pady=5)
        
        ttk.Separator(self.frame4,orient=HORIZONTAL).grid(columnspan=3,column=0,row=6,pady=5,sticky=("N","S","E","W"))
        
        Button(self.frame4,command = self.eliminar_fila, text='Eliminar').grid(column = 1,row=7,pady=10)
        Button(self.frame4, text="Salir",width=5,command= lambda:Registro.salir_aplicacion(self)).grid(column=2,row=7) 

    # Tabla con datos de los albumes
    def tabla_albumes(self):   
        
        # Frame para mostrar base de datos de los albumes en una tabla
        self.frame3 = Frame(self.master)
        self.frame3.pack(side="bottom",padx=30,pady=30)
        
        # barra eje x
        self.barra_lado_x = Scrollbar(self.frame3, orient = HORIZONTAL)
        self.barra_lado_x.pack(side=BOTTOM,fill=X)

        # barra eje y 
        self.barra_lado_y = Scrollbar(self.frame3, orient =VERTICAL)
        self.barra_lado_y.pack(side=RIGHT,fill=Y)

        # Se crea tabla para mostrar datos
        self.tabla = ttk.Treeview(self.frame3,height=10,yscrollcommand=self.barra_lado_y.set,xscrollcommand=self.barra_lado_x.set)
        self.tabla.pack()
        
        # comando para que la barra corra cuando hay datos para ver
        self.barra_lado_x.config(command=self.tabla.xview)
        self.barra_lado_y.config(command=self.tabla.yview)

        # Se enumeran y se ubican las columnas para mostrar datos de la BBDD
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
        
        self.boton_cerrar = Button (self.frame3,text="Cerrar",command= lambda: self.frame3.destroy()).pack(side='right',padx=250)

        self.boton_actualizar = Button(self.frame3,text='Actualizar Datos',command = self.actualizar_album).pack(side='left',padx=250)

    def tabla_genero(self):   
        
        # Frame para mostrar base de datos de los albumes en una tabla
        self.frame3 = Frame(self.master)
        self.frame3.pack(side="bottom",padx=30,pady=30)
        
        # barra eje x
        self.barra_lado_x = Scrollbar(self.frame3, orient = HORIZONTAL)
        self.barra_lado_x.pack(side=BOTTOM,fill=X)

        # barra eje y 
        self.barra_lado_y = Scrollbar(self.frame3, orient =VERTICAL)
        self.barra_lado_y.pack(side=RIGHT,fill=Y)

        # Se crea tabla para mostrar datos
        self.tabla1 = ttk.Treeview(self.frame3,height=10,yscrollcommand=self.barra_lado_y.set,xscrollcommand=self.barra_lado_x.set)
        self.tabla1.pack()
        
        # comando para que la barra corra cuando hay datos para ver
        self.barra_lado_x.config(command=self.tabla1.xview)
        self.barra_lado_y.config(command=self.tabla1.yview)

        # Se enumeran y se ubican las columnas para mostrar datos de la BBDD
        self.tabla1['columns'] = ('Codigo_album','Nombre_album','Nombre_Interprete','Apellido_interprete','Genero','Discografica',
            'Precio','Cantidad','Formato')

        self.tabla1.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla1.column('#1',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#2',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#3',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#4',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#5',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#6',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#7',minwidth=100,width=100,anchor='center')
        self.tabla1.column('#8',minwidth=100,width=120,anchor='center')
       
        self.tabla1.heading('#0',text='Codigo_album',anchor ='center')
        self.tabla1.heading('#1',text='Nombre_album',anchor='center')
        self.tabla1.heading('#2',text='Nombre_interprete',anchor ='center')
        self.tabla1.heading('#3',text='Apellido_Interprete',anchor ='center')
        self.tabla1.heading('#4',text='Genero',anchor='center')
        self.tabla1.heading('#5',text='Discografica',anchor='center')
        self.tabla1.heading('#6',text='Precio',anchor ='center')
        self.tabla1.heading('#7',text='Cantidad',anchor='center')
        self.tabla1.heading('#8',text='Formato',anchor='center')
    
        # style es para dar estilo a la tabla, formato de las columnas y el color de la seleccion de la fila
        estilo = ttk.Style(self.frame3)
        estilo.theme_use('clam')    
        estilo.map('Treeview',background=[('selected', 'light blue')], foreground=[('selected','black')] )

        self.tabla1.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        
        self.boton_cerrar = Button (self.frame3,text="Cerrar",command= lambda: self.frame3.destroy()).pack()

    # Ventana para cargar un nuevo album
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
        ttk.Combobox(self.ventana_datos_album,values=self.base_datos.buscar_discografica(),textvariable=self.discografica).grid(column=1,row=6) #state="readonly",
        Entry(self.ventana_datos_album,textvariable=self.formato).grid(column=1,row=7)
        Entry(self.ventana_datos_album,textvariable=self.fecha_lanzamiento).grid(column=1,row=8)
        Entry(self.ventana_datos_album,textvariable=self.precio).grid(column=1,row=9)
        Entry(self.ventana_datos_album,textvariable=self.cantidad).grid(column=1,row=10)
        Entry(self.ventana_datos_album,textvariable=self.caratula).grid(column=1,row=11)
    
        # boton para ingresar un nuevo albun a la base
        Button(self.ventana_datos_album,command=lambda:[self.agregar_datos(),self.ventana_datos_album.destroy()], text='Registrar Album').grid(column=0,row=12, pady=10, padx=5)
        
        # boton para volver a la pantalla principal
        Button(self.ventana_datos_album,command= self.ventana_datos_album.destroy, text="Volver").grid(column=2,row=12,pady=10,padx=5)
        
        self.ventana_datos_album.mainloop() 
    
    # Ventana para actualizar datos de album seleccionado
    def actualizar(self):
        # Se crea una nueva ventana para cargar albumes
        self.ventana_actualizar = Tk()
        self.ventana_actualizar.title('Actualizar Albumes')
        self.ventana_actualizar.config(background='navy')
        
        # varibles donde registrar los ingresos de datos para ingresar un nuevo album
        #self.id_album = StringVar(self.ventana_actualizar)
        self.codigo_album1 = StringVar(self.ventana_actualizar)
        self.nombre1 = StringVar(self.ventana_actualizar)
        self.interprete1 = StringVar(self.ventana_actualizar)
        self.genero1 = StringVar(self.ventana_actualizar)
        self.cant_temas1 = StringVar(self.ventana_actualizar)
        self.discografica1 = StringVar (self.ventana_actualizar)
        self.formato1 = StringVar(self.ventana_actualizar)
        self.fecha_lanzamiento1 = StringVar(self.ventana_actualizar)
        self.precio1 = StringVar(self.ventana_actualizar)
        self.cantidad1 = StringVar(self.ventana_actualizar)
        self.caratula1 = StringVar(self.ventana_actualizar )

        # indicaciones para los datos en los Entrys datos de albumes
        Label(self.ventana_actualizar, text = 'Codigo Album',fg='white', bg ='navy').grid(column=0,row=1, pady=10)
        Label(self.ventana_actualizar, text = 'Nombre',fg='white', bg ='navy').grid(column=0,row=2, pady=10)
        Label(self.ventana_actualizar, text = 'Interprete',fg='white', bg ='navy').grid(column=0,row=3, pady=10)
        Label(self.ventana_actualizar, text = 'Genero', fg='white',bg ='navy').grid(column=0,row=4, pady=10)
        Label(self.ventana_actualizar, text = 'Cant_temas',fg='white', bg ='navy').grid(column=0,row=5, pady=10)
        Label(self.ventana_actualizar, text = 'Discografica',fg='white', bg ='navy').grid(column=0,row=6, pady=10)
        Label(self.ventana_actualizar, text = 'Formato',fg='white', bg ='navy').grid(column=0,row=7, pady=10)
        Label(self.ventana_actualizar, text = 'Fecha lanzamiento \n aaaa-mm-dd',fg='white', bg ='navy').grid(column=0,row=8,pady=10)
        Label(self.ventana_actualizar, text = 'Precio',fg='white', bg ='navy').grid(column=0,row=9, pady=10)
        Label(self.ventana_actualizar, text = 'Cantidad',fg='white', bg ='navy').grid(column=0,row=10, pady=10)
        Label(self.ventana_actualizar, text = 'Caratula',fg='white', bg ='navy').grid(column=0,row=11, pady=10)

        #Entrys donde se van a mostrar los datos cargados y luego se modifican 
        self.entry_codigo = ttk.Entry(self.ventana_actualizar,textvariable= self.codigo_album1)
        self.entry_codigo.grid(column=1,row=1, padx =5)
        self.entry_codigo.insert(0,self.codigo_album_cargado)    

        self.entry_nombre = ttk.Entry(self.ventana_actualizar,textvariable=self.nombre1)
        self.entry_nombre.grid(column=1,row=2)
        self.entry_nombre.insert(0,self.nombre_cargado)

        self.entry_interprete = ttk.Entry(self.ventana_actualizar,textvariable=self.interprete1)
        self.entry_interprete.grid(column=1,row=3)
        self.entry_interprete.insert(0,self.interprete_cargado)

        self.entry_genero = ttk.Entry(self.ventana_actualizar,textvariable= self.genero1)
        self.entry_genero.grid(column=1,row=4)
        self.entry_genero.insert(0,self.genero_cargado)

        self.entry_cant_temas = ttk.Entry(self.ventana_actualizar,textvariable=self.cant_temas1)
        self.entry_cant_temas.grid(column=1,row=5)
        self.entry_cant_temas.insert(0,self.cantidad_temas_cargado)

        self.entry_discografica = ttk.Combobox(self.ventana_actualizar,values= self.base_datos.buscar_discografica(),textvariable=self.discografica_cargada)
        self.entry_discografica.grid(column=1,row=6) #state="readonly",
        self.entry_discografica.set(self.discografica_cargada)
        
        entry_formato = ttk.Entry(self.ventana_actualizar,textvariable=self.formato1)
        entry_formato.grid(column=1,row=7)
        entry_formato.insert(0,self.formato_cargado)

        entry_fecha_lanzanmiento = ttk.Entry(self.ventana_actualizar,textvariable=self.fecha_lanzamiento1)
        entry_fecha_lanzanmiento.grid(column=1,row=8)
        entry_fecha_lanzanmiento.insert(0,self.fecha_cargada)

        entry_precio = ttk.Entry(self.ventana_actualizar,textvariable=self.precio1)
        entry_precio.grid(column=1,row=9)
        entry_precio.insert(0,self.precio_cargado)
        
        entry_cantidad = ttk.Entry(self.ventana_actualizar,textvariable=self.cantidad1)
        entry_cantidad.grid(column=1,row=10)
        entry_cantidad.insert(0,self.cantidad_cargada)

        entry_caratula = ttk.Entry(self.ventana_actualizar,textvariable=self.caratula1)
        entry_caratula.grid(column=1,row=11)
        entry_caratula.insert(0,self.caratula_cargada)

        # boton para modificar un album
        Button(self.ventana_actualizar,command= lambda:[self.agregar_datos_modificados(),self.ventana_actualizar.destroy()] ,text='Modificar Album').grid(column=0,row=12, pady=10, padx=5)
    
        # boton para volver a la pantalla principal
        Button(self.ventana_actualizar,command= self.ventana_actualizar.destroy, text="Volver").grid(column=2,row=12,pady=10,padx=5)

        self.ventana_actualizar.mainloop()

    # Fn para sacar el ID de la discografica para que se cargue como int en la sentencia SQL
    def obtener_id_discografica(self):
        self.id_disc=self.discografica.get()
        self.lista_codigo=[]
        for i in self.id_disc:
            if not i == " ":
                self.lista_codigo.append(i)
        return int(self.lista_codigo[0])

    # Fn que recibe los datos ingresados en la funcion nuevo_album y a travez de base_datos.inserta_album los ingresa en la BBDD
    def agregar_datos(self):
        #self.tabla.get_children()
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
    
    # Fn para actualizar datos del album selecionado
    def agregar_datos_modificados(self):
        #self.tabla.get_children()
        id_album = self.id_album
        codigo_album1 = self.codigo_album1.get()
        nombre1 = self.nombre1.get()
        interprete1 = self.interprete1.get()
        genero1 = self.genero1.get()
        cant_temas1 = self.cant_temas1.get()
        discografica1 = self.discografica_cargada
        formato1 = self.formato1.get()
        fecha_lanzamiento1 = self.fecha_lanzamiento1.get()
        precio1 = self.precio1.get()
        cantidad1 = self.cantidad1.get()
        caratula1 = self.caratula1.get()
        datos = (codigo_album1, nombre1,interprete1,genero1,cant_temas1,
        discografica1,formato1,fecha_lanzamiento1,precio1,cantidad1,caratula1,id_album)

        self.base_datos.actualizar_datos_album(datos)

        messagebox.showinfo("Disquería","Album actualizado con exito!")

    # Fn para salir de la aplicacion
    def salir_aplicacion(self):
        salir=messagebox.askokcancel("Disquería","Desea salir de la aplicación?")
        if salir == True:
            self.master.destroy()

    # Fn para buscar albumes por nombre
    def buscar_nombre(self):
        try:
            if self.buscar != '':
                nombre_album = self.buscar.get()
                nombre_album = str("'" + nombre_album + "%'")
                nombre_buscado = self.base_datos.busca_nombre_album(nombre_album)
                self.tabla.delete(*self.tabla.get_children())
                i = -1
                for dato in nombre_buscado:
                    i= i+1                       
                    self.tabla.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:12])
                self.buscar.set("")
            else:
                messagebox.showerror("Disquería","Ingrese un nombre de Album para buscar")
        except:
            self.mostrar_todo()
            if self.buscar == "":
                messagebox.showerror("Disquería","Ingrese un nombre de Album para buscar")
            else:
                pass
            
    # Fn para mostrar datos en la tabla
    def mostrar_todo(self):
        self.tabla_albumes()
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_datos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert("",i, text = registro[i][0:1], values=registro[i][1:12])

    # Fn para mostrar listado por genero en la tabla
    def mostrar_listado_genero(self):
        self.tabla_genero()
        self.tabla1.delete(*self.tabla1.get_children())
        registro_genero = self.base_datos.listado_genero()
        i = -1
        for dato in registro_genero:
            i= i+1                       
            self.tabla1.insert("",i, text = registro_genero[i][0:1], values=registro_genero[i][1:10])

    # Fn para eliminar album            
    def eliminar_fila(self):
        try:
            item_seleccionado = self.tabla.focus()
            if not item_seleccionado:
                return messagebox.showerror("Disquería","Seleccione un Album para eliminar")
            fila = self.tabla.selection()
            if len(fila) !=0:        
                nombre = ("'"+ str(self.nombre_borrar) + "'")       
                self.base_datos.fn_elimina_album(nombre)
                self.tabla.delete(fila)
        except:
            return messagebox.showerror("Disquería","Seleccione un Album del listado para eliminar")

    # Fn para que toma los datos seleccionados de una fila
    def obtener_fila(self,event):
        item_seleccionado = self.tabla.focus()
        if not item_seleccionado:
            return
        data = self.tabla.item(item_seleccionado)
        self.nombre_borrar = data['values'][1]

    # Fn que toma los datos seleccionados de un album y los inserta en la ventana actualizar para modificarlos
    def actualizar_album(self):    
        item_seleccionado = self.tabla.focus()
        if not item_seleccionado:
            return messagebox.showerror("Disquería","Seleccione un Album para modificar")
        data = self.tabla.item(item_seleccionado)
        self.id_album = data ['text']   
        self.codigo_album_cargado = data['values'][0]
        self.nombre_cargado = data['values'][1]
        self.interprete_cargado = data['values'][2]
        self.genero_cargado = data['values'][3]
        self.cantidad_temas_cargado = data['values'][4]
        self.discografica_cargada = data['values'][5]
        self.formato_cargado = data['values'][6]
        self.fecha_cargada = data['values'][7]
        self.precio_cargado = data['values'][8]
        self.cantidad_cargada = data['values'][9]
        self.caratula_cargada = data['values'][10]
      
        self.actualizar()

# Fn que da inicio a la ventana principal
def main():
    ventana_inicio = Tk()
    ventana_inicio.title("Registro de Albumes e Interpretes")
    fondo = PhotoImage (file='' )
    ventana_inicio.config(bg='gray')
    ventana_inicio.state('zoomed')
    w, h = ventana_inicio.winfo_screenwidth(),ventana_inicio.winfo_screenheight()
    ventana_inicio.geometry("%dx%d+0+0" % (w, h))
    app = Registro(ventana_inicio)
    app.mainloop()

if __name__=="__main__":
    main()        

