from tkinter import *

class VentInicio(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)       
        self.pack()
        
        # Creacion de Frames

        p1Frame=Frame(self,height=450,width=425,bg="red")
        p1Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=(5,3),pady=5)
        p1Frame.grid_propagate(False)

        p2Frame=Frame(self,height=450,width=425,bg="blue")
        p2Frame.grid(row=0,column=1,columnspan=1,rowspan=1,padx=(3,5),pady=5)
        p2Frame.grid_propagate(False)

        p3Frame=Frame(p1Frame,height=70,width=415,bg="green")
        p3Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p3Frame.pack_propagate(False)

        p4Frame=Frame(p1Frame,height=365,width=415,bg="green")
        p4Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p4Frame.pack_propagate(False)

        p5Frame=Frame(p2Frame,height=100,width=415,bg="yellow")
        p5Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p5Frame.pack_propagate(False)

        p6Frame=Frame(p2Frame,height=335,width=335,bg="yellow")
        p6Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
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

        self.biblios = [bibi1,bibi2,bibi3,bibi4,bibi5]
          
        self.punteroIntergrante =1
        def cambiarTextoEImagenF6(evento):
            i=self.punteroIntergrante
            
            # Cambio de texto
            evento.widget["text"]=self.biblios[i]
            
            # Cambio de imagenes
            
            imag1=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\imgIn{i+1}_1.png")     
            imag2=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\imgIn{i+1}_2.png")     
            imag3=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\imgIn{i+1}_3.png")     
            imag4=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\imgIn{i+1}_4.png")     
            
            global lisImagenes # Es global para no perder el puntero de las imagenes cuando el metodo finalice
            lisImagenes=[imag1,imag2,imag3,imag4]
            
            setCuatroImagenes(lisImagenes)
            
            # Cambio de puntero  
            i+=1
            n =2 # numero de grupo de fotos en la carpeta imagenes, cuando se tengan todas debe ser 4
            if i ==n:
                self.punteroIntergrante= 0
            else:
                self.punteroIntergrante=i
            

        biblioTexto = Label(p5Frame,text=bibi1,font=("arial", 12, "bold"),bg="yellow",wraplength=410,highlightbackground="black",highlightthickness=2)
        biblioTexto.pack(expand=True,fill="both")
        biblioTexto.bind("<Button-1>",cambiarTextoEImagenF6)


        # Frame 6 Imagenes:
        def setCuatroImagenes(packImagenes):
            img1.config(image=packImagenes[0])
            img2.config(image=packImagenes[1])
            img3.config(image=packImagenes[2])
            img4.config(image=packImagenes[3])

        tam=157

        self.image1 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\imgIn1_1.png")
        self.image2 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\imgIn1_2.png")
        self.image3 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\imgIn1_3.png")
        self.image4 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\imgIn1_4.png")


        img1 = Label(p6Frame,image=self.image1,height=tam,width=tam)
        img1.grid(row=0,column=0,columnspan=1,rowspan=1,padx=3,pady=3)

        img2 = Label(p6Frame,image=self.image2,height=tam,width=tam)
        img2.grid(row=0,column=1,columnspan=1,rowspan=1,padx=3,pady=3)

        img3 = Label(p6Frame,image=self.image3,height=tam,width=tam)
        img3.grid(row=1,column=0,columnspan=1,rowspan=1,padx=3,pady=3)

        img4 = Label(p6Frame,image=self.image4,height=tam,width=tam)
        img4.grid(row=1,column=1,columnspan=1,rowspan=1,padx=3,pady=3)
        
        
        # Frame 4
        
        # Imagen:
        self.punteroImagen=2
        def cambiarTextoEImagenF4(evento):
            i=self.punteroImagen

            # Cambio de imagenes
            global imagF4
            imagF4=PhotoImage(file=f"Python\src\gestorGrafico\Imagenes\imgInF4.{i}.png")     
   
            ImagenF4.config(image=imagF4)
            
            # Cambio de puntero  
            i+= 1
            n = 2 # numero de grupo de fotos en la carpeta imagenes, cuando se tengan todas debe ser 5
            if i ==(n+1):
                self.punteroImagen= 1
            else:
                self.punteroImagen=i
        
        self.imagenF41 =PhotoImage(file="Python\src\gestorGrafico\Imagenes\imgInF4.1.png")
        
        ImagenF4 = Label(p4Frame,image=self.imagenF41,width=300,wraplength=160,highlightbackground="black",highlightthickness=2)
        ImagenF4.pack(side="top",pady=3)
        ImagenF4.bind("<Enter>",cambiarTextoEImagenF4)
        
        # Texto descripcion
        
        descripTexto = Label(p4Frame,text="",font=("arial", 12, "bold"),bg="green",wraplength=400)
        descripTexto.pack(side="top",fill="x",pady=10)
        
        # Boton para pasar
        
        def cambioVentana():
            self.destroy()           
            ventana.abrirLog()
            
        
        botonIngreso=Button(p4Frame,text="Ingresar",command=cambioVentana)
        botonIngreso.pack(side="top",pady=20)
           
        
        # Creacion del menu :U
        ventana.menuBar = Menu(ventana)
        ventana.option_add("*tearOff",  False)
        ventana.config(menu=ventana.menuBar)
        menu1= Menu(ventana.menuBar)
        ventana.menuBar.add_cascade(label="Archivo",menu=menu1)
        menu1.add_command(label="Salir",command=lambda:ventana.destroy())
        
        textDescrip="Hola esto es un texto de prueba Hola esto es un texto de prueba Hola esto es un texto de prueba Hola esto es un texto de prueba Hola esto es un texto de prueba Hola esto es un texto de prueba Hola esto es un texto de prueba"
        menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))
        