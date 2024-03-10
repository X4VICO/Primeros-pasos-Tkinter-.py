# primeros pasos tkinter

import tkinter as tk

# crar ventana principal
ventana = tk.Tk()

# poner titulo a la ventana
ventana.title('Tkinter basico')

# configurar ventana para que no se pueda redimensionar
ventana.resizable(False,False)

# cambiar el color de fondo de la ventana 
ventana.configure(bg='white')

# establecer dimensiones principale de la ventana
ventana.geometry("400x200")

# crear un label y colocarlo con place() para poder detallar la posición con X y Y
etiqueta = tk.Label(ventana, text="¡Hola!", bg='lightblue', fg='black')
etiqueta.place(x=100, y=50)

# crear un botón, cambiar su color de fondo y texto y colocarlo con place()
boton= tk.Button(ventana, text="Haz click", bg='orange', fg='white')
boton.place(x=150, y=100)

#iniciar el bucle
ventana.mainloop()
