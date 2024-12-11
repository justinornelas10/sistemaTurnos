import tkinter as tk
import  asignar
import threading
from pantallaControl import controlTurnos
from pantallaTurnos import showTurnos

turnoActual = asignar.siguienteTurno()
updateEvent = threading.Event()

sizeVentana = "1280x720"


        
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
  
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    controlTurnos(root, changeTurno)
    showTurnos(root, lambda: turnoActual)

    hilo = threading.Thread(target=updateTurno, daemon=True)
    hilo.start()
    
    root.mainloop()


