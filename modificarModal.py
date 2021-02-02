from tkinter import *
from modificar import *
from base_datos import *
from tkinter import messagebox
from peewee import DoesNotExist

def show(variables, popupModificar):
    popupModificar.destroy()
    # imprimir(variables)
    # print(type(variables))


def modifica(variables, popupModificar, elobjeto):
    popupModificar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    try:
        verificar_id = Articulos.get(Articulos.ID == lista[0])
        actualizar = Articulos.update(titulo = lista[1], descripcion = lista[2]).where(Articulos.ID == lista[0])
        actualizar.execute()
        messagebox.showinfo(title="Modificacion de datos", message="Los datos para el ID %s se modificaron correctamente." % lista[0])
        elobjeto.mostrar()
    except DoesNotExist:
        messagebox.showerror(title="Modificacion de datos", message="No se encontro el ID %s en la BBDD.\n Pruebe nuevamente con otro ID." % lista[0])
    
    # print(lista)
    # mibase = base_datos.miconexion()
    # print(mibase)
    # print(lista[0])
    # print(lista[1])
    # micursor = mibase.cursor()
    # elid = lista[0]
    # tit =lista[1]
    # desc =lista[2]
    # sql = "UPDATE producto SET titulo = " +"'"+ tit +"' , descripcion = " +"'"+ desc +"' WHERE id = "+ elid +""

    # print(sql)
    # micursor.execute(sql)
    # mibase.commit()

    #-----------objeto----------

def modificar(objeto):
    # print("------- ver objeto -----------")
    # print(objeto)
    # print("------- visto objeto -----------")
    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    # print(vars_modificar)
    Button(popupModificar, text='Modificar', command=(lambda: modifica(vars_modificar, popupModificar, objeto))).pack()
    Button(popupModificar, text='Cancelar', command=(lambda: show(vars_modificar, popupModificar))).pack()    

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()
