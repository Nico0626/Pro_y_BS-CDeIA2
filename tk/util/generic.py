from PIL import ImageTk, Image

#Renderizar la imagen a gusto
def leer_imagen(patch, size):
    return ImageTk.PhotoImage(Image.open(patch).resize(size, Image.ADAPTIVE))


#Funcion para centrar la ventana
def center_ventana(ventana, ancho, largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_largo // 2) - (largo // 2)
    geometria = "{}x{}+{}+{}".format(ancho, largo, x, y)#actualizar python y cambiar a geometria = f"{ancho}x{largo}+{x}+{y}"
    ventana.geometry(geometria)
    
