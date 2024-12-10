import tkinter as tk
from tkinter import ttk
import const, asignar
import threading

turnoActual = asignar.siguienteTurno()
updateEvent = threading.Event()

sizeVentana = "1280x720"

def controlTurnos(root):
    #Ventana para el control de turnos
    showControl = tk.Toplevel(root)
    showControl.title("Control de Turnos")

    tk.Label(showControl, text="Asignar Truno", font=("Arial", 16)).pack(pady=10)

    comboTramites = ttk.Combobox(showControl, values=const.tramites, font=("Arial", 14))
    comboTramites.pack(pady=10)
    comboTramites.set("Seleccione un trámite")

    tk.Button(showControl, text="Asignar Turno", font=("Arial", 14), command=lambda: asignar.asignarTurno(comboTramites.get()),
    ).pack(pady=10)
    tk.Button(showControl, text="Siguiente Turno", font=("Arial", 14), command=changeTurno,).pack(pady=10)
        
def changeTurno():
    global updateEvent
    updateEvent.set()

def updateTurno():
    global turnoActual, updateEvent
    while True: 
        updateEvent.wait()
        turnoActual = asignar.siguienteTurno()
        print(turnoActual)
        updateEvent.clear()

def showTurnos(root): 
    global turnoActual

    showWindow = tk.Toplevel(root)
    showWindow.title("Turnos Actuales")

    tk.Label(showWindow, text="Turno Actual: ", font=("Arial", 16)).pack(pady=10)

    turnoLabel = tk.Label(showWindow, text=turnoActual, font=("Arial", 24))
    turnoLabel.pack(pady=10)

    tk.Label(showWindow, text="Lista de espera", font=("Arial", 14)).pack(pady=10)


    asignar.listaTurnos = tk.Listbox(showWindow, font=("Arial", 16), height=10, width=30)
    asignar.listaTurnos.pack(pady=10)

    def actualizarTurno():
        turnoLabel.config(text=turnoActual)
        showWindow.after(500, actualizarTurno)

    actualizarTurno()    
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    controlTurnos(root)
    showTurnos(root)

    hilo = threading.Thread(target=updateTurno, daemon=True)
    hilo.start()
    
    root.mainloop()


