from ast import main
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Ventana(Frame):
    def __init__(self, master=None):  
        super().__init__(master, width=800, height=400)
        self.master = master
        self.pack()
        self.create_widgets()
        master.wm_attributes("-alpha", 0.9)
        #self.llenarDatos()
        #self.habilitarCajas("disabled")
        self.habilitarbtnOper("normal")
        self.habilitarbtnGuardar("disabled")
    
    def habilitarCajas(self, estado):
        self.textId.configure(state=estado)
        self.textAlbum.configure(state=estado)
        self.textDiscografia.configure(state=estado)
        self.textGenero.configure(state=estado)
        self.textInterprete.configure(state=estado)
        self.textTema.cinfigure(state=estado)

    def habilitarbtnOper(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarbtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCajas(self):
        pass




    def bNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarbtnOper("disabled")
        self.habilitarbtnGuardar("normal")
        self.limpiarCajas()
        self.textAlbum
        pass

    def bModificar(self):
        pass

    def bEliminar():

        pass

    def bGuardar():
        pass

    def bCancelar():
        pass

    def create_widgets(self):
        frame = Frame(self, bg="lightgrey")
        frame.place(x=0, y=0, width=150, height=350 )
       
       
        
        

        self.btnNuevo = Button(frame, text= "Nuevo", command=self.bNuevo, border=2)
        self.btnNuevo.place(x=4, y=40, width=80, height=30)
        

        self.btnModificar = Button(frame, text= "Modificar", command=self.bNuevo, border=2)
        self.btnModificar.place(x=4, y=80, width=80, height=30)

        self.btnEliminar = Button(frame, text= "Eliminar", command=self.bNuevo, border=2)
        self.btnEliminar.place(x=4, y=120, width=80, height=30)

        frame1 = Frame(self,bg="lightblue")
        frame1.place(x=95, y=0, width=150,height=350)

        label = Label(frame1, text="Album: ")
        label.place(x=3,y=5)
        self.textAlbum=Entry(frame1)
        self.textAlbum.place(x=2,y=20,width=100, height=20)

        label1 = Label(frame1,text="Interprete: ")
        label1.place(x=3, y=55)
        self.textInterprete = Entry(frame1)
        self.textInterprete.place(x=3, y=75, width=100, height=20)

        label2 = Label(frame1, text="Genero: ")
        label2.place(x=3, y=105)
        self.textGenero=Entry(frame1)
        self.textGenero.place(x=3, y=125, width=100, height=20)

        label3 = Label(frame1, text="Discografia: ")
        label3.place(x=3, y=155)
        self.textDiscografia=Entry(frame1)
        self.textDiscografia.place(x=3, y=175, width=100, height=20)

        label4 = Label(frame1, text="Tema: ")
        label4.place(x=3, y=200)
        self.textTema=Entry(frame1)
        self.textTema.place(x=3, y=220, width=100, height=20)

        label5 = Label(frame1, text="Precio: ")
        label5.place(x=3, y=245)
        self.textTema=Entry(frame1)
        self.textTema.place(x=3, y=265, width=100, height=20)

        
    

        self.btnGuardar=Button(frame1, text="Guardar", command=self.bGuardar)
        self.btnGuardar.place(x=4, y=300, width=60, height=30)


        self.btnCancelar=Button(frame1, text="Cancelar", command= self.bCancelar)
        self.btnCancelar.place(x=78, y=300, width=60, height=30)



        frame2 = Frame(self)
        frame2.place(x=250, y=0, width=450, height=200)

        self.grid = ttk.Treeview(frame2, columns =("Columna1", "Columna2","Columna3", "Columna4", "Columna5", "Columna6") )
        self.grid.column("#0", width=50)
        self.grid.column("Columna1", width=50, anchor=CENTER)
        self.grid.column("Columna2", width=90, anchor=CENTER)
        self.grid.column("Columna3", width=90, anchor=CENTER)
        self.grid.column("Columna4", width=90, anchor=CENTER)
        self.grid.column("Columna5", width=90, anchor=CENTER)
        self.grid.column("Columna6", width=90, anchor=CENTER)


        

        self.grid.heading("#0", text= "Id", anchor=CENTER)
        self.grid.heading("Columna1", text= "Album", anchor=CENTER)
        self.grid.heading("Columna2", text= "Interprete", anchor=CENTER)
        self.grid.heading("Columna3", text= "Genero", anchor=CENTER)
        self.grid.heading("Columna4", text= "Discografia", anchor=CENTER)
        self.grid.heading("Columna5", text= "Tema", anchor=CENTER)
        self.grid.heading("Columna6", text= "Precio", anchor=CENTER)
        
        self.grid.pack(side=LEFT, fill= Y)

        scrol = Scrollbar(frame2, orient=VERTICAL)
        scrol.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=scrol.set)
        scrol.config(command=self.grid.yview)
        
            