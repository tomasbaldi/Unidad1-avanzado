from tkinter import *
from guardar import *
import base_datos
from base_datos import *

def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


def guarda(variables, popupGuardar, elobjeto):
    
    popupGuardar.destroy()
    #-----------guardar-----------
    lista = []
    for variable in variables:
        lista.append(variable.get())
    
    #-------------base------------
    # articulo = Articulos()
    # articulo.titulo = lista[0]
    # articulo.descripcion = lista[1]
    # articulo.save()

    res = Articulos.insert({
    Articulos.titulo: lista[0],
    Articulos.descripcion: lista[1]
    }).execute()

    # mibase = base_datos.miconexion()
    # print(mibase)
    # print(lista)
    # micursor = mibase.cursor()
    # sql = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
    # print(sql)
    #datos = (lista[0], lista[1])
    #micursor.execute(sql, datos)
    #mibase.commit()

    #------------objeto-----------
    elobjeto.mostrar()

def guardar(objeto):
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    
    Button(popupGuardar, text='Guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()
    Button(popupGuardar, text='Cancelar', command=(lambda: show(vars_guardar, popupGuardar))).pack()
    #Button(popupGuardar, text='Guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
