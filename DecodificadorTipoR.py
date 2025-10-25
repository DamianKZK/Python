import tkinter

# Diccionario de operaciones
Operaciones = {
    "add": "100000",
    "sub": "100010",
    "or": "001101"
}
"""def ventana():
    exito= tkinter.Tk()
    exito.tkinter()
    exito.title("¡Se ha creado el archivo!")
    exito.geometry("200x100")
    
    boton2= tkinter.Button(exito, text=("regresar"), command=exit)"""

# Función para convertir la instrucción
def convertir(instruccion):
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

            instruccion_completa = op + bin_rs + bin_rt + bin_rd + shft + funct
            with open("Binarios.txt", "w") as binarios:
                binarios.write(instruccion_completa+"\n")
                
                
            mostrar_resultado(instruccion_completa)
            
            
        else:
            mostrar_resultado("Operación no reconocida.")
    except Exception as e:
        mostrar_resultado(f"Error: {e}")
# Función para mostrar el resultado
def mostrar_resultado(res):
    entrada.delete("1.0", tkinter.END)
    entrada.insert(tkinter.END, res)

# Interfaz gráfica
ventana = tkinter.Tk()
ventana.title("Decodificador")
ventana.geometry("500x500")
ventana.configure(bg="grey20")

etiqueta = tkinter.Label(ventana, text="Decodificador de instrucciones tipo R", fg="white", font=("TimesNewRoman", 20), bg="gray10")
etiqueta.pack(fill=tkinter.X)

TextoB = tkinter.Label(ventana, text="Ingrese su instrucción (ej. add $1, $2, $3)", bg="blue", fg="white", font=("BOLD", 13))
TextoB.pack()

entrada = tkinter.Text(ventana, width=50, height=10, bg="grey50")
entrada.pack()

boton = tkinter.Button(ventana, text="Submit", command=lambda: convertir(entrada.get("1.0", "end-1c")), bg="blue")
boton.pack()

ventana.mainloop()