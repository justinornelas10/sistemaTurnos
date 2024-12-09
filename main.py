import tkinter as tk
from tkinter import ttk
import const, asignar
from threading import Thread


sizeVentana = "1280x720"

def controlTurnos():
    showControl = tk.Tk()
    showControl.title("Turnos")

    tk.Label(showControl, text="Asignar Truno", font=("Arial", 16)).pack(pady=10)

    comboTramites = ttk.Combobox(showControl, values=const.tramites, font=("Arial", 14))
    comboTramites.pack(pady=10)
    comboTramites.set("Seleccione un trámite")

    tk.Button(showControl, text="Asignar Turno", font=("Arial", 14), command=lambda: asignar.asignarTurno(comboTramites.get())).pack(pady=10)
    tk.Button(showControl, text="Siguiente Turno", font=("Arial", 14), command=lambda: asignar.siguienteTurno).pack(pady=10)


    showControl.mainloop()
        


def showTurnos(): 

    showWindow = tk.Tk()
    showWindow.title("Turnos Actuales")

    tk.Label(showWindow, text="Turno Actual: ", font=("Arial", 16)).pack(pady=10)
    tk.Label(showWindow, textvariable=asignar.turnoActual, font=("Arial", 24)).pack(pady=10)

    tk.Label(showWindow, text="Turnos en Espera:", font=("Arial", 14)).pack(pady=10)
    asignar.listaTurnos = tk.Listbox(showWindow, font=("Arial", 16), height=10, width=30)
    asignar.listaTurnos.pack(pady=10)

    showWindow.mainloop()

    
        
if __name__ == "__main__":
    Thread(target=controlTurnos).start()
    Thread(target=showTurnos).start()


