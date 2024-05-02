import tkinter as tk
import random
import time
from collections import deque
from graphviz import Digraph

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
    
    def mover(self, path):
        if path:
            self.x, self.y = path.popleft()
            print(f"Agente se mueve a ({self.x},{self.y})")

    def recoger_basura(self, basuras):
        if(self.x, self.y) in basuras:
            basuras.remove((self.x, self.y))
            self.basuras_recogidas += 1
            return True
        return False
    
    def bfs(self, inicio, basuras, ancho, alto , graph=None):
        cola = deque([inicio])
        visitados = {}
        visitados[inicio]= True
        ruta = {inicio: []}

        if graph is not None:
            graph.node(str(inicio), f"{inicio}")  # Agregar el nodo de inicio al gráfico


        while cola:
            actual = cola.popleft()
            if actual in basuras:
                return deque(ruta[actual])
            
            direcciones = [("arriba", 0, -1), ("abajo", 0, 1) , ("izquierda", -1, 0 ), ("derecha", 1, 0 )]
            for direccion in direcciones:
                nx, ny = actual[0] + direccion[1], actual[1] + direccion[2]
                if 0 <= nx  < ancho and 0 <= ny < alto and not visitados.get((nx, ny), False):
                    visitados[(nx, ny)] = True
                    cola.append((nx, ny))
                    ruta[(nx, ny)] = ruta[actual] + [(nx, ny)]
                    if graph is not None:
                        graph.node(str((nx, ny)), f"{(nx, ny)}")  # Agregar el nodo al gráfico
                        graph.edge(str(actual), str((nx, ny)))  # Agregar la arista al gráfico
        return deque()


def ejecutar_simulacion():
    global root, tablero, agente, basuras
    path = deque()
    
    graph = Digraph(comment='BFS Arbol')

    while basuras:
        if not path:
            path = agente.bfs((agente.x, agente.y), basuras, size_x, size_y, graph=graph)

        agente.mover(path)
        if agente.recoger_basura(basuras):
             print("Basura recogida en: ", agente.x, agente.y)
             path = deque()
             
        tablero.dibujar([agente], basuras)
        root.update_idletasks()
        time.sleep(1)
    graph.view()

root = tk.Tk()

root.title("Tablero de simulacion G8")

size_x = 5
size_y = 5
num_basuras = 1

tablero = TableroTk(root, n_celdas=(size_x, size_y))
basuras = [(2,2)]
agente = AgenteTk(0,0)
tablero.dibujar([agente], basuras)

root.after(1000, ejecutar_simulacion)
root.mainloop()





    
                    
            



        