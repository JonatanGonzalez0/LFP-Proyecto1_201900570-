from SRC.Token import Token
import tkinter as tk
from tkinter import filedialog,messagebox
from tkinter import *
from tkinter import ttk
import os,webbrowser
from SRC.celda import celda
from SRC.imagen import imagen
from SRC.Analizador import Analizador
from PIL import Image, ImageOps,ImageTk

entradaPrincipal = ''
analizador = Analizador()
imagenes=[]
app = tk.Tk()
combo_imagenes= ttk.Combobox()
existeImagen = False
canvas = Canvas()



def carga_Menu():
    
    ancho_ventana = 1600
    alto_ventana = 900


    #Centrar app dependiendo del monitor
    x_ventana = app.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = app.winfo_screenheight() // 2 - alto_ventana // 2
    app.title("Proyecto LENGUAJES FORMALES DE PROGRAMACION")
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    app.geometry(posicion)

    menubar = tk.Menu(app)
    filemenu = tk.Menu(menubar, tearoff=0)

    etiquetaM = tk.Label(app,text="BIENVENIDO",font=("Courier", 30))
    etiquetaM.pack(padx=30,pady=5)
    
    #botones de las diferentes opciones
    
    filemenu.add_command(label="Cargar Archivo", command=cargarArchivo)
    filemenu.add_command(label="Reporte Tokens HTML", command=reporteTokensHTML)
    filemenu.add_command(label="Reporte Errores HTML", command=reporteErroresHTML)
    filemenu.add_command(label="Salir", command=salir)

    menubar.add_cascade(label="Menu", menu=filemenu)
    app.config(menu=menubar)

    cargarBotones()

    app.mainloop()

def salir():
    app.destroy()

def cargarArchivo():
    try:
        global entradaPrincipal
        Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = filedialog.askopenfilename(initialdir=Carpeta_Raiz,title = "Seleccionar su archivo lfp")
        #ruta_archivo ='C:/Users/Jonatan/OneDrive - Facultad de Ingeniería de la Universidad de San Carlos de Guatemala/2do Semestre 2021/LENGUAJES FORMALES/LABORATORIO/[LFP]Proyecto1_201900570/archivoEntrada.pxla'
        archivo = open(ruta_archivo)

        entrada = archivo.read()
        entradaPrincipal = entrada
        analizadorLexico()
        extraerInfoTokens() 

    
        #mainloop()
    except:
        messagebox.showwarning("Error","No se abrio ningun archivo")   

def analizadorLexico():
    global entradaPrincipal
    global analizador
        
    analizador.Scanner(entradaPrincipal)
        
