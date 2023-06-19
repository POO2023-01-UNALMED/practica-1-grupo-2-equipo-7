from tkinter import *

class VentInicio(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)       
        self.pack()
        
        # Creacion de Frames

        p1Frame=Frame(self,height=450,width=425,bg="#cedae0")
        p1Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=(5,0),pady=5)
        p1Frame.grid_propagate(False)

        p2Frame=Frame(self,height=450,width=425,bg="#cedae0")
        p2Frame.grid(row=0,column=1,columnspan=1,rowspan=1,padx=(0,5),pady=5)
        p2Frame.grid_propagate(False)

        p3Frame=Frame(p1Frame,height=70,width=415,bg="#085870")
        p3Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p3Frame.pack_propagate(False)

        p4Frame=Frame(p1Frame,height=365,width=415,bg="#cedae0")
        p4Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p4Frame.pack_propagate(False)

        p5Frame=Frame(p2Frame,height=100,width=415,bg="yellow")
        p5Frame.grid(row=0,column=0,columnspan=1,rowspan=1,padx=5,pady=(5,3))
        p5Frame.pack_propagate(False)

        p6Frame=Frame(p2Frame,height=335,width=335,bg="#085870")
        p6Frame.grid(row=1,column=0,columnspan=2,rowspan=1,padx=5,pady=(3,5))
        p6Frame.grid_propagate(False)

        # Frame 3 Saludo bienvenida
        mensaje="Hola, bienvenido al sistemas de matricula de materias S.M.M"
        mensajeBienv = Label(p3Frame,text=mensaje,font=("arial", 18, "bold"),bg="#085870",wraplength=415,fg="#cedae0")
        mensajeBienv.pack(expand=True)


        # Frame 5 Bibliografia de cada desarrollador
        bibi1="Mi nombre es Mateo Álvarez Murillo, nací en Medellín el 15 de agosto del 2004. Actualmente, curso el tercer semestre de ingeniería de sistemas e informática. Comencé a programar en el equipo de robótica de mi institución, me apasiona el desarrollo de software y todo el mundo de la informática."
        bibi2="Soy Sebastián Ocampo Galvis, nacido en Medellín un 24 de Septiembre de 2003. Estoy cursando tercer semestre en ingeniería de sistemas en la Universidad Nacional de Colombia. Soy un gran aficionado al deporte y a la informática desde hace muchos años."
        bibi3="Mi nombre es Ana Sofía Gómez, nací el 4 de Marzo del 2005 en Medellín. Actualmente me encuentro cursando mi segundo semestre de Ingeniería de Sistemas e Informática en la Universidad Nacional. Aparte de lo que involucra la carrera, disfruto mucho de la repostería."
        bibi4="Mi nombre es Efrain Gomez Ramirez, nací el 14 de Mayo del 2004 en Mompos. Actualmente me encuentro cursando mi tercer semestre de Ingeniería de Sistemas e Informática en la Universidad Nacional. Disfruto participar en eventos de programacion competitiva y aprender sobre algoritmia."
        bibi5="In4 congue, metus eget venenatis condimentum, tellus dolor facilisis risus, non blandit risus dolor sed quam. Nunc eu iaculis magna. Vivamus ac vestibulum ipsum4"

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
            n =4 # numero de grupo de fotos en la carpeta imagenes, cuando se tengan todas debe ser 5
            if i ==n:
                self.punteroIntergrante= 0
            else:
                self.punteroIntergrante=i
            

        biblioTexto = Label(p5Frame,text=bibi1,font=("arial", 10),bg="#cedae0",wraplength=405,highlightbackground="#085870",highlightthickness=2)
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
        
        ImagenF4 = Label(p4Frame,image=self.imagenF41,width=300,wraplength=160,highlightbackground="#085870",highlightthickness=4)
        ImagenF4.pack(side="top",pady=3)
        ImagenF4.bind("<Enter>",cambiarTextoEImagenF4)
        
        # Texto descripcion
        
        descripTexto = Label(p4Frame,text="",font=("arial", 12, "bold"),bg="#cedae0",wraplength=400)
        descripTexto.pack(side="top",fill="x",pady=10)
        
        # Boton para pasar
        
        def cambioVentana():
            self.destroy()           
            ventana.abrirLog()
            
        
        botonIngreso=Button(p4Frame,text="Ingresar",command=cambioVentana,bg="#085870",font=("arial", 12, "bold"),fg="#cedae0")
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
        