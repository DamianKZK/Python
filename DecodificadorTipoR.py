import tkinter
from tkinter import filedialog

Operaciones = {
    "add": "100000",
    "sub": "100010",
    "or": "001101"
}

def decodificar_linea(instruccion):
    try:
        partes = instruccion.replace(",", "").split()
        operacion = partes[0].lower()
        if operacion in Operaciones:
            rd = int(partes[1].replace("$", ""))
            rs = int(partes[2].replace("$", ""))
            rt = int(partes[3].replace("$", ""))

            op = "000000"
            shft = "00000"
            funct = Operaciones[operacion]

            bin_rs = format(rs, '05b')
            bin_rt = format(rt, '05b')
            bin_rd = format(rd, '05b')

            return op + bin_rs + bin_rt + bin_rd + shft + funct
        else:
            return "Operación no reconocida"
    except Exception as e:
        return f"Error: {e}"

def convertir_manual():
    instrucciones = entrada.get("1.0", "end-1c").strip().splitlines()
    resultado = ""
    for idx, linea in enumerate(instrucciones, start=1):
        if linea.strip():
            binario = decodificar_linea(linea)
            resultado += f"Instrucción {idx}: {binario}\n"
    mostrar_resultado(resultado)

def mostrar_resultado(res):
    entrada.delete("1.0", tkinter.END)
    entrada.insert(tkinter.END, res)

def Seleccionar():
    ruta = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta:
        resultado = ""
        try:
            with open(ruta, "r") as archivo:
                lineas = archivo.readlines()
                for idx, linea in enumerate(lineas, start=0):
                    linea = linea.strip()
                    if linea:
                        binario = decodificar_linea(linea)
                        resultado += f"Instrucción {idx}: {binario}\n"
            mostrar_resultado(resultado)
        except Exception as e:
            mostrar_resultado(f"Error al abrir el archivo: {e}")

def guardar():
    contenido = entrada.get("1.0", "end-1c")
    with open("Binarios.txt", "a") as binarios:
        binarios.write(contenido + "\n")
    ventana_exito = tkinter.Toplevel()
    ventana_exito.configure(bg="grey30")
    ventana_exito.title("¡Archivo Guardado!")
    ventana_exito.geometry("300x150")
    TextoE = tkinter.Label(ventana_exito, text="¡Archivo guardado exitosamente!", bg="royalblue", fg="white", font=("BOLD", 13))
    TextoE.pack(pady=50)

# Interfaz gráfica
ventana = tkinter.Tk()
ventana.title("Decodificador")
ventana.geometry("500x500")
ventana.configure(bg="grey20")

etiqueta = tkinter.Label(ventana, text="Decodificador de instrucciones tipo R", fg="white", font=("TimesNewRoman", 20), bg="grey10")
etiqueta.pack(fill=tkinter.X)

TextoB = tkinter.Label(ventana, text="Ingrese una o más instrucciones (ej. add $1, $2, $3)", bg="royalblue", fg="white", font=("BOLD", 13))
TextoB.pack(pady=10)

entrada = tkinter.Text(ventana, width=50, height=10, bg="grey50")
entrada.pack(pady=5)

botonD = tkinter.Button(ventana, text="Decodificar", command=convertir_manual, bg="darkblue", fg="white")
botonD.place(relx=0.5, rely=0.65, anchor="center")

TextoO = tkinter.Label(ventana, text="O también puede:", bg="royalblue", fg="white", font=("BOLD", 13))
TextoO.pack(pady=10)

botonT = tkinter.Button(ventana, text="Ingresar su archivo de texto", command=Seleccionar, bg="darkblue", fg="white")
botonT.place(relx=0.5, rely=0.75, anchor="center")

botonG = tkinter.Button(ventana, text="Guardar", command=guardar, bg="darkblue", fg="white")
botonG.place(relx=0.95, rely=0.95, anchor="se")

botonS = tkinter.Button(ventana, text="Salir", command=ventana.quit, bg="darkblue", fg="white")
botonS.place(relx=0.05, rely=0.95, anchor="sw")

ventana.mainloop()