def extraerInfoTokens():
    
    global imagenes
    imagentemp= imagen()
   
    fila = 1
    tokensFila = []
    ultimoToken = analizador.tokens[-1]
    for token in analizador.tokens:
        
        filaTokenActual = token.fila
        
        
        if fila == filaTokenActual:
            if token ==ultimoToken:
                tokensFila.append(token)
                if tokensFila[0].getLexema()=='filtros':
                    
                    if len(tokensFila)==4:
                        imagentemp.filtros.append(tokensFila[2].getLexema())
                        tokensFila.clear()
                        fila +=1
                    if len(tokensFila)==6:
                        imagentemp.filtros.append(tokensFila[2].getLexema())
                        imagentemp.filtros.append(tokensFila[4].getLexema())
                        tokensFila.clear()
                        fila +=1
                    if len(tokensFila)==8:
                        imagentemp.filtros.append(tokensFila[2].getLexema())
                        imagentemp.filtros.append(tokensFila[4].getLexema())
                        imagentemp.filtros.append(tokensFila[6].getLexema())
                        tokensFila.clear()
                        fila +=1
                imagenes.append(imagentemp)
                continue
                
            else:
                tokensFila.append(token)   
                continue
        else:
            if tokensFila[0].getLexema()=='titulo':
                titulo = tokensFila[2].getLexema()
                titulo = titulo.replace("\"","")
                imagentemp.titulo = titulo
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
                
            if tokensFila[0].getLexema()=='ancho':
                imagentemp.ancho = int(tokensFila[2].getLexema())
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
            if tokensFila[0].getLexema()=='alto':
                imagentemp.alto = int(tokensFila[2].getLexema())
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
            if tokensFila[0].getLexema()=='filas':
                imagentemp.filas = int(tokensFila[2].getLexema())
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
            if tokensFila[0].getLexema()=='columnas':
                imagentemp.columnas = int(tokensFila[2].getLexema())
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
            if tokensFila[0].getLexema()=='[':
                x = int(tokensFila[1].getLexema())
                y =int(tokensFila[3].getLexema())
                
                if tokensFila[5].getLexema() =='true':
                    booleanPintar = TRUE
                else:
                    booleanPintar = FALSE
            
                colorHex = tokensFila[7].getLexema()
                
                imagentemp.celdas.append(celda(x,y,booleanPintar,colorHex))
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
                
            if tokensFila[0].getLexema()=='filtros':
                
                if len(tokensFila)==4:
                    imagentemp.filtros.append(tokensFila[2].getLexema())
                    tokensFila.clear()
                    fila +=1
                if len(tokensFila)==6:
                    imagentemp.filtros.append(tokensFila[2].getLexema())
                    imagentemp.filtros.append(tokensFila[4].getLexema())
                    tokensFila.clear()
                    fila +=1
                if len(tokensFila)==8:
                    imagentemp.filtros.append(tokensFila[2].getLexema())
                    imagentemp.filtros.append(tokensFila[4].getLexema())
                    imagentemp.filtros.append(tokensFila[6].getLexema())
                    tokensFila.clear()
                    fila +=1
                
                tokensFila.append(token)
                continue
    
            if tokensFila[0].getLexema() =='celdas' or tokensFila[0].getLexema()=='}':
                tokensFila.clear()
                fila +=1
                tokensFila.append(token)
                continue
                 
            if tokensFila[0].getLexema()=="@@@@":
                imagenes.append(imagentemp)
                imagentemp = imagen()
                tokensFila.clear()
                fila = token.fila
                tokensFila.append(token)
                continue
            
                   
    if analizador.sePuedeGenerar() ==True:
        global combo_imagenes
        valoresCombo = []
        etiquetaImagenes = tk.Label(app,text="Selecciona una imagen",font=("Courier", 16))
        etiquetaImagenes.place(x=40, y=100)
        
        combo_imagenes = ttk.Combobox(app,font=("Courier", 15))
        combo_imagenes.place(x=40, y=150)
        for img in imagenes:
            valoresCombo.append(img.titulo)

        combo_imagenes["values"]=valoresCombo
        
        btn_Original = tk.Button(app,text="Analizar",font=("Courier", 15),command=analizarImagen)
        btn_Original.place(x=325, y=150)
            
        messagebox.showinfo("Correcto","Analisis completado con exito y sin errores lexicos") 
    else:
        messagebox.showwarning("Error","Analisis completado con éxito y HAY errores lexicos")              
      
    analizador.imprimirErrores() 
 
def cargarBotones(): 
    btn_Original = tk.Button(app,text="Original",font=("Courier", 15),command=Original)
    btn_Original.place(x=30, y=250)
    

    btn_MirrorX = tk.Button(app,text="Mirror X",font=("Courier", 15),command=mirrorX)
    btn_MirrorX.place(x=30, y=350)

    btn_mirrorY = tk.Button(app,text="Mirror Y",font=("Courier", 15),command=mirrorY)
    btn_mirrorY.place(x=30, y=450)

    btn_doubleMirror = tk.Button(app,text="Double Mirror",font=("Courier", 15),command=doubleMirror)
    btn_doubleMirror.place(x=30, y=550)   

