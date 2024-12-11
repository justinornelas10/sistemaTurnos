import tkinter as tk
import asignar

def showTurnos(root, turnoActual): 
    showWindow = tk.Toplevel(root)
    showWindow.title("Turnos Actuales")
    showWindow.state('zoomed')

    frameTop=tk.Frame(showWindow)
    frameTop.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    frameTop.config(bg='#f57c00')

    frameRight=tk.Frame(showWindow)
    frameRight.place(relx=0.7, rely=0.2, relwidth=0.3, relheight=0.8)
    frameRight.config(bg='#676767')


    tk.Label(frameRight, text="Turno Actual: ", font=("Arial", 16)).pack(pady=10)

    turnoLabel = tk.Label(frameRight, text=turnoActual(), font=("Arial", 24))
    turnoLabel.pack(pady=10)

    tk.Label(frameRight, text="Lista de espera", font=("Arial", 14)).pack(pady=10)


    asignar.listaTurnos = tk.Listbox(frameRight, font=("Arial", 16), height=10, width=30)
    asignar.listaTurnos.pack(pady=10)

    def actualizarTurno():
        turnoLabel.config(text=turnoActual())
        showWindow.after(500, actualizarTurno)

    actualizarTurno()  