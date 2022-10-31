from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
from conexion import*


class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='navy')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column=0, row=2)

        self.id_album = StringVar()
        self.cod_album = StringVar()
        self.nombre = StringVar()
        self.id_interprete = StringVar()
        self.id_genero = StringVar()
        self.cant_temas = StringVar()
	self.id_discografia = StringVar()
	self.id_formato = StringVar()
	self.fec_lanzamiento = StringVar()
	self.precio = StringVar()
	self.cantidad = StringVar()
	self.caratula = StringVar()
	

        self.DISQUERIA_TSIT40 = Registro_datos()
        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = 'R E G I S T R O \t D E \t ALBUNES',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'AGREGAR REGISTROS',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
	Label(self.frame2, text = 'id_album',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'cod_album',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'nombre',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'id_interprete',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'id_genero', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'cant_temas',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
	Label(self.frame2, text = 'id_discografia',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
	Label(self.frame2, text = 'id_formato',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
	Label(self.frame2, text = 'fec_lanzamiento',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
	Label(self.frame2, text = 'precio',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
	Label(self.frame2, text = 'cantidad',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
	Label(self.frame2, text = 'caratula',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)

        Entry(self.frame2,textvariable=self.id_album , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.cod_album , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.nombre , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.id_interprete , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.id_genero , font=('Arial',12)).grid(column=1,row=5)
	Entry(self.frame2,textvariable=self.cant_temas , font=('Arial',12)).grid(column=1,row=6)
	Entry(self.frame2,textvariable=self.id_discografia , font=('Arial',12)).grid(column=1,row=7)
	Entry(self.frame2,textvariable=self.id_formato , font=('Arial',12)).grid(column=1,row=8)
	Entry(self.frame2,textvariable=self.fec_lanzamiento , font=('Arial',12)).grid(column=1,row=9)
	Entry(self.frame2,textvariable=self.precio , font=('Arial',12)).grid(column=1,row=10)
	Entry(self.frame2,textvariable=self.cantidad , font=('Arial',12)).grid(column=1,row=11)
	Entry(self.frame2,textvariable=self.caratula , font=('Arial',12)).grid(column=1,row=12)
	
       
        Label(self.frame4, text = 'ESCOJA UNA OPCION',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4,command = self.limpiar_datos, text='LIMPIAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)        
        Button(self.frame4,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.buscar_nombre, text='BUSCAR POR TITULO', font=('Arial',8,'bold'), bg='orange').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.buscar , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='MOSTRAR DATOS', font=('Arial',10,'bold'), bg='green2').grid(columnspan=3,column=0,row=3, pady=8)


        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('id_album', 'cod_album', 'nombre', 'id_interprete' , 'id_genero' , 'cant_temas' , 'id_discografica' , 'id_formato' , 	'fec_lanzamiento' , 'precio' , 'cantidad' , 'caratula')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('cod_album', minwidth=100, width=130 , anchor='center')
        self.tabla.column('nombre', minwidth=100, width=120, anchor='center' )
        self.tabla.column('id_interprete', minwidth=100, width=120 , anchor='center')
        self.tabla.column('id_genero', minwidth=100, width=105, anchor='center')
	self.tabla.column('cant_temas', minwidth=100, width=105, anchor='center')
	self.tabla.column('id_discografia', minwidth=100, width=105, anchor='center')
	self.tabla.column('id_formato', minwidth=100, width=105, anchor='center')
	self.tabla.column('fec_lanzamiento', minwidth=100, width=105, anchor='center')
	self.tabla.column('precio', minwidth=100, width=105, anchor='center')
	self.tabla.column('cantidad', minwidth=100, width=105, anchor='center')
	self.tabla.column('caratula', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='id_album', anchor ='center')
        self.tabla.heading('cod_album', text='cod_album', anchor ='center')
        self.tabla.heading('nombre', text='cod_album', anchor ='center' )
        self.tabla.heading('id_interprete', text='id_interprete', anchor='center' )
        self.tabla.heading('id_genero', text='id_genero', anchor ='center')
	self.tabla.heading('cant_temas', text='cant_temas', anchor ='center')
        self.tabla.heading('id_discografia', text='id_discografia', anchor ='center')
        self.tabla.heading('id_formato', text='id_formato', anchor ='center')
	self.tabla.heading('fec_lanzamiento', text='fec_lanzamiento', anchor ='center')
	self.tabla.heading('precio', text='precio', anchor ='center')
	self.tabla.heading('cantidad', text='cantidad', anchor ='center')
	self.tabla.heading('caratula', text='caratula', anchor ='center')
	
	
        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        

    def agregar_datos(self):
        self.tabla.get_children()
        id_album = self.id_album.get()
        cod_album = self.cod_album.get()
        nombre = self.modelo.get()
        id_interprete = self.id_interprete.get()
        id_genero = self.id_genero.get()
	cant_temas = self.cant_temas.get()
	id_discografica = self.id_discografica.get()
	fec_lanzamiento = self.fec_lanzamiento.get()
	precio = self.precio.get()
	cantidad = self.cantidad.get()
	caratula = self.caratula.get()

        datos = (cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
        if cod_album and nombre and id_interprete and id_genero and cant_temas and id_discografica and id_formato and fec_lanzamiento and precio and cantidad and         caratula !='':        
            self.tabla.insert('',0, text = codigo, values=datos)
            self.DISQUERIA_TSIT40.inserta_producto(cod_album, nombre, id_interprete and id_genero , cant_temas , id_discografica , id_formato , fec_lanzamiento , precio , cantidad , caratula)


    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.cos_album.set('')
        self.nombre.set('')
        self.id_interprete.set('')
        self.id_genero.set('')
        self.cant_temas.set('')
	self.id_discografica.set('')
	self.id_formato.set('')
	self.fec_lanzamiento.set('')
	self.precio.set('')
	self.cantidad.set('')
	self.caratula.set('')

    def buscar_nombre(self):
        nombre_album = self.buscar.get()
        nombre_album = str("'" + nombre_producto + "'")
        nombre_buscado = self.DISQUERIA_TSIT40.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.DISQUERIA_TSIT40.mostrar_productos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:12])


    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.DISQUERIA_TSIT40.elimina_productos(nombre)


    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
   

def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('900x500')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()        