def analizarImagen():
    global combo_imagenes
    global existeImagen
    global canvas
    imagenGrafica = combo_imagenes.get()
    
    
    for imagen in imagenes:
        if imagen.titulo==imagenGrafica:
            imagenEncontrada = imagen
            continue
    
    ANCHO = imagenEncontrada.ancho
    ALTO = imagenEncontrada.alto
    FILAS = imagenEncontrada.filas
    COLUMNAS = imagenEncontrada.columnas
    
    TamX = int(ANCHO/COLUMNAS)

    TamY = int(ALTO/FILAS)
    if existeImagen == True:
        canvas.destroy()
        
    canvas = Canvas(app,width=ANCHO,height=ALTO,bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=ANCHO, height=ALTO)
    canvas.create_image(0,0, image=img, anchor=NW)

    for indice in range(len(imagenEncontrada.celdas)):
        celTemp = imagenEncontrada.celdas[indice]
        if celTemp.bool is TRUE:

            inicioX = (celTemp.x)*TamX
            inicioY = (celTemp.y)*TamY
            for i in range(inicioX,inicioX+TamX):
                for j in range(inicioY,inicioY+ TamY):
                    img.put(celTemp.colorHex,(i,j))
    existeImagen = True  
    Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
    img.write( Carpeta_Raiz+'\IMAGENES\originales\\'+imagenEncontrada.titulo+'.png', format='png')
    titulo = imagenEncontrada.titulo.upper()
    rutaHtml = Carpeta_Raiz + f'\\REPORTES\\reporteAnalisis\\analisis{imagenEncontrada.titulo}.html'
    archivo = open(rutaHtml,"w")
    archivo.write("<html><head><title> Analisis </title></head>")
    archivo.write("<body style=\"background-color:  #e5e7e9  ;font-family:courier;font-size:20px;font-style:courier;\" ><br> ")
    archivo.write(f'<h2 align=\"center\"> Titulo imagen : {titulo} </h2>') 
    
    archivo.write("<br><h1 align=\"center\">  Caracteristicas Imagen </h1>") 
    archivo.write("<table align=\"center\" border=\"1\" WIDTH=\"40%\"><tr><th>Caracteristica </th><th>Valor</th></tr>")
    
    archivo.write("<tr><td align=\"center\">ANCHO </td> <td align=\"center\"> "+ str(imagenEncontrada.ancho)+ " </td></tr>")
    archivo.write("<tr><td align=\"center\">ALTO </td> <td align=\"center\"> "+ str(imagenEncontrada.alto)+ " </td></tr>")
    archivo.write("<tr><td align=\"center\">FILAS </td> <td align=\"center\"> "+ str(imagenEncontrada.filas)+ " </td></tr>")
    archivo.write("<tr><td align=\"center\">COLUMNAS </td> <td align=\"center\"> "+ str(imagenEncontrada.columnas)+ " </td></tr>")
    
    for filtro in imagenEncontrada.filtros:
        archivo.write("<tr align=\"center\"><td>FILTRO </td> <td> "+ filtro.upper()+ " </td></tr>")
        
    archivo.write("</table>")
    
    Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
    
    rutaOriginal = Carpeta_Raiz+'\\IMAGENES\\originales\\'+imagenEncontrada.titulo+'.png'
    
    archivo.write("<br><h2 align=\"center\"> Original </h2>") 
    archivo.write(f'<div align="center"><img  src=\"{rutaOriginal}\"></div>')
    
    
    if "mirrorx" in imagenEncontrada.filtros:
        rutaImagen = Carpeta_Raiz+"\\IMAGENES\\originales\\"+imagenEncontrada.titulo+'.png'
        im = Image.open(rutaImagen)
        im_mirror = ImageOps.mirror(im)
        im_mirror.save(Carpeta_Raiz+'\\IMAGENES\\mirrorX\\'+imagenEncontrada.titulo+'.png', quality=95)
        
        rutaMirrorX = Carpeta_Raiz+'\\IMAGENES\\mirrorX\\'+imagenEncontrada.titulo+'.png'
        
        archivo.write("<br><h2 align=\"center\"> MIRROR X </h2>") 
        archivo.write(f'<div align="center"><img  src=\"{rutaMirrorX}\"></div>')
        
    if "mirrory" in imagenEncontrada.filtros:
        rutaImagen = Carpeta_Raiz+"\\IMAGENES\\originales\\"+imagenEncontrada.titulo+'.png'
        im = Image.open(rutaImagen)
        im_flip = ImageOps.flip(im)
        im_flip.save(Carpeta_Raiz+'\\IMAGENES\\mirrorY\\'+imagenEncontrada.titulo+'.png', quality=95)
        
        rutaMirrorY = Carpeta_Raiz+'\\IMAGENES\\mirrorY\\'+imagenEncontrada.titulo+'.png'
        
        archivo.write("<br><h2 align=\"center\"> MIRROR Y </h2>") 
        archivo.write(f'<div align="center"><img  src=\"{rutaMirrorY}\"></div>')
        
    if "doublemirror" in imagenEncontrada.filtros:
        rutaImagen = Carpeta_Raiz+"\\IMAGENES\\originales\\"+imagenEncontrada.titulo+'.png'
        
        im = Image.open(rutaImagen)
        im_mirror = ImageOps.mirror(im)
        im_double = ImageOps.flip(im_mirror)
        im_double.save(Carpeta_Raiz+'\\IMAGENES\\doubleMirror\\'+imagenEncontrada.titulo+'.png', quality=95)
        
        rutaMirrorDouble = Carpeta_Raiz+'\\IMAGENES\\doubleMirror\\'+imagenEncontrada.titulo+'.png'
        
        archivo.write("<br><h2 align=\"center\"> DOUBLE MIRROR </h2>") 
        archivo.write(f'<div align="center"><img  src=\"{rutaMirrorDouble}\"></div>')
    
    archivo.write("</body></html>")
    archivo.close()
    #abrir automaticamente el html en el navegador
    canvas.destroy()
    webbrowser.open(rutaHtml,new=2)
    

