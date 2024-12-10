import tkinter as tk
from tkinter import ttk
import const, asignar

text = asignar.siguienteTurno()

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
    tk.Button(showControl, text="Siguiente Turno", font=("Arial", 14), command=asignar.siguienteTurno,).pack(pady=10)
        


def showTurnos(root): 

    showWindow = tk.Toplevel(root)
    showWindow.title("Turnos Actuales")

    tk.Label(showWindow, text="Turno Actual: ", font=("Arial", 16)).pack(pady=10)
    tk.Label(showWindow, text=asignar.turnoActual, font=("Arial", 24)).pack(pady=10)

    tk.Label(showWindow, text="Turnos en Espera:", font=("Arial", 14)).pack(pady=10)
    asignar.listaTurnos = tk.Listbox(showWindow, font=("Arial", 16), height=10, width=30)
    asignar.listaTurnos.pack(pady=10)

    
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    controlTurnos(root)
    showTurnos(root)

    root.mainloop()


