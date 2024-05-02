import tkinter as tk
import random
import time

class TableroTk:
    def __init__(self, master, tamano_celda = 50, n_celdas=(5,5)):
        self.master = master
        self.tamano_celda = tamano_celda
        self.n_celdas = n_celdas
        self.canvas = tk.Canvas(master, width=self.tamano_celda* n_celdas[1],
                                height=self.tamano_celda*n_celdas[0])
        self.canvas.pack()

    def dibujar(self, agentes, basuras):
            self.canvas.delete("all")

            for i in range(self.n_celdas[0]):
                for j in range(self.n_celdas[1]):
                    x0 = j * self.tamano_celda
                    y0 = i * self.tamano_celda
                    x1 = x0 + self.tamano_celda
                    y1 = y0 + self.tamano_celda
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline="gray", fill="white")
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2 , text=f'({j},{i})')

            for basura in basuras:
                bx , by = basura
                x0 = bx * self.tamano_celda
                y0 = by * self.tamano_celda
                x1 = x0 + self.tamano_celda
                y1 = y0 + self.tamano_celda
                self.canvas.create_oval(x0, y0, x1, y1, fill="green")

            for agente in agentes:
                ax , ay = agente.x, agente.y
                x0 = ax * self.tamano_celda
                y0 = ay * self.tamano_celda
                x1 = x0 + self.tamano_celda
                y1 = y0 + self.tamano_celda
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

class AgenteTk:
    
    def __init__(self, x=0, y=0, emoticon="🤖", tamano_emoticon=30):
          self.x = x
          self.y = y
          self.emoticon = emoticon
          self.tamano_emoticon = tamano_emoticon
          self.basuras_recogidas = 0
    
    def mover(self, direccion, size_x, size_y):
        if direccion == "arriba" and self.y > 0:
              self.y -= 1
        elif direccion == "abajo" and self.y < size_y -1:
             self.y += 1
        elif direccion == "izquierda" and self.x > 0:
             self.x -= 1
        elif direccion == "derecha" and self.x < size_x -1:
             self.x += 1
        
        print(f"Movimiento hacia: {direccion} Nueva posicion: ({self.x}, {self.y})")

    def recoger_basura(self, basuras):
        if(self.x, self.y) in basuras:
            basuras.remove((self.x, self.y))
            self.basuras_recogidas += 1
            return True
        return False


def ejecutar_simulacion():
    global root, tablero, agente, basuras
    while basuras:
        direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])

        agente.mover(direccion, size_x, size_y)
        if agente.recoger_basura(basuras):
             print("Basura recogida en: ", agente.x, agente.y)
        tablero.dibujar([agente], basuras)
        root.update_idletasks()
        time.sleep(1)

root = tk.Tk()

root.title("Tablero de simulacion G8")

size_x = 10
size_y = 10
num_basuras = 5

tablero = TableroTk(root, n_celdas=(size_x, size_y))
basuras = {(random.randint(0, size_x - 1), random.randint(0, size_y - 1)) for _ in range(num_basuras)}
agente = AgenteTk(0,0)
tablero.dibujar([agente], basuras)

root.after(1000, ejecutar_simulacion)
root.mainloop()