def Original():
    global combo_imagenes
    global existeImagen
    global canvas
    imagenGrafica = combo_imagenes.get()
    
    
    for imagen in imagenes:
        if imagen.titulo==imagenGrafica:
            imagenEncontrada = imagen
            continue
    
    ANCHO = imagenEncontrada.ancho
    ALTO = imagenEncontrada.alto
    FILAS = imagenEncontrada.filas
    COLUMNAS = imagenEncontrada.columnas
    
    TamX = int(ANCHO/COLUMNAS)

    TamY = int(ALTO/FILAS)
    if existeImagen == True:
        canvas.destroy()
        
    canvas = Canvas(app,width=ANCHO,height=ALTO,bg="#ffffff")
    canvas.pack()
    img = PhotoImage(width=ANCHO, height=ALTO)
    canvas.create_image(0,0, image=img, anchor=NW)

    for indice in range(len(imagenEncontrada.celdas)):
        celTemp = imagenEncontrada.celdas[indice]
        if celTemp.bool is TRUE:

            inicioX = (celTemp.x)*TamX
            inicioY = (celTemp.y)*TamY
            for i in range(inicioX,inicioX+TamX):
                for j in range(inicioY,inicioY+ TamY):
                    img.put(celTemp.colorHex,(i,j))
    existeImagen = True  
    Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
    img.write( Carpeta_Raiz+'\\IMAGENES\\originales\\'+imagenEncontrada.titulo+'.png', format='png')

    messagebox.showinfo("CORRECTO",f"Se grafico la imagen normal de " + imagenEncontrada.titulo)   
    mainloop()
    
def reporteTokensHTML():
    Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
    rutaHtml = Carpeta_Raiz + "\\REPORTES\\reporteTokens\\reporte_Tokens.html"
    archivo = open(rutaHtml,"w")
    archivo.write("<html><head><title> REPORTE DE TOKENS </title></head>")
    archivo.write("<body style=\"background-color:  #e5e7e9  ;font-family:courier;font-size:20px;font-style:courier;\" ><br> ")
    
    archivo.write("<h2 align=\"center\"> TABLA TOKENS </h2>") 

    archivo.write("<table align=\"center\" border=\"1\" WIDTH=\"40%\"><tr><th>Lexema</th><th>Token</th><th>fila</th><th>columna</th></tr>")
    
    for token in analizador.tokens:
        if token.getTipo()!='DESCONOCIDO ERROR':
            archivo.write("<tr><td align=\"center\">"+token.getLexema()+ "</td> <td align=\"center\"><font color=\"blue\"> " +token.getTipo()+ "</font></td> <td align=\"center\">"+token.getFila()+ "</td> </td> <td align=\"center\">"+token.getColumna()+ "</td></tr>")

    archivo.write("</table><br>")
    archivo.write("</body></html>")
    archivo.close()
    #abrir automaticamente el html en el navegador
    webbrowser.open(rutaHtml,new=2)
    
def reporteErroresHTML():
    if analizador.sePuedeGenerar()==True:
        messagebox.showwarning("ATENCION","No hay errores reportados en la entrada")   
    else:
        Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
        rutaHtml = Carpeta_Raiz + "\\REPORTES\\reporteTokens\\reporte_Errores.html"
        archivo = open(rutaHtml,"w")
        archivo.write("<html><head><title> REPORTE DE ERRORES </title></head>")
        archivo.write("<body style=\"background-color:  #e5e7e9  ;font-family:courier;font-size:20px;font-style:courier;\" ><br> ")
        
        archivo.write("<h2 align=\"center\"> TABLA TOKENS </h2>") 

        archivo.write("<table align=\"center\" border=\"1\" WIDTH=\"40%\"><tr><th>Lexema</th><th>Token</th><th>fila</th><th>columna</th></tr>")
        
        for token in analizador.tokens:
            if token.getTipo() =='DESCONOCIDO ERROR':
                archivo.write("<tr><td align=\"center\">"+token.getLexema()+ "</td> <td align=\"center\"><font color=\"blue\"> " +token.getTipo()+ "</font></td> <td align=\"center\">"+token.getFila()+ "</td> </td> <td align=\"center\">"+token.getColumna()+ "</td></tr>")

        archivo.write("</table><br>")
        archivo.write("</body></html>")
        archivo.close()
        #abrir automaticamente el html en el navegador
        webbrowser.open(rutaHtml,new=2)
    
        
