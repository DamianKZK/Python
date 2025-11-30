import tkinter as tk
from tkinter import filedialog

from core import tokenize, open_file
from tobin import Instruction
from code_parser import parse, parseline


def decodificar_linea(instruccion: str) -> str:
    try:
        return parseline(instruccion)

    except Exception as e:
        return f"Error: {e}"

def convertir_manual() -> None:
    instrucciones = entrada.get("1.0", "end-1c").strip().splitlines()
    resultado = ""
    for linea in instrucciones:

        if not linea.strip():
            continue

        binario = decodificar_linea(linea)
        resultado += f"{binario}\n"

    mostrar_resultado(resultado)

def mostrar_resultado(res: str) -> None:
    entrada.delete("1.0", tk.END)
    entrada.insert(tk.END, res)

def Seleccionar() -> None:
    ruta = tk.filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if not ruta:
        return

    try:
        mostrar_resultado(parse(ruta))

    except Exception as e:
        mostrar_resultado(f"Error al abrir el archivo: {e}")

def guardar() -> None:
    contenido = entrada.get("1.0", "end-1c")

    with open("Binarios.txt", "a") as binarios:
        binarios.write(contenido + "\n")

    ventana_exito = tk.Toplevel()
    ventana_exito.configure(bg="grey30")
    ventana_exito.title("¡Archivo Guardado!")
    ventana_exito.geometry("300x150")   

    TextoE = tk.Label(ventana_exito, text="¡Archivo guardado exitosamente!", bg="royalblue", fg="white", font=("BOLD", 13))
    TextoE.pack(pady=50)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Decodificador")
ventana.geometry("500x500")
ventana.configure(bg="grey20")

etiqueta = tk.Label(ventana, text="Decodificador de instrucciones tipo R", fg="white", font=("TimesNewRoman", 20), bg="grey10")
etiqueta.pack(fill=tk.X)

TextoB = tk.Label(ventana, text="Ingrese una o más instrucciones (ej. add $1, $2, $3)", bg="royalblue", fg="white", font=("BOLD", 13))
TextoB.pack(pady=10)

entrada = tk.Text(ventana, width=50, height=10, bg="grey50")
entrada.pack(pady=5)

botonD = tk.Button(ventana, text="Decodificar", command=convertir_manual, bg="darkblue", fg="white")
botonD.place(relx=0.5, rely=0.65, anchor="center")

TextoO = tk.Label(ventana, text="O también puede:", bg="royalblue", fg="white", font=("BOLD", 13))
TextoO.pack(pady=10)

botonT = tk.Button(ventana, text="Ingresar su archivo de texto", command=Seleccionar, bg="darkblue", fg="white")
botonT.place(relx=0.5, rely=0.75, anchor="center")

botonG = tk.Button(ventana, text="Guardar", command=guardar, bg="darkblue", fg="white")
botonG.place(relx=0.95, rely=0.95, anchor="se")

botonS = tk.Button(ventana, text="Salir", command=ventana.quit, bg="darkblue", fg="white")
botonS.place(relx=0.05, rely=0.95, anchor="sw")

ventana.mainloop()