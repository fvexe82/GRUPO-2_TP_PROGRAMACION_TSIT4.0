from doctest import master
from logging import root
from tkinter import Tk




from tkinter import *
from ventana import *
def main():
    root = Tk()
    root.wm_title(" INSTITUTO SUPERIOR POLITECNICO CORDOBA - PROYECTO INTEGRADOR BASES DE DATOS")
    app = Ventana(root)
    app.mainloop()
    

if __name__== "__main__":
    main()
    
    
    
    
