import tkinter as tk

try:
    root = tk.default_root
    if root is None:
        root=tk.Tk()
        root.withdraw()
except AttributeError:
    root = tk.Tk()
    root.withdraw()

turnoActual = tk.StringVar(value="Ninguno")
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
        turnoActual.set(turnos.pop(0))
        actualizarLista()
    else:
        turnoActual.set("Niguno")

def actualizarLista():
    if listaTurnos:
        listaTurnos.delete(0, tk.END)
        for turno in turnos:
            listaTurnos.insert(tk.END, turno)

