import tkinter as tk
from tkinter import ttk
import asignar, const

def controlTurnos(root, changeTurno):
    # Ventana para el control de turnos
    showControl = tk.Toplevel(root)
    showControl.title("Control de Turnos")

    tk.Label(showControl, text="Asignar Turno", font=("Arial", 16)).pack(pady=10)

    comboTramites = ttk.Combobox(showControl, values=const.tramites, font=("Arial", 14))
    comboTramites.pack(pady=10)
    comboTramites.set("Seleccione un trámite")

    tk.Button(
        showControl, 
        text="Asignar Turno", 
        font=("Arial", 14), 
        command=lambda: asignar.asignarTurno(comboTramites.get())
    ).pack(pady=10)
    tk.Button(
        showControl, 
        text="Siguiente Turno", 
        font=("Arial", 14), 
        command=changeTurno
    ).pack(pady=10)