def mirrorX():
    global combo_imagenes
    global existeImagen
    global canvas
    imagenGrafica = combo_imagenes.get()
    for imagen in imagenes:
        if imagen.titulo==imagenGrafica:
            imagenEncontrada = imagen
            continue
    
    if "mirrorx"  in imagenEncontrada.filtros:
        Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
        rutaImagen = Carpeta_Raiz+"\\IMAGENES\\originales\\"+imagenEncontrada.titulo+'.png'
        canvas.delete("all")

        im = Image.open(rutaImagen)
        im_mirror = ImageOps.mirror(im)
        im_mirror.save(Carpeta_Raiz+'\\IMAGENES\\mirrorX\\'+imagenEncontrada.titulo+'.png', quality=95)
        
        imgMirrorXOpen = Image.open(Carpeta_Raiz+'\\IMAGENES\\mirrorX\\'+imagenEncontrada.titulo+'.png')
        python_image = ImageTk.PhotoImage(imgMirrorXOpen)

        canvas.create_image(0,0, image=python_image, anchor=NW)
        messagebox.showinfo("MIRROR X","Se grafico la imagen espejo x")  
        mainloop()
    else:
        messagebox.showwarning("Error","Esta imagen no tiene filtro mirror X")  
        mainloop()
         

def mirrorY():
    global combo_imagenes
    global existeImagen
    global canvas
    imagenGrafica = combo_imagenes.get()
    for imagen in imagenes:
        if imagen.titulo==imagenGrafica:
            imagenEncontrada = imagen
            continue
    
    if "mirrory"  in imagenEncontrada.filtros:
        Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
        rutaImagen = Carpeta_Raiz+"\\IMAGENES\\originales\\"+imagenEncontrada.titulo+'.png'
        canvas.delete("all")

        im = Image.open(rutaImagen)
        im_flip = ImageOps.flip(im)
        im_flip.save(Carpeta_Raiz+'\\IMAGENES\\mirrorY\\'+imagenEncontrada.titulo+'.png', quality=95)

        
        imgMirrorYOpen = Image.open(Carpeta_Raiz+'\\IMAGENES\\mirrorY\\'+imagenEncontrada.titulo+'.png')
        python_image = ImageTk.PhotoImage(imgMirrorYOpen)

        canvas.create_image(0,0, image=python_image, anchor=NW)
        messagebox.showinfo("MIRROR Y","Se grafico la imagen espejo Y")
        mainloop()  
    else:
        messagebox.showwarning("Error","Esta imagen no tiene filtro mirror Y") 
        mainloop() 
         

def doubleMirror():
    global combo_imagenes
    global existeImagen
    global canvas
    imagenGrafica = combo_imagenes.get()
    for imagen in imagenes:
        if imagen.titulo==imagenGrafica:
            imagenEncontrada = imagen
            continue
    
    if "doublemirror"  in imagenEncontrada.filtros:
        Carpeta_Raiz = os.path.dirname(os.path.abspath(__file__))
        rutaImagen = Carpeta_Raiz+"\\IMAGENES\\originales\\"+imagenEncontrada.titulo+'.png'
        canvas.delete("all")

        im = Image.open(rutaImagen)
        
        im_mirrorx = ImageOps.mirror(im)
        im_doubleMirror = ImageOps.flip(im_mirrorx)
        
        im_doubleMirror.save(Carpeta_Raiz+'\\IMAGENES\\doubleMirror\\'+imagenEncontrada.titulo+'.png', quality=95)
        
        imgMirrorDouble = Image.open(Carpeta_Raiz+'\\IMAGENES\\doubleMirror\\'+imagenEncontrada.titulo+'.png')
        python_image = ImageTk.PhotoImage(imgMirrorDouble)

        canvas.create_image(0,0, image=python_image, anchor=NW)
        messagebox.showinfo("DOUBLE MIRROR","Se grafico la imagen con filtro doble espejo") 
        mainloop() 
    else:
        messagebox.showwarning("Error","Esta imagen no tiene filtro Double Mirror")  
        mainloop()

carga_Menu()
            

