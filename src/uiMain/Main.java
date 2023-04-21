package uiMain;

import java.util.Scanner;
import gestorAplicacion.administracion.Grupo;
import gestorAplicacion.administracion.Horario;
import gestorAplicacion.administracion.Materia;
import gestorAplicacion.administracion.Salon;
import gestorAplicacion.usuario.Coordinador;
import gestorAplicacion.usuario.Estudiante;
import gestorAplicacion.usuario.Profesor;
import gestorAplicacion.usuario.Usuario;

import java.net.SecureCacheResponse;
import java.util.ArrayList;
import java.util.Arrays;

import baseDatos.Deserializador;

public class Main {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        Boolean continuar=true;
        System.out.println("Bienvenido al Portal de Servicios Acacémicos S.M.M");
        while(continuar){
            //Aun no esta contruido la interfaz (mensajes bonitos en la terminal)
            //Por aquí irá el menu con las opciones
            System.out.println("A continuación encontrará los diferentes servicios ofrecidos por la plataforma.");
            System.out.println("Ingrese la opcion deseada: \n1. Matricular Materia.\n2. Generar Horario.\n3. Eliminar o agregar Materia / Grupo.\n4. Desmatricular Alumno. \n5. Busqueda y Postulación de Becas.");
            int opcion = scanner.nextInt();
            switch(opcion) {
            case 1:
                System.out.println("Has seleccionado la opción 1 (Matricular materia)");
                matricularMateria();
                break;
            case 2:
                System.out.println("Has seleccionado la opción 2 (Generar Horario).");
                System.out.println("Esta Opcion te permitira generar una horario aleatorio segun unas materias dadas.");
                
                boolean salir = true;
                while(salir){

                    
                    System.out.println("Elija como quiere seleccionar las materias: \n1.Ver la lista de materias. \n2.Buscar por criterio (Facultad - Creditos - Codigo). \n3.Salir");
                    int opt=scanner.nextInt();
                    

                    // Ver la lista de materias
                    if (opt==1){
                        fusionImpresiones(Materia.getMateriasTotales());
                    }
    
                    // Ver lista pero con filtro
                    else if (opt ==2){
                        System.out.println("Por cual criterio quiere buscar: \n1. Facultad. \n2. Creditos. \n3. Codigo");
                        int opt2=scanner.nextInt();
                        
                        if (opt2==1){
                            System.out.println("Ingrese la facultad: ");
                            String opt3=scanner.nextLine();
    
                            fusionImpresiones(mostrarMateriasConFiltro(opt2, opt3));
                        }
                        else if (opt2 == 2){
                            System.out.println("Ingrese el numero de creditos: ");
                            String opt3=scanner.nextLine();
    
                            fusionImpresiones(mostrarMateriasConFiltro(opt2, opt3));

                        }
                        else if (opt2 == 3){
                            System.out.println("Ingrese el codigo: ");
                            String opt3=scanner.nextLine();
    
                            fusionImpresiones(mostrarMateriasConFiltro(opt2, opt3));

                        }
                    
                    // Salir
                    } else{
                        salir = false;
                    }
                }
                break;
            case 3:
                System.out.println("Has seleccionado la opción 3 (Eliminar o agregar Materia / Grupo).");
                System.out.println("Ingrese la opción que se ajuste a su búsqueda:\n1. Agregar Materia.       2.Eliminar Materia.\n3.Agregar Grupo.          4.Eliminar Grupo.");
                int opcion_3 = scanner.nextInt();
                if(opcion_3 == 1){
                    System.out.println("Has seleccionado la opción 1 (Agregar materia.)");
                    //Funcionalidad agregar materia//
                }
                else if(opcion_3 == 2){
                    System.out.println("Has seleccionado la opción 2 (Eliminar materia.)");
                    //Funcionalidad eliminar materia//
                }
                else if(opcion_3 == 3){
                    System.out.println("Has seleccionado la opción 3 (Agregar grupo.)");
                    boolean salida = false;
                    while(!salida) {
	                    System.out.println("Ingrese la materia a la cual desea agregar el grupo (Con mayúscula inicial solo en la primera palabra).\nSi desea salir ingrese la palabra Salir:");
	                    String materiaStr = scanner.nextLine();
	                    if (materiaStr=="Salir") {
	                    	salida=true;
	                    	break;
	                    }
	                    Materia materiaSel = null;
	                    for (Materia materia:Materia.materiasTotales) {
	                    	if (materia.getNombre()==materiaStr) {
	                    		materiaSel = materia;
	                    		break;
	                    	}
	                    }
	                    if (materiaSel==null) {
	                    	System.out.println("La materia no ha sido encontrada. Ingrese un nombre de una materia valida.");
	                    	continue;
	                    }
	                    Profesor profesorSel = null;
		                while(true) {
		                    System.out.println("Ingrese el método por el cual quiere asignar el profesor para el nuevo grupo:\n1. Seleccionar del listado de profesores.\n2. Asignar un profesor nuevo.\n3. Salir");
		                    int opcion_profe = scanner.nextInt();
		                    
		                    if (opcion_profe==1) {
		                    	System.out.println("Seleccione uno de los siguientes profesores");
		                    	System.out.print(Profesor.mostrarProfesMateria(materiaSel));
		                    	int seleccionProfe = scanner.nextInt();
		                    	ArrayList<Profesor> preProfes = Profesor.profesoresDeMateria(materiaSel);
		                    	profesorSel = preProfes.get(seleccionProfe-1);
		                    	break;
		                    }
		                    
		                    else if(opcion_profe==2){
		                    	System.out.println("Ingrese el nombre completo del profesor: ");
		                    	String nomb = scanner.nextLine();
		                    	System.out.println("Ingrese la facultad a la que pertenece el profesor: ");
		                    	String facu = scanner.nextLine();
		                    	System.out.println("Ingrese las materias (separadas por comas con su respectivo espacio) para las cuales el profesor está capacitado:");
		                    	String materias = scanner.nextLine();
		                    	String[] mate = materias.split(", ");
		                    	ArrayList<Materia> mates = new ArrayList<Materia>();
		                    	for (String smateria:mate) {
		                    		for (Materia materia:Materia.getMateriasTotales()) {
		                    			if (smateria==materia.getNombre()) {
		                    				mates.add(materia);
		                    				break;
		                    			}
		                    		}
		                    	}
		                    	profesorSel = new Profesor(nomb,facu,new Horario(),mates);
		                    	break;
		                    }
		                    else if(opcion_profe==3){
		                    	salida = true;
		                    	break;
		                    }
		                    else {
		                    	System.out.println("Valor erroneo. Ingrese un valor válido.");
		                    }
	                	}
		                if(salida) {break;}
		                
			            System.out.println("Ingrese el horario de clase del grupo.\nPor cada sesión de clase ingrese un horario con el formato d-hi-hf, donde d es el número del día de la semana, hi es la hora inicial y hf es la hora final.\nSepare cada uno de estos por comas con su respectivo espacio:");
			            String hor = scanner.nextLine();
			            String[] horario = hor.split(", ");
			            ArrayList<String> horarioSel= new ArrayList<String>(Arrays.asList(horario));
			            System.out.println("Ingrese la cantidad de cupos con la que contará el grupo:");
			            int cuposSel = scanner.nextInt();
			            Salon salonSel = null;
			            while(true) {
			            	System.out.println("Ingrese el salón donde se darán las sesiones de clase del grupo.\nSi desea salir ingrese la palabra Salir:");
			            	String nomSalon = scanner.nextLine();
			            	if (nomSalon=="Salir") {
			            		salida = true;
			            		break;
			            	}
			            	for (Salon salon:Salon.salones) {
			            		if(nomSalon==salon.getLugar()) {
			            			salonSel = salon;
			            			break;
			            		}
			            	}
			            	if (salonSel==null) {
			            		System.out.println("El salón ingresado no existe. Ingrese un salón válido.");
			            	}
			            }
			            if(salida) {break;}
			            int numSel = materiaSel.getGrupos().size();
			            materiaSel.agregarGrupo(numSel, profesorSel, horarioSel, cuposSel, salonSel);
			            System.out.println("El grupo "+numSel+" de la materia "+materiaSel+" ha sido asignado correctamente");
			            break;
                    }
                }
                else if(opcion_3 == 4){
                    System.out.println("Has seleccionado la opción 4 (Eliminar grupo.)");
                    boolean salida = false;
                    while(!salida) {
                    	System.out.println("ingrese la materia a la cual le desea eliminar un grupo.\nSi desea salir escriba la palabra Salir:");
                    	String materiaNom = scanner.nextLine();
                    	Materia materiaSel = null;
                    	if(materiaNom=="Salida") {
                    		break;
                    	}
                    	for (Materia materia:Materia.getMateriasTotales()) {
                    		if (materiaNom==materia.getNombre()) {
                    			materiaSel = materia;
                    			break;
                    		}
                    	}
                    	if(materiaSel==null) {
                    		System.out.println("La materia ingresada no existe. Ingrese una materia válida.");
                    		continue;
                    	}
                    	while(true) {
                    		System.out.println("Ingrese el número del grupo que desea eliminar\nSi desea salir escriba el número 0");
                    		int numSel = scanner.nextInt();
                    		if (numSel<0||numSel>materiaSel.getGrupos().size()) {
                    			System.out.println("El número de grupo ingresado no existe. Ingrese el número de un grupo válido.");
                    		}
                    		else if(numSel==0) {
                    			salida = true;
                    			break;
                    		}
                    		else {
                    			materiaSel.eliminarGrupo(numSel);
                    			System.out.println("El grupo "+numSel+" de la materia "+materiaSel+" ha sido eliminado con éxito");
                    			break;
                    		}
                    		break;
                    	}
                    }
                }
                else if(0 > opcion_3 || opcion_3 > 4){
                    System.out.println("Opción inválida.");
                    continue;
                }
                break;
            case 4:
                System.out.println("Has seleccionado la opción 4 (Desmatricular Alumno).");
                Estudiante estudiante = null;
                while (true){
                    System.out.println("Elija como quiere seleccionar el alumno: \n1.Ver la lista de estudiantes. \n2.Buscar estudiante por ID y nombre. \n3.Salir");
                    int eleccion = scanner.nextInt();
                    Scanner scanner2 = new Scanner(System.in);
                    if (eleccion == 1){
                        System.out.println("Elija el número del estudiante");
                        System.out.println(Estudiante.mostrarEstudiantes());
                        int numeroEstudiante = scanner2.nextInt();
                        estudiante = Estudiante.getEstudiantes().get(numeroEstudiante-1);
                    }
                    else if(eleccion == 2){
                        System.out.print("Ingrese el nombre del estudiante: ");
                        String nombre = scanner2.nextLine();
                        System.out.print("Ingrese el id del estudiante: ");
                        long id = scanner2.nextLong();
                        int numeroEstudiante = Estudiante.buscarEstudiante(nombre, id);
                        if (numeroEstudiante != -1){
                            System.out.println("El estudiante ha sido encontrado\n");
                            estudiante = Estudiante.getEstudiantes().get(numeroEstudiante);
                        }
                        else{
                            System.out.println("El estudiante no ha sido encontrado, busque nuevamente\n");
                        }
                    }
                    else if(eleccion == 3){
                        break;
                    }
                    else{
                        System.out.println("Ingresa una opción valida\n");
                    }
                    scanner2.close();
                }

                while(true && estudiante != null){
                    Scanner scanner2 = new Scanner(System.in);
                    while(true){
                        System.out.println("Seleccione de que quiere desmatricular al estudiante:");
                        System.out.println("1. Desmatricular de una materia \n2. Desmatricular del sistema \n3. Retroceder");
                        int opcion_1 = scanner2.nextInt();
                        if (opcion_1 == 1){
                            Scanner scanner3 = new Scanner(System.in);
                            while (true){
                                
                                System.out.println("Elija como quiere seleccionar la materia y el grupo");
                                System.out.println("1. Ver lista de materias y grupos \n2. Buscar materia y grupo");
                                int opcion_2 = scanner3.nextInt();
                                switch(opcion_2){
                                    case 1:
                                    System.out.println(estudiante.mostrarMaterias());
                                    System.out.print("Ingrese el numero de la materia: ");
                                    int numeroMateria = scanner3.nextInt();
                                    System.out.print("Ingrese el numero del grupo: ");
                                    int numeroGrupo = scanner3.nextInt();
                                    Grupo grupo = estudiante.getMaterias().get(numeroMateria).getGrupos().get(numeroGrupo);
                                    if (grupo.existenciaEstudiante(estudiante)){
                                        grupo.eliminarEstudiante(estudiante);
                                        estudiante.getHorario().liberarHorario(grupo.getHorario());
                                        System.out.println("El estudiante ha sido desmatriculado de la materia y el grupo");
                                        break;
                                    }
                                    else{
                                        System.out.println("El estudiante no está matriculado en el grupo");
                                    }
                                    break;
                                    case 2:
                                    System.out.print("Ingrese el nombre de la materia: ");
                                    String nombreMateria = scanner3.nextLine();
                                    Materia materia = estudiante.buscarMateriaPorNombre(nombreMateria);
                                    if (materia != null){
                                        Grupo grupoEstudiante = materia.buscarGrupoDeEstudiante(estudiante);
                                        grupoEstudiante.eliminarEstudiante(estudiante);
                                        estudiante.getHorario().liberarHorario(grupoEstudiante.getHorario());
                                        System.out.println("El estudiante ha sido desmatriculado de la materia y el grupo");
                                        break;
                                    }
                                    else{
                                        System.out.println("El estudiante no tiene matriculada esta materia");
                                    }                                   
                                }
                                scanner3.close();
                            }
                        }
                        else if(opcion_1 == 2){
                            estudiante.desmatricularMaterias();
                            System.out.println("El estudiante ha sido desmatriculado del sistema");
                            break;
                        }
                        else if(opcion_1 == 3){
                            break;
                        }
                        else{
                            System.out.println("Ingresa una opcion valida\n");
                        }
                    }
                    scanner2.close();
                    break;
                }

                break;
            case 5:
                //El nombre aun se puede cambiar
                System.out.println("Has seleccionado la opción 5 (Busqueda y Postulación Becas).");
                break;
            default:
                System.out.println("Opción inválida");
                System.out.println("Desea continuar?");
                System.out.println("Opción 1- SI");
                System.out.println("Opción 2- NO");
                System.out.println("Por favor ingrese la opción deseada");
                int continuarint=scanner.nextInt();
                if (continuarint==1){
                    continue;
                } else{
                continuar=false;
                }
            }
        }

