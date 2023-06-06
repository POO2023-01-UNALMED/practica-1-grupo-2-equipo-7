from tkinter import *

# Configuracion de ventana
mainWin = Tk()
mainWin.title("Sistema Matricula de Materias")
mainWin.resizable(1,1)
mainWin.geometry("")

# Creacion de Frames

p1Frame=Frame(mainWin,height=450,width=425,bg="red")
p1Frame.grid(row=0,column=0,columnspan=10,rowspan=10,padx=(5,2.5),pady=5)
p1Frame.grid_propagate(False)

p2Frame=Frame(mainWin,height=450,width=425,bg="blue")
p2Frame.grid(row=0,column=10,columnspan=20,rowspan=10,padx=(2.5,5),pady=5)
p2Frame.grid_propagate(False)

p3Frame=Frame(p1Frame,height=100,width=415,bg="green")
p3Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,2.5))
p3Frame.pack_propagate(False)

p4Frame=Frame(p1Frame,height=335,width=415,bg="green")
p4Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(2.5,5))

p5Frame=Frame(p2Frame,height=100,width=415,bg="yellow")
p5Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,2.5))
p5Frame.pack_propagate(False)

p6Frame=Frame(p2Frame,height=335,width=335,bg="yellow")
p6Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(2.5,5))
p6Frame.grid_propagate(False)

# Frame 3 Saludo bienvenida
mensaje="Hola, bienvenido al sistemas de matricula de materias S.M.M"
mensajeBienv = Label(p3Frame,text=mensaje,font=("arial", 18, "bold"),bg="green",wraplength=415)
mensajeBienv.pack(expand=True)

# Frame 5 Bibliografia de cada desarrollador

bibi1="In1 congue, metus eget venenatis condimentum, tellus dolor facilisis risus, non blandit risus dolor sed quam. Nunc eu iaculis magna. Vivamus ac vestibulum ipsum1"
bibi2="In2 congue, metus eget venenatis condimentum, tellus dolor facilisis risus, non blandit risus dolor sed quam. Nunc eu iaculis magna. Vivamus ac vestibulum ipsum2"
bibi3="In3 congue, metus eget venenatis condimentum, tellus dolor facilisis risus, non blandit risus dolor sed quam. Nunc eu iaculis magna. Vivamus ac vestibulum ipsum3"
bibi4="In4 congue, metus eget venenatis condimentum, tellus dolor facilisis risus, non blandit risus dolor sed quam. Nunc eu iaculis magna. Vivamus ac vestibulum ipsum4"
bibi5="In5 congue, metus eget venenatis condimentum, tellus dolor facilisis risus, non blandit risus dolor sed quam. Nunc eu iaculis magna. Vivamus ac vestibulum ipsum5"

biblios = [bibi1,bibi2,bibi3,bibi4,bibi5]

i =1
lisImagenes=[]
def cambiarTextoEImagen(evento):
    global i
    
    # Cambio de texto
    evento.widget["text"]=biblios[i]
    
    # Cambio de imagenes
    imag1=PhotoImage(file=f"Python\src\Imagenes\imgIn{i+1}_1.png")     
    imag2=PhotoImage(file=f"Python\src\Imagenes\imgIn{i+1}_2.png")     
    imag3=PhotoImage(file=f"Python\src\Imagenes\imgIn{i+1}_3.png")     
    imag4=PhotoImage(file=f"Python\src\Imagenes\imgIn{i+1}_4.png")     
    
    global lisImagenes
    lisImagenes=[imag1,imag2,imag3,imag4]
    
    setCuatroImagenes(lisImagenes)
    
    # Cambio de puntero  
    i+=1
    n =2 # numero de grupo de fotos en la carpeta imagenes, cuando se tengan todas debe ser 4
    if i ==n:
        i=0
    

biblioTexto = Label(p5Frame,text=bibi1,font=("arial", 12, "bold"),bg="yellow",wraplength=410,bd=2, relief="solid")
biblioTexto.pack(expand=True,fill="both")
biblioTexto.bind("<Button-1>",cambiarTextoEImagen)

# Frame 6 Imagenes:

def setCuatroImagenes(packImagenes):
    img1.config(image=packImagenes[0])
    img2.config(image=packImagenes[1])
    img3.config(image=packImagenes[2])
    img4.config(image=packImagenes[3])

tam=157

image1 =PhotoImage(file="Python\src\Imagenes\imgIn1_1.png")
image2 =PhotoImage(file="Python\src\Imagenes\imgIn1_2.png")
image3 =PhotoImage(file="Python\src\Imagenes\imgIn1_3.png")
image4 =PhotoImage(file="Python\src\Imagenes\imgIn1_4.png")


img1 = Label(p6Frame,image=image1,height=tam,width=tam)
img1.grid(row=0,column=0,columnspan=1,rowspan=1,padx=2.5,pady=2.5)

img2 = Label(p6Frame,image=image2,height=tam,width=tam)
img2.grid(row=0,column=1,columnspan=1,rowspan=1,padx=2.5,pady=2.5)

img3 = Label(p6Frame,image=image3,height=tam,width=tam)
img3.grid(row=1,column=0,columnspan=1,rowspan=1,padx=2.5,pady=2.5)

img4 = Label(p6Frame,image=image4,height=tam,width=tam)
img4.grid(row=1,column=1,columnspan=1,rowspan=1,padx=2.5,pady=2.5)
    

mainWin.mainloop()


