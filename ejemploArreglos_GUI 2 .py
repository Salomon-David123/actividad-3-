#Importar la libreria para trabajar la interfaz gráfica
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

# Estructura de datos (arreglo)
datos = []

def salir():
	raiz.destroy()

def leerDatos():
        '''
        seguir = "yes"

        while (seguir == "yes"):
                valor = simpledialog.askinteger("dato: ", "Cantidad de pastelitos: ")
                datos.append(valor)

                seguir = messagebox.askquestion("seguir?", "Desea seguir?")
        '''
        cadena = simpledialog.askstring("dato ", "Ingrese las cantidades de pastelitos separado por comas: ")
        for dato in cadena.split(","):
                datos.append(int(dato))



def mostrarDatos():
        reporteDatos = ""
        n = len(datos)

        for i in range(n):
                reporteDatos += str(datos[i]) + ", "

        ctReporte.insert(END, "Datos: " + reporteDatos + "\n")

def calcularMaximo():
        mayor = datos[0]
        n = len(datos)

        for i in range(1,n): # 1,2,3...,n-1
                if datos[i] > mayor:
                        mayor = datos[i]

        ctReporte.insert(END, "Mayor: " + str(mayor) + "\n")

def calcularMinimo():
        menor = datos[0]
        n = len(datos)

        for i in range(1,n): # 1,2,3...,n-1
                if datos[i] < menor:
                        menor = datos[i]

        ctReporte.insert(END, "Menor: " + str(menor) + "\n")

def calcularPromedio():
        sumatoria = 0
        n = len(datos)
        for i in range(n): # i= 0,1,2,3,..., n-1
                # sumamos lo que tiene el arreglo en la posicion i
                sumatoria += datos[i]

        promedio = sumatoria / n

        ctReporte.insert(END, "Promedio: " + str(promedio) + "\n")


def buscar():
        n = len(datos)
        elemento = simpledialog.askinteger("Búsqueda", "Ingrese el datos a buscar: ")

        for x in datos:
                if x == elemento:
                        ctReporte.insert(END, str(elemento) + " SI esta en la lista\n")
                        return

        ctReporte.insert(END, str(elemento) + " NO esta en la lista\n")

def contarDatos():
        n = len(datos)
        elemento = simpledialog.askinteger("Búsqueda", "Ingrese el datos a contar: ")
        contador = 0

        for x in datos:
                if x == elemento:
                        contador += 1

        ctReporte.insert(END, str(elemento) + " aparece " +str(contador)+ " veces en la lista\n")

#Interfaz Gráfica
raiz = Tk()
raiz.title("Ejemplo Arreglos")
raiz.resizable(0,0)
raiz.geometry("650x550")

#Contenedor 1
ventana1 = Frame(raiz)
ventana1.config(bd=5,relief="sunken")
ventana1.pack(padx =10, pady=10)

btnLeer = Button(ventana1, text="Leer datos", command= leerDatos)
btnLeer.grid(row=0, column=0,padx=10, pady=10)

btnMostrar = Button(ventana1, text="Mostrar datos", command= mostrarDatos)
btnMostrar.grid(row=0, column=1,padx=10, pady=10)

btnMostrar = Button(ventana1, text="Máximo", command= calcularMaximo)
btnMostrar.grid(row=1, column=0,padx=10, pady=10)

btnMostrar = Button(ventana1, text="Mínimo", command= calcularMinimo)
btnMostrar.grid(row=1, column=1,padx=10, pady=10)

btnMostrar = Button(ventana1, text="Promedio", command= calcularPromedio)
btnMostrar.grid(row=2, column=0,padx=10, pady=10)

btnMostrar = Button(ventana1, text="Buscar", command= buscar)
btnMostrar.grid(row=2, column=1,padx=10, pady=10)


btnMostrar = Button(ventana1, text="Contar", command= contarDatos)
btnMostrar.grid(row=3, column=0,padx=10, pady=10)

bSalir = Button(ventana1, text="Salir", width=10, command= salir)
bSalir.grid(row=3, column=1)

#Contenedor 2
ventana = LabelFrame(raiz, text="Reporte")
ventana.config(bd=5,relief="sunken")
ventana.pack(padx =10, pady=10)

# Area de texto para mostrar el reporte.
ctReporte = Text(raiz, height = 20, width = 62)
#ctReporte.insert(END, 'Correct')
ctReporte.pack()

raiz.mainloop()