        scanner.close();
    }

    //METODOS USADOS EN MATRICULAR MATERIA
    //La parte 1 de matricular materia es para seleccionar al estudiante
    public static void matricularMateria(){
        Scanner scn = new Scanner(System.in);
        boolean salir=false;
    	while(salir==false){
            Boolean invalido=false;
            System.out.println("Desea buscar al estudiante mediante una lista o mediante su ID o su nombre?");
            System.out.println("Ingrese la opción deseada: \n1- Lista de estudiantes disponibles\n2- Buscar al estudiante");
            int opcion1=scn.nextInt();
            //Opcion Lista de estudiantes
            if (opcion1==1){
                /*
                 * Opcion 1:
                 * Busqueda de estudiante mediante la lista completa de estudiantes
                 * Quitando los estudiantes que ya no pueden inscribir mas materias
                 * Quitando los estudiantes que no tienen la matricula pagada
                 */
                ArrayList<Estudiante> totalEstudiantes=new ArrayList<Estudiante>(Estudiante.getEstudiantes());
                for (int i=0;i<totalEstudiantes.size();i++){
                    Estudiante est=totalEstudiantes.get(i);
                    if (est.isMatriculaPagada()!=true){
                        totalEstudiantes.remove(i);
                    } else if (est.getCreditos()==Coordinador.getLimitesCreditos()){
                        totalEstudiantes.remove(i);
                    }
                    if (i==totalEstudiantes.size()-1){
                        break;
                    }
                }
                System.out.println("Lista de estudiantes disponibles para matricular: ");
                for (int j=1;j<totalEstudiantes.size()+1;j++){
                    Estudiante est=totalEstudiantes.get(j-1);
                    System.out.println(j+" Nombre: "+est.getNombre()+" ID: "+est.getId());
                }
                int opcion3 = scn.nextInt();
                if (opcion3<totalEstudiantes.size() && opcion3>0){
                    Estudiante seleccionado=totalEstudiantes.get(opcion3-1);
                    System.out.println("Estudiante seleccionado, nombre: "+seleccionado.getNombre()+" ID: "+seleccionado.getId());
                    matricularMateriaParte2(seleccionado);
                    salir=true;
                }else{
                    invalido=true;
                }

            }else if(opcion1==2){
                /*
                 * Opcion 2:
                 * Buscar al estudiante mediante su id y su nombre
                 * si el estudiante que se desea buscar no exite se le notificará al usuario
                 */
                System.out.println("Por favor ingrese el nombre del estudiante: ");
                String nombre=scn.nextLine();
                System.out.println("Por favor ingrese el ID del estudiante: ");
                long id=scn.nextLong();
                int index=Estudiante.buscarEstudiante(nombre, id);
                if (index==-1){
                    System.out.println("Estudiante no encontrado");
                    invalido=true;
                }else{
                    Estudiante seleccionado=Estudiante.getEstudiantes().get(index);
                    System.out.println("Estudiante seleccionado, nombre: "+seleccionado.getNombre()+" ID: "+seleccionado.getId());
                    matricularMateriaParte2(seleccionado);
                }
            }else{
                /*
                 * Opcion invalida:
                 * Desea salir o continuar?
                 */
                invalido=true;
            }
            if (invalido){
                System.out.println("Opción invalida");
                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opción deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion2=scn.nextInt();
                if (opcion2!=1){
                    salir=true;
                }
            }
        }
        scn.close();
    }
    //La parte 2 de matricular materia es dependiendo del estudiante cuales materias puede ver
    public static void matricularMateriaParte2(Estudiante estudiante){
        Scanner scanner = new Scanner(System.in); 
        boolean salir=false;
        while(salir==false){
            Boolean invalido=false;
            System.out.println("Como desea buscar la materia?\n1- Mediante una lista de las materias disponibles\n2- Mediante una busqueda manual");
            int opt=scanner.nextInt();
            ArrayList<Materia> materiasTotales=new ArrayList<Materia>(Materia.getMateriasTotales());
            if (opt==1){
                ArrayList<Materia> materiasDisponibles=new ArrayList<Materia>();

                /*
                * PRIMERO: 
                * Quitamos las materias que el estudiante no puede ver por los prerrequisitos
                * Revisamos cuales materias al ser matriculadas al estudiante le hacen sobrepasar el limite de creditos
                * Y tambien revisamos la disponibilidad en los cupos de la materia
                */
                int limitesCreditos=Coordinador.getLimitesCreditos();
                for (int i=0; i<materiasTotales.size();i++){
                    Materia materia=materiasTotales.get(i);
                    boolean anadir=true;
                    for (int j=0; j<materia.getPrerrequisitos().size();j++){
                        Materia prerrequisito=materia.getPrerrequisitos().get(j);
                        if (estudiante.buscarMateriaEnInscritas(prerrequisito.getNombre(), prerrequisito.getCodigo())){
                            anadir=false;
                            break;
                        }
                    }
                    if (materia.getCupos()<=0){
                        anadir=false;
                    }else if (estudiante.getCreditos()+materia.getCreditos()>limitesCreditos){
                        anadir=false;
                    }
                    if (anadir){
                        materiasDisponibles.add(materia);
                    }
                }

                /*
                * SEGUNDO:
                * En esta parte le mostramos una lista de posibles opciones a matricular
                * Dependiendo de la respuesta del usuario el ciclo se romperá o continuará hasta que el usuario quiera
                */
                System.out.println("Lista de materias disponibles para matricular: ");
                for (int m=1;m<materiasDisponibles.size()+1;m++){
                    Materia materia=materiasDisponibles.get(m-1);
                    System.out.println(m+" Nombre: "+materia.getNombre()+" Cupos: "+materia.getCupos());

                }
                System.out.println("Por favor ingrese el numero correspondiente a la materia que desea matricular");
                int eleccion=scanner.nextInt();
                if (0<eleccion-1 && eleccion-1<materiasDisponibles.size()){
                    Materia seleccionada = materiasDisponibles.get(eleccion-1);
                    System.out.println("Materia seleccionada "+seleccionada.getNombre());
                    matricularMateriaParte3(estudiante, seleccionada);
                    salir=true;
                } else{
                    invalido=true;
                }

            }else if(opt==2){
                /*
                 * Opcion 2:
                 * Buscar la matetia mediante su codigo y su nombre
                 * si la materia que se desea buscar no exite se le notificará al usuario
                 */
                System.out.println("Por favor ingrese el nombre de la materia deseada: ");
                String nombre=scanner.nextLine();
                System.out.println("Por favor ingrese el codigo de la materia deseada: ");
                int codigo=scanner.nextInt();
                int index=Materia.buscarMateria(nombre, codigo);
                if (index==-1){
                    invalido=true;
                }else{
                    Materia seleccionada=materiasTotales.get(index);
                    System.out.println("Materia seleccionada "+seleccionada.getNombre());
                    matricularMateriaParte3(estudiante, seleccionada);
                    salir=true;
                }
            }else{
                //Opcion invalida, desea continuar?
                System.out.println("Materia no encontrada");
                invalido=true;
            }
            if (invalido){
                System.out.println("Opción invalida");
                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opción deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opt2=scanner.nextInt();
                if (opt2!=1){
                    salir=true;
                }
            }
        }
        
        
        scanner.close();
    }
    //La parte 3 de matricular materia es para finalizar la funcionalidad
    public static void matricularMateriaParte3(Estudiante estudiante, Materia materia){
        Scanner scanner=new Scanner(System.in);
        boolean salir=false;
        while (salir==false){
            Boolean invalido=false;
            ArrayList<Grupo> gruposDisponibles=new ArrayList<Grupo>(materia.getGrupos());
            for (int i=0;i<gruposDisponibles.size();i++){
                Grupo grp=gruposDisponibles.get(i);
                if (grp.getCupos()==0){
                    gruposDisponibles.remove(i);
                }
                if (i==gruposDisponibles.size()-1){
                    break;
                }
            }
            System.out.println("Grupos disponibles para matricular: ");
            for (int j=0;j<gruposDisponibles.size();j++){
                Grupo grp=gruposDisponibles.get(j);
                System.out.println((j+1)+" Grupo #"+grp.getNumero()+ " cupos: "+grp.getCupos()+" Profesor: "+grp.getProfesor().getNombre());
            }
            int opt3=scanner.nextInt();
            if (opt3>0 && opt3<gruposDisponibles.size()-1){
                Grupo grupoSeleccionado=gruposDisponibles.get(opt3-1);
                ArrayList<Materia> materiasInscritas=new ArrayList<Materia>(estudiante.getMaterias());
                materiasInscritas.add(materia);
                grupoSeleccionado.agregarEstudiante(estudiante);
                grupoSeleccionado.getMateria().setCupos(grupoSeleccionado.getMateria().getCupos()-1);
                grupoSeleccionado.setCupos(grupoSeleccionado.getCupos()-1);
                estudiante.setCreditos(estudiante.getCreditos()+materia.getCreditos());
                estudiante.setMaterias(materiasInscritas);
                String imprimir="Materia "+materia.getNombre()+" - grupo #"+grupoSeleccionado.getNumero();
                System.out.println(imprimir+ ". Ha sido matriculado al estudiante: "+estudiante.getNombre());
                break;
            }else{
                invalido=true;
            }
            System.out.println("Desea visualizar el horario del estudiante?: \n1- Sí\n2- No");
            int opcion=scanner.nextInt();
            if (opcion==1){
                estudiante.getHorario().mostrarHorario();
            }
            if (invalido){
                System.out.println("Opción invalida");
                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opción deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opt2=scanner.nextInt();
                if (opt2!=1){
                    salir=true;
                }
            }

        }
        scanner.close();
    }
    //Esto me lo pidio efrain
    public static void matricularMateriaParte4(Estudiante estudiante, Grupo grupo){
        Scanner scanner=new Scanner(System.in);
        ArrayList<Materia> materiasInscritas=new ArrayList<Materia>(estudiante.getMaterias());
        materiasInscritas.add(grupo.getMateria());
        grupo.agregarEstudiante(estudiante);
        grupo.getMateria().setCupos(grupo.getMateria().getCupos()-1);
        grupo.setCupos(grupo.getCupos()-1);
        estudiante.setCreditos(estudiante.getCreditos()+grupo.getMateria().getCreditos());
        estudiante.setMaterias(materiasInscritas);
        String imprimir="Materia "+grupo.getMateria().getNombre()+" - grupo #"+grupo.getNumero();
        System.out.println(imprimir+ ". Ha sido matriculado al estudiante: "+estudiante.getNombre());
        System.out.println("Desea visualizar el horario del estudiante?: \n1- Sí\n2- No");
        int opcion=scanner.nextInt();
        if (opcion==1){
            estudiante.getHorario().mostrarHorario();
        }
        scanner.close();


}

    // METODOS USADOS EN GENERAR HORARIO: 
    // - Mostrar Materias confiltro
    public static ArrayList<Materia> mostrarMateriasConFiltro(int opcionFiltro,String filtro){
        /*
        * Muestra solo las materias que cumplan el filtro dado (segundo parametro)
        * Retorna:
        * Un arreglo que sera una lista de las materias que pasaron por el filtro 
        */

    
        ArrayList<Materia> listaFiltrada=new ArrayList<Materia>();

        // filtro == 1 == facultad
        if (opcionFiltro == 1){
            for (Materia pMateria:Materia.getMateriasTotales()){
                if(pMateria.getFacultad().equalsIgnoreCase(filtro)){
                    listaFiltrada.add(pMateria);
                }
            }
        }
        // filtro == 2 == Creditos 
        else if (opcionFiltro == 2){
            for (Materia pMateria:Materia.getMateriasTotales()){
                if(pMateria.getCreditos()==Integer.parseInt(filtro)){
                    listaFiltrada.add(pMateria);
                }
            }
        }
        // filtro == 3 == Codigo 
        else if (opcionFiltro == 3){
            for (Materia pMateria:Materia.getMateriasTotales()){
                if(pMateria.getCodigo()==Integer.parseInt(filtro)){
                    listaFiltrada.add(pMateria);
                }
            }
        }
        
        return listaFiltrada;

    }
    
    // - Mostrar materias por consola
    public static void imprimirListaPorConsola(ArrayList<Materia> ListaAMostrar){
        /*
         * Toma una lista y la imprime con un formato especial
         */
        // imprimir Lista
        
        int con =1;
        System.out.printf("%-3s %-40s %-10s %-10s%n", "Num", "Nombre", "Facultad","Codigo");
        
        for (Materia pMateria:ListaAMostrar){
            System.out.printf("%-3n %-40s %-10s %-15n%n",con,pMateria.getNombre(),pMateria.getFacultad(),pMateria.getCodigo());
            con++;
        }       
    }
    
    // - Muestra el horario generado 
    public static void imprimirHorarioGenerado(ArrayList<Materia> ListaAGenerar){
        /*
         * Muestra el horario generado ademas de que recoge la informacion para costruirlo
         */

        // Elecciones del usuario
        Scanner scanner=new Scanner(System.in);
        ArrayList<Materia> listaMateriasAGenerar = new ArrayList<Materia>();

        System.out.println("Indique uno por uno los numeros de la materias que quiere incluir en su horario y envie 0 cuando termine: ");
        boolean flag = true;
        while(flag){
            System.out.print("-> ");
            int opt3=scanner.nextInt();
            if (opt3!=0){
                listaMateriasAGenerar.add(ListaAGenerar.get(opt3-1));
            }
            else{
                flag = false;
            }
        }
        Object[] informacion = Coordinador.crearHorarioAleatorio(listaMateriasAGenerar);
        
        if ((boolean)informacion[0]){
            Horario pHorario= (Horario)informacion[1];
        }
        else{
            System.out.println("No fue posible generar el horario, ya que "+((Materia)informacion[2]).getNombre()+" es un obstaculo");
        }

        // System.out.println("Desea conservar el horario?\n1. Si \n2. No");
        // int opt4=scanner.nextInt();
        // if (opt4 == 1){
        //     System.out.println("Escoja el numero del estudiante a asignar: ");
        //     Estudiante.mostrarEstudiantes();
        //     int opt4=scanner.nextInt();
            
        }
    
    // Conexion de dos metodos
    public static void fusionImpresiones(ArrayList<Materia> listaObjetivo){
        /*
         * La idea es factorizar un poco mas el codigo, al recibir un arreglo y aplicarle dos metodos ya establecidos
         */
        if (listaObjetivo.size()!=0){
            imprimirListaPorConsola(listaObjetivo);
            imprimirHorarioGenerado(listaObjetivo);
        }
        else{
            System.out.println("Ningun elemente hizo encontrado con el filtro dado");
        }
    }

}

