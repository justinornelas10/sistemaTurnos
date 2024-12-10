import tkinter as tk

try:
    root = tk._default_root
    if root is None:
        root=tk.Tk()
        root.withdraw()
except AttributeError:
    root = tk.Tk()
    root.withdraw()

turnoActual = "Ninguno"
turnos = []
listaTurnos = None

def asignarTurno(tramite): 
    if tramite and tramite != 'Seleccione un trámite':
        numTurno = len(turnos) + 1
        newTurno = f"T{numTurno} - {tramite}"
        turnos.append(newTurno)
        actualizarLista()

def siguienteTurno():
    if turnos:
        turnoActual = str(turnos.pop(0))
        print(turnoActual)
        actualizarLista()
    else:
        turnoActual = "Ninguno"
    return turnoActual

def actualizarLista():
    if listaTurnos:
        listaTurnos.delete(0, tk.END)
        for turno in turnos:
            listaTurnos.insert(tk.END, turno)

