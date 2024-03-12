from tkinter import *  #importamos la libreria tkinter

#-------------------------------configuracion de ventana-------------------------------
root = Tk()                                      #creamos ventana
root.geometry('1440x720')                        #aplicamos a la ventana una medida ('WIDTHxHEIGHT')
root.configure(bg="black")                       #aplicamos color de fondo de la ventana
root.title("Buscaminas by Xavi and Gerard")      #cambiamos el nombre de la ventana
root.resizable(False, False)                     #bloqueamos el reescalado de la ventana

#-------------------------------preparamos zonas de la ventana

#intentar hacer tamaños con variables para que sea más facil manejar medidas
#una vez lo tengamos podemos crear menú y escogiendo dificultad, modificar medidas de ventana
#altoV=1440
#anchoV=180

marco_superior = Frame(root, bg='red', width=1440, height=180) #ancho total x 25% de la altura
marco_superior.place = (x=0, y=0)  #punto superior izquierda

marco_izquierdo = Frame(root, bg='blue', width=360, height=540) #25% del ancho total x (altura - altura marco_superior)
marco_izquierdo.place(x=0, y=180)  #despues de cabecera superior

marco_central = Frame(root, bg='green', width=1080, height=540)
marco_central.place(x=360, y=180)

#-------------------------------iniciar ventana-------------------------------
root.mainloop()                                  
