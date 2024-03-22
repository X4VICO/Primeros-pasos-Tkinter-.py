import tkinter as tk
import random

class Buscaminas:
    def __init__(self, master):
        self.master = master
        self.master.title("Buscaminas")
        self.master.resizable(False, False)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.bombas = set(random.sample(range(81), 10))
        self.botones = []

        for i in range(9):
            fila = []
            for j in range(9):
                boton = tk.Button(self.frame, width=6, height=3)
                boton.grid(row=i, column=j)
                boton.bind("<Button-1>", lambda event, fila=i, columna=j: self.revelar_celda(fila, columna))
                fila.append(boton)
            self.botones.append(fila)

    def revelar_celda(self, fila, columna):
        if (fila * 9 + columna) in self.bombas:
            self.botones[fila][columna].config(text="X", state="disabled", disabledforeground="red")
        else:
            minas_adyacentes = self.contar_minas_adyacentes(fila, columna)
            if minas_adyacentes > 0:
                self.botones[fila][columna].config(text=minas_adyacentes, state="disabled", disabledforeground="blue")
            else:
                self.botones[fila][columna].config(state="disabled", relief=tk.SUNKEN, bg="light gray")
        
    def contar_minas_adyacentes(self, fila, columna):
        contador = 0
        for i in range(max(0, fila - 1), min(8, fila + 1) + 1):
            for j in range(max(0, columna - 1), min(8, columna + 1) + 1):
                if (i, j) == (fila, columna):
                    continue
                if (i * 9 + j) in self.bombas:
                    contador += 1
        return contador

def main():
    root = tk.Tk()
    app = Buscaminas(root)
    root.mainloop()

if __name__ == "__main__":
    main()