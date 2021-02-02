from tkinter import *
from eliminar import *
from base_datos import *
from tkinter import messagebox

def show(variables, popupGuardar):
    popupGuardar.destroy()
    # imprimir(variables)


def elimina(variables, popupEliminar, elobjeto):
    popupEliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
 
    #-----------base----------
    borrar = Articulos.get(Articulos.ID == lista[0])
    try:
        borrar.delete_instance()
    except:
        messagebox.showerror(message="El registro %s no existe en la BBDD." % borrar, title="Eliminar registro")
    
    # mibase = base_datos.miconexion()
    # print(mibase)
    # print(lista)

    # micursor = mibase.cursor()

    # sql = "DELETE FROM producto WHERE id = %s"
    # dato = (lista[0],)

    # micursor.execute(sql, dato)

    # mibase.commit()

    # print(micursor.rowcount, "Registro borrado")
    
    #-----------objeto----------
    elobjeto.mostrar()
    messagebox.showinfo(message="El registro %s se elimino satisfactoriamente." % borrar, title="Eliminar registro")

def eliminar(objeto):
    # print("------- ver objeto -----------")
    # print(objeto)
    # print("------- visto objeto -----------")
    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)
    Button(popupEliminar, text='Eliminar', command=(lambda: elimina(vars_eliminar, popupEliminar, objeto))).pack()
    Button(popupEliminar, text='Cancelar', command=(lambda: show(vars_eliminar, popupEliminar))).pack()

    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()


