package uiMain;

import java.util.Scanner;
import gestorAplicacion.administracion.Grupo;
import gestorAplicacion.administracion.Horario;
import gestorAplicacion.administracion.Materia;
import gestorAplicacion.administracion.Salon;
import gestorAplicacion.administracion.Beca;
import gestorAplicacion.usuario.Coordinador;
import gestorAplicacion.usuario.Estudiante;
import gestorAplicacion.usuario.Profesor;
import gestorAplicacion.usuario.Usuario;

import java.util.ArrayList;
import java.util.Arrays;
// import java.util.Random; por el momento no se usa aqui

import baseDatos.Serializador;
import baseDatos.Deserializador;

public class Main implements Interfaz{
    public static void main(String[] args){
        Deserializador.deserializarListas();
        Scanner scanner=new Scanner(System.in);
        Boolean continuar=true;
        Boolean logueado = false;
        System.out.println("\nBienvenido al Portal de Servicios Academicos S.M.M");

        // Zona de Pruebas -------------------------------------------------------------------

        // for (Salon salon: Salon.getSalones()){
        //     System.out.println(salon.getLugar());
        //     System.out.println(salon.getAforo());
        // }
        // for (Materia materia: Materia.getMateriasTotales()){
        //     int suma=0;
        //     for (Grupo grupo: materia.getGrupos()){
        //         suma+=grupo.getCupos();
        //     }
        //     materia.setCupos(suma);
        // }

        // Profesor.getProfesores().get(19).setFacultad("Facultad de ciencias humanas y economica");
        // for(Profesor profe : Profesor.getProfesores()){
        //     System.out.println(profe.getFacultad());
        // }
        
        // for(Estudiante estudiantee : Estudiante.getEstudiantes()){
        //     System.out.println(estudiantee.getNombre());
        //     System.out.println(estudiantee.getFacultad());
        // }
        
        // Zona de Pruebas -------------------------------------------------------------------

        Usuario usuario = null;
        while(!logueado) {
        	Scanner scanner2 = new Scanner(System.in);
        	System.out.println("\nSeleccione como desea ingresar a la plataforma:\n1. Crear nuevo usuario.\n2. Ingresar usuario existente.");
        	int opcion_log = scanner.nextInt();
            scanner.nextLine();
        	if (opcion_log==1) {
        		String nomb;
        		boolean existe;
        		do {
        			System.out.println("Ingrese su nombre completo:\nSi desea salir introduzca la palabra Salir");
        			nomb = scanner2.nextLine();
        			if (nomb=="Salir") {
        				existe = false;
        			}
        			else if (Interfaz.existenciaUsuario(nomb)) {
        				System.out.println("Ya existe un usuario asociado a este nombre.");
        				existe=true;
        			}
        			else {
        				existe=false;
        			}
        		}while (existe);
        		System.out.println("Ingrese la facultad a la que pertenece:");
        		String facul = scanner2.nextLine();
        		System.out.println("Ingrese su contrasena:");
        		String cont = scanner2.nextLine();
        		long id = Interfaz.generarId();
        		usuario = new Coordinador(facul,id,nomb,cont);
        		System.out.println("Se ha creado un nuevo usuario a nombre de "+nomb+" con el id "+id+" asignado.\nRecuerde que este id sera con el que inicie sesion en este usuario de ahora en adelante");
        		logueado=true;
        		// scanner2.close();
        	}
        	else if(opcion_log==2) {
        		Scanner scanner3 = new Scanner(System.in);
        		boolean intentando = true;
        		while(intentando) {
        			System.out.println("Ingrese su id de usuario:\nSi desea salir escriba el numero 0.");
        			long id = scanner3.nextLong();
                    scanner3.nextLine();
        			if (id==0) {
        				break;
        			}
        			else if (id<10000||id>99999) {
        				System.out.println("Id invalido. Ingrese un id de 5 cifras.");
        			}
        			else if (!Interfaz.existenciaId(id)){
        				System.out.println("El id ingresado no corresponde a ningun usuario registrado en el sistema.");
        			}
        			else if (Interfaz.encontrarUsuario(id).getTipo()=="Estudiante") {
        				System.out.println("Error. Solo pueden ingresar coordinadores en la plataforma.");
        			}
        			else {
        				Coordinador coordinadorE = (Coordinador) Interfaz.encontrarUsuario(id);
        				boolean pwCorect = false;
        				while(!pwCorect){
        					System.out.println("Ingrese la contrasena:");
        					String cont = scanner3.nextLine();
        					if(!Interfaz.verificarPw(coordinadorE,cont)) {
        						while(true) {
        							System.out.println("La contrasena es incorrecta.\nDesea intentar nuevamente?\n1. Si.\n2. No.");
        							int opCf = scanner3.nextInt();
                                    scanner3.nextLine();
        							if (opCf==1) {	
        								break;
        							}
        							else if (opCf==2) {
        								pwCorect=true;
        								intentando = false;
        								break;
        								
        							}
        							else {
        								System.out.println("Valor invalido. Ingrese el numero de una de las opciones mencionadas.");
        							}
        						}
        					}
        					else {
        						System.out.println("Ha ingresado exitosamente al sistema.");
        						usuario = coordinadorE;
        						intentando=false;
        						logueado = true;				
        						break;
        					}
        				}
        			}
        		}
        		// scanner3.close();
        	}
        	else {
        		System.out.println("Valor invalido. Ingrese el numero de una de las opciones mencionadas");
        	}
        }
        while(continuar){
            //Aun no esta contruido la interfaz (mensajes bonitos en la terminal)
            //Por aqui ira el menu con las opciones
            System.out.println("\nA continuacion encontrara los diferentes servicios ofrecidos por la plataforma.");
            System.out.println("Ingrese la opcion deseada: \n1. Matricular Materia.\n2. Generar Horario.\n3. Eliminar o agregar Materia / Grupo.\n4. Desmatricular Alumno. \n5. Busqueda y Postulacion de Becas. \n6. Salir y Guardar");
            int opcion = scanner.nextInt();
            scanner.nextLine();
            switch(opcion) {
            case 1:
                System.out.println("Has seleccionado la opcion 1 (Matricular materia)");
                Interfaz.matricularMateria();
                break;
            case 2:
                System.out.println("Has seleccionado la opcion 2 (Generar Horario).");
                System.out.println("Esta Opcion te permitira generar una horario aleatorio segun unas materias dadas.");
                
                boolean salir = true;
                while(salir){

                    
                    System.out.println("Elija como quiere seleccionar las materias: \n1.Ver la lista de materias. \n2.Buscar por criterio (Facultad - Creditos - Codigo). \n3.Salir");
                    int opt=scanner.nextInt();
                    scanner.nextLine();
                    

                    // Ver la lista de materias
                    if (opt==1){
                        Interfaz.fusionImpresiones(Materia.getMateriasTotales());
                    }
    
                    // Ver lista pero con filtro
                    else if (opt ==2){
                        System.out.println("Por cual criterio quiere buscar: \n1. Facultad. \n2. Creditos. \n3. Codigo");
                        int opt2=scanner.nextInt();
                        scanner.nextLine();
                        
                        if (opt2==1){
                            System.out.println("Ingrese la facultad: ");
                            String opt3=scanner.nextLine();
    
                            // fusionImpresiones(mostrarMateriasConFiltro(opt2, opt3));
                            Interfaz.fusionImpresiones(Interfaz.mostrarMateriasConFiltro(opt2, opt3));

                            
                        }
                        else if (opt2 == 2){
                            System.out.println("Ingrese el numero de creditos: ");
                            String opt3=scanner.nextLine();
    
                            Interfaz.fusionImpresiones(Interfaz.mostrarMateriasConFiltro(opt2, opt3));

                        }
                        else if (opt2 == 3){
                            System.out.println("Ingrese el codigo o la parte del codigo a filtrar: ");
                            String opt3=scanner.nextLine();
    
                            Interfaz.fusionImpresiones(Interfaz.mostrarMateriasConFiltro(opt2, opt3));

                        }
                    
                    // Salir
                    } else{
                        salir = false;
                    }
                }
                break;
            case 3:
                System.out.println("Has seleccionado la opcion 3 (Eliminar o agregar Materia / Grupo).");
                System.out.println("Ingrese la opcion que se ajuste a su busqueda:\n1.Agregar Materia.       2.Eliminar Materia.\n3.Agregar Grupo.         4.Eliminar Grupo.");
                int opcion_3 = scanner.nextInt();
                scanner.nextLine();
                if(opcion_3 == 1){
                    System.out.println("Has seleccionado la opcion 1 (Agregar materia.)");
                    if(opcion_3 == 1){
                        boolean fin = false;
                        
                        while(!fin){
                            Scanner scanner3_1 = new Scanner(System.in);
                            System.out.println("Ingresa el nombre de la materia que desea agregar.");
                            String nombre = scanner3_1.nextLine();
                            for (Materia materia : Materia.getMateriasTotales()){
                                if (materia.getNombre().equals(nombre) == true){
                                    System.out.println("La materia que intenta crear, ya se existe actualmente.");
                                    fin = true;
                                }
                            }                      
                            System.out.println("Ingresa el codigo de la materia que desea agregar.");
                            int codigo = scanner3_1.nextInt();
                            scanner3_1.nextLine();
                            for (Materia materia : Materia.getMateriasTotales()){
                                if (materia.getCodigo() == codigo){
                                    System.out.println("El codigo que intenta asignarle a la materia, ya le corresponde a una existente.");
                                    fin = true;
                                }
                            }
                            System.out.println("Ingrese una breve descripcion de la materia.");
                            String descrip = scanner3_1.nextLine();
                            System.out.println("Ingresa los creditos que le asigna a la materia.");
                            int creditos = scanner3_1.nextInt();
                            scanner3_1.nextLine();
                            System.out.println("Ingrese la facultad a la que pertenece la materia");
                            String facu = scanner3_1.nextLine();
                            
                            System.out.println("Ingrese como desea crear la materia:");
                            System.out.println("1.Con prerrequisitos.       2.Sin prerrequisitos.");
                            int decision = scanner3_1.nextInt();
                            scanner3_1.nextLine();
                            if(decision == 1){                              
                                System.out.println("Ha escogido crear la materia con prerrequisitos.");
                                System.out.println("Ingrese los prerrequisitos que tiene la materia para poder ser inscritas por el estudiante (separadas por comas con su respectivo espacio).");
                                String prerreq = scanner3_1.nextLine();
                                String[] pReq = prerreq.split(", ");
                                ArrayList<Materia> pRequisitos = new ArrayList<Materia>();
                                for(String r: pReq){
                                    for(Materia materia:Materia.getMateriasTotales()){
                                        if (r.equals(materia.getNombre()) == true){
                                            pRequisitos.add(materia);
                                            
                                        }
                                        
                                    }
                                }
                                usuario.agregarMateria(nombre, codigo, descrip, creditos, facu, pRequisitos);
                                System.out.println("La materia "+ nombre + " ha sido creada con exito.");
                                break; 
                            }
                            else if(decision == 2){
                                System.out.println("Ha escogido crear la materia sin prerrequisitos.");
                                Materia materiaN = new Materia(nombre, codigo, descrip, creditos, facu);
                                System.out.println("La materia "+ nombre + " ha sido creada con exito.");
                                break; 
                            }
                            else if(0 > decision || decision > 2){
                                System.out.println("Opcion invalida.");
                                continue;
                            }
                            break;                               
                            
                        }
                        
                    }
                }
                else if(opcion_3 == 2){
                    System.out.println("Has seleccionado la opcion 2 (Eliminar materia.)");
                    boolean terminar = false;
                    while(!terminar){
                        Scanner scanner3_2 = new Scanner(System.in);
                        System.out.println("Ingresa el nombre de la materia que desea eliminar.");
                        String nomMat = scanner3_2.nextLine();
                        ArrayList<String> nombresMaterias = new ArrayList<String>();
                        for (Materia materia : Materia.getMateriasTotales()){
                            String a = materia.getNombre();
                            nombresMaterias.add(a);
                        }
                        if ((!nombresMaterias.contains(nomMat)) == false){
                            System.out.println("La materia que desea eliminar no existe en la base de datos.");
                            terminar = true;
                        }
                        for (Materia materia : Materia.getMateriasTotales()){
                            if (materia.getNombre().equals(nomMat) == true){
                                usuario.eliminarMateria(materia);
                                break;
                            }
                        }
                        System.out.println("La materia "+ nomMat + "ha sido eliminada con exito.");
                        break;                     
                    }                    
                }
                else if(opcion_3 == 3){
                    System.out.println("Has seleccionado la opcion 3 (Agregar grupo.)");
                    boolean salida = false;
                    while(!salida) {
                    	Scanner scanner3 = new Scanner(System.in);
	                    System.out.println("Ingrese la materia a la cual desea agregar el grupo.\nSi desea salir ingrese la palabra Salir:");
	                    String materiaStr = scanner3.nextLine();
	                    if (materiaStr.equals("Salir")) {
	                    	salida=true;
	                    	break;
	                    }
	                    Materia materiaSel = null;
	                    for (Materia materia:Materia.materiasTotales) {
	                    	if (materia.getNombre().equals(materiaStr)) {
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
		                	Scanner scanner4 = new Scanner(System.in);
		                    System.out.println("Ingrese el metodo por el cual quiere asignar el profesor para el nuevo grupo:\n1. Seleccionar del listado de profesores.\n2. Asignar un profesor nuevo.\n3. Salir");
		                    int opcion_profe = scanner4.nextInt();
                            scanner4.nextLine();
		                    
		                    if (opcion_profe==1) {
		                    	if(Profesor.profesoresDeMateria(materiaSel.getNombre()).size()==0) {
		                    		System.out.println("No existen profesores registrados capacitados para dictar la materia");
		                    	}
		                    	else {
		                    		System.out.println("Seleccione uno de los siguientes profesores");
		                    		System.out.print(Profesor.mostrarProfesMateria(materiaSel.getNombre()));
		                    		int seleccionProfe = scanner4.nextInt();
		                    		scanner4.nextLine();
		                    		ArrayList<Profesor> preProfes = Profesor.profesoresDeMateria(materiaSel.getNombre());
		                    		profesorSel = preProfes.get(seleccionProfe-1);
		                    		break;
		                    	}
		                    }
		                    
		                    else if(opcion_profe==2){
		                    	System.out.println("Ingrese el nombre completo del profesor: ");
		                    	String nomb = scanner4.nextLine();
		                    	System.out.println("Ingrese la facultad a la que pertenece el profesor: ");
		                    	String facu = scanner4.nextLine();
		                    	System.out.println("Ingrese las materias (separadas por comas con su respectivo espacio) para las cuales el profesor esta capacitado:");
		                    	String materias = scanner4.nextLine();
		                    	String[] mate = materias.split(", ");
		                    	ArrayList<Materia> mates = new ArrayList<Materia>();
		                    	for (String smateria:mate) {
		                    		for (Materia materia:Materia.getMateriasTotales()) {
		                    			if (smateria.equals(materia.getNombre())) {
		                    				mates.add(materia);
		                    				break;
		                    			}
		                    		}
		                    	}
		                    	profesorSel = new Profesor(nomb,facu,mates);
		                    	break;
		                    }
		                    else if(opcion_profe==3){
		                    	salida = true;
		                    	break;
		                    }
		                    else {
		                    	System.out.println("Valor erroneo. Ingrese un valor valido.");
		                    }
	                	}
		                if(salida) {break;}
		                ArrayList<String> horarioSel = null;
		                while(true) {
		                	Scanner scanHor = new Scanner(System.in);
		                	System.out.println("Ingrese el horario de clase del grupo.\nPor cada sesion de clase ingrese un horario con el formato d-hi-hf, donde d es el numero del dia de la semana, hi es la hora inicial y hf es la hora final.\nSepare cada uno de estos por comas con su respectivo espacio:\nSi desea salir ingrese la palabra Salir.");
		                	String hor = scanHor.nextLine();
		                	String[] horario = hor.split(", ");
		                	if (hor.equals("Salir")) {
		                		salida=true;
		                		break;
		                	}
		                	else {
		                		boolean correcto = false;
		                		for(String hora:horario) {
		                			correcto = Interfaz.formatoHorario(hora);
		                			if(!correcto) {
		                				System.out.println("El horario ingresado no esta en el formato correcto.");
		                				break;
		                			}
		                		}
		                		if (correcto) {
		                			horarioSel = new ArrayList<String>(Arrays.asList(horario));
		                			break;
		                		}
		                	}
		                }
		                //scanHor.close();
		                if(salida) {break;}
			            System.out.println("Ingrese la cantidad de cupos con la que contara el grupo:");
			            int cuposSel = scanner.nextInt();
                        scanner.nextLine();
			            Salon salonSel = null;
			            while(true) {
			            	System.out.println("Ingrese el salon donde se daran las sesiones de clase del grupo.\nSi desea salir ingrese la palabra Salir:");
			            	String nomSalon = scanner.nextLine();
			            	if (nomSalon.equals("Salir")) {
			            		salida = true;
			            		break;
			            	}
			            	for (Salon salon:Salon.salones) {
			            		if(nomSalon.equals(salon.getLugar())) {
			            			salonSel = salon;
			            			break;
			            		}
			            	}
			            	if (salonSel==null) {
                                
			            		System.out.println("El salon ingresado no existe. Ingrese un salon valido.");
			            	}
                            else{
                                break;
                            }
			            }
			            if(salida) {break;}
			            int numSel = materiaSel.getGrupos().size();
			            materiaSel.agregarGrupo(numSel+1, profesorSel, horarioSel, cuposSel, salonSel);
			            if (materiaSel.getGrupos().size()==numSel+1) {
			            	System.out.println("El grupo "+(numSel+1)+" de la materia "+materiaSel.getNombre()+" ha sido asignado correctamente");
			            }
			            else {
			            	System.out.println("El grupo no ha sido agregado. El salon y/o el profesor no contaba/n con disponibilidad en el horario asignado.");
			            }
			            break;
                    }
                }
                else if(opcion_3 == 4){
                    System.out.println("Has seleccionado la opcion 4 (Eliminar grupo.)");
                    boolean salida = false;
                    while(!salida) {
                    	System.out.println("ingrese la materia a la cual le desea eliminar un grupo.\nSi desea salir escriba la palabra Salir:");
                    	String materiaNom = scanner.nextLine();
                    	Materia materiaSel = null;
                    	if(materiaNom.equals("Salir")) {
                    		break;
                    	}
                    	for (Materia materia:Materia.getMateriasTotales()) {
                    		if (materiaNom.equals(materia.getNombre())) {
                    			materiaSel = materia;
                    			break;
                    		}
                    	}
                    	if(materiaSel==null) {
                    		System.out.println("La materia ingresada no existe. Ingrese una materia valida.");
                    		continue;
                    	}
                    	while(true) {
                    		System.out.println("Ingrese el numero del grupo que desea eliminar\nSi desea salir escriba el numero 0");
                    		int numSel = scanner.nextInt();
                            scanner.nextLine();
                    		if (numSel<0||numSel>materiaSel.getGrupos().size()) {
                    			System.out.println("El numero de grupo ingresado no existe. Ingrese el numero de un grupo valido.");
                    		}
                    		else if(numSel==0) {
                    			salida = true;
                    			break;
                    		}
                    		else {
                    			materiaSel.eliminarGrupo(numSel-1);
                    			System.out.println("El grupo "+numSel+" de la materia "+materiaSel.getNombre()+" ha sido eliminado con exito");
                    			break;
                    		}
                    		break;
                    	}
                    }
                }
                else if(0 > opcion_3 || opcion_3 > 4){
                    System.out.println("Opcion invalida.");
                    continue;
                }
                break;
            case 4:
                System.out.println("Has seleccionado la opcion 4 (Desmatricular Alumno).");
                Estudiante estudiante = null;
                Scanner scanner2 = new Scanner(System.in);
                while (true){
                    System.out.println("Elija como quiere seleccionar el alumno: \n1.Ver la lista de estudiantes. \n2.Buscar estudiante por ID y nombre. \n3.Salir");
                    int eleccion = scanner.nextInt();
                    scanner.nextLine();
                    if (eleccion == 1){
                        System.out.println("Elija el numero del estudiante");
                        System.out.println(Estudiante.mostrarEstudiantes());
                        int numeroEstudiante = scanner2.nextInt();
                        scanner2.nextLine();
                        estudiante = Estudiante.getEstudiantes().get(numeroEstudiante-1);
                        break;
                    }
                    else if(eleccion == 2){
                        System.out.print("Ingrese el nombre del estudiante: ");
                        String nombre = scanner2.nextLine();
                        System.out.print("Ingrese el id del estudiante: ");
                        long id = scanner2.nextLong();
                        scanner2.nextLine();
                        int numeroEstudiante = Estudiante.buscarEstudiante(nombre, id);
                        if (numeroEstudiante != -1){
                            System.out.println("El estudiante ha sido encontrado\n");
                            estudiante = Estudiante.getEstudiantes().get(numeroEstudiante);
                            break;
                        }
                        else{
                            System.out.println("El estudiante no ha sido encontrado, busque nuevamente\n");
                        }
                    }
                    else if(eleccion == 3){
                        break;
                    }
                    else{
                        System.out.println("Ingresa una opcion valida\n");
                    }
                    
                }

                while(true && estudiante != null){
                    while(true){
                        System.out.println("Seleccione de que quiere desmatricular al estudiante:");
                        System.out.println("1. Desmatricular de una materia \n2. Desmatricular del sistema \n3. Retroceder");
                        int opcion_1 = scanner2.nextInt();
                        scanner2.nextLine();
                        if (opcion_1 == 1){
                            Scanner scanner3 = new Scanner(System.in);
                            if (estudiante.getMaterias().size() == 0){
                                System.out.println("El estudiante no tiene ninguna materia matriculada. Intente otra opcion o retroceda para seleccionar otro estudiante\n");
                            }
                            else{
                            while (true){
                                boolean terminado = false;
                                System.out.println("Elija como quiere seleccionar la materia y el grupo");
                                System.out.println("1. Ver lista de materias y grupos \n2. Buscar materia y grupo");
                                int opcion_2 = scanner3.nextInt();
                                scanner3.nextLine();
                                switch(opcion_2){
                                    case 1:
                                    System.out.println(estudiante.mostrarMaterias());
                                    System.out.print("Ingrese el numero de la materia: ");
                                    int numeroMateria = scanner3.nextInt();
                                    scanner3.nextLine();
                                    System.out.print("Ingrese el numero del grupo: ");
                                    int numeroGrupo = scanner3.nextInt();
                                    scanner3.nextLine();
                                    Grupo grupo = estudiante.getMaterias().get(numeroMateria-1).getGrupos().get(numeroGrupo-1);
                                    if (grupo.existenciaEstudiante(estudiante)){
                                        grupo.eliminarEstudiante(estudiante);
                                        estudiante.getHorario().liberarHorario(grupo.getHorario());
                                        System.out.println("El estudiante ha sido desmatriculado de la materia y el grupo");
                                        terminado = true;
                                        break;
                                    }
                                    else{
                                        System.out.println("El estudiante no esta matriculado en el grupo");
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
                                        terminado = true;
                                        break;
                                    }
                                    else{
                                        System.out.println("El estudiante no tiene matriculada esta materia");
                                    }                                   
                                }
                                if (terminado){
                                    break;
                                }
                            }
                        }
                        }
                        else if(opcion_1 == 2){
                            if (usuario.comprobacionFacultad(estudiante)){
                                estudiante.getHorario().vaciarHorario(estudiante.getGrupos());
                                estudiante.desmatricularMaterias();
                                usuario.desmatricularDelSistema(estudiante);
                                System.out.println("El estudiante ha sido desmatriculado del sistema\n");
                                break;

                            }
                            else{
                                System.out.println("El estudiante es de una facultad diferente a la suya");
                                System.out.println("Puede volver a intentar con otro estudiante o salir\n");
                            }
                        }
                        else if(opcion_1 == 3){
                            break;
                        }
                        else{
                            System.out.println("Ingresa una opcion valida\n");
                        }
                    }
                    // scanner2.close();
                    break;
                }

                break;
            case 5:
            Coordinador e = (Coordinador) usuario;
            ArrayList<Estudiante> estudiantesBeneficiados = new ArrayList<Estudiante>();
                System.out.println("Has seleccionado la opcion 5 (Busqueda y Postulacion Becas).");
                boolean end = false;
                while(!end){
                    Scanner scanner_5 = new Scanner(System.in); 
                    System.out.println("Ingrese el numero que corresponde a la opcion que mejor se adapta a su busqueda:");
                    System.out.println("1.Ver listado de becas existentes actualmente.       2.Aplicar beca a estudiante.\n3.Crear nueva beca.                                  4.Eliminar beca.");
                    int opcion_5 = scanner_5.nextInt();
                    scanner_5.nextLine();
                    if (opcion_5 == 1){
                        System.out.println("Has seleccionado la opcion 1 (Ver listado de becas existentes actualmente.)");
                        System.out.println("A continuacion podra ver la lista de becas existentes en el momento:");
                        Interfaz.mostrarBecas();
                        continue;
                    }
                    else if(opcion_5 == 2){
                        Scanner scanner5_2 = new Scanner(System.in);
                        System.out.println("Has seleccionado la opcion 2 (Aplicar beca a estudiante.)");
                        System.out.println("Ingrese el nombre del estudiante");
                        String estNombre = scanner5_2.nextLine();
                        System.out.println("Ingrese el numero que corresponde a la beca que quiere aplicar el estudiante.");
                        Interfaz.mostrarBecas();
                        int nBeca = scanner5_2.nextInt();
                        scanner5_2.nextLine();
                        Beca tipoBeca = (Beca.getBecas()).get(nBeca-1);

                        ArrayList<String> nomEst = new ArrayList<String>();
                        for(Estudiante estu : Estudiante.getEstudiantes()){
                            String nom = estu.getNombre();
                            nomEst.add(nom);
                        }

                        if(nomEst.contains(estNombre) == false){
                            System.out.println("El nombre ingresado no fue encontrado entre los estudiantes actuales, intentelo otra vez (Recuerde que este debe ir con mayuscula inicial en cada palabra y sin tildes).");
                            continue;
                        }

                        for(Estudiante becado : estudiantesBeneficiados){
                            if(becado.getNombre().equals(estNombre) == true){
                                System.out.println("El estudiante ya ha aplicado exitosamente a una beca, no puede aplicar a otra durante el semestre academico actual.");
                                break;
                            }
                        }
                        
                        for(Estudiante est : Estudiante.getEstudiantes()){
                            if(est.getNombre().equals(estNombre) == true){
                                if(tipoBeca.getCupos() == 0){
                                    System.out.println("La beca "+tipoBeca.getConvenio()+" no cuenta con vacantes disponibles en el momento.");
                                    break;
                                }
                                else if (e.candidatoABeca(est,tipoBeca)){
                                    estudiantesBeneficiados.add(est);
                                    tipoBeca.setCupos(tipoBeca.getCupos()-1);
                                    System.out.println("El estudiante "+ est.getNombre() +" cumple con los requisitos para aplicar a la beca " +tipoBeca.getConvenio()+".");
                                    estudiantesBeneficiados.add(est);
                                    est.setSueldo(tipoBeca.getAyudaEconomica());
                                    System.out.println("La ayuda economica ha sido cargada al sueldo del estudiante "+est.getNombre()+".");

                                    if (est.pagarMatricula()){
                                        System.out.println("La matricula ha sido pagada.");
                                    }
                                    else if (est.pagarMatricula() == false){
                                        System.out.println("La matricula aun no ha sido pagada en su totalidad.");
                                    }
                                    break;

                                }
                                else if (e.candidatoABeca(est,tipoBeca) == false){
                                    System.out.println("El estudiante no cumple con los requisitos para aplicar a la beca " +tipoBeca.getConvenio()+".");
                                }                                
                            }
                        }
                    }else if(opcion_5 == 3){
                        System.out.println("Has seleccionado la opcion 3 (Crear nueva beca.)");
                        Scanner scanner5_3 = new Scanner(System.in);
                        System.out.println("Ingrese el numero de cupos totales que tendra la nueva beca:");
                        int cuposBeca =  scanner5_3.nextInt();
                        scanner5_3.nextLine();
                        System.out.println("Ingrese el nombre de la beca:");
                        String nombreBeca =  scanner5_3.nextLine();
                        // scanner5_3.nextLine();
                        System.out.println("Ingrese el promedio requerido que debe tener el estudiante para poder aplicar a la beca:");
                        double promedioBeca =  scanner5_3.nextDouble();
                        scanner5_3.nextLine();
                        System.out.println("Ingrese el numero que representa el porcentaje de avance con el que debe contar el estudiante para poder aplicar a la beca:");
                        double avanceBeca =  scanner5_3.nextDouble();
                        scanner5_3.nextLine();
                        System.out.println("Ingrese el estrato maximo que puede tener el estudiante para poder aplicar a la beca:");
                        int estratoBeca =  scanner5_3.nextInt();
                        scanner5_3.nextLine();
                        System.out.println("Ingrese el numero de creditos inscritos en el semestre que debe tener el estudiante para aplicar beca:");
                        int creditosBeca =  scanner5_3.nextInt();
                        scanner5_3.nextLine();
                        System.out.println("Ingrese la ayuda economica a la que puede acceder el estudiante una vez tenga la beca (Sin puntos ni comas):");
                        int ayudaBeca =  scanner5_3.nextInt();
                        scanner5_3.nextLine();
                        System.out.println("¿La beca necesita de recomendacion por parte de un profesor?");
                        System.out.println("1.Si.          2.No.");
                        int booleano =  scanner5_3.nextInt();
                        scanner5_3.nextLine();
                        boolean recomendacionBeca;
                        while(true){
                            if(booleano == 1){
                            recomendacionBeca = true;
                            break;
                        }                        
                        else if(booleano == 2){
                            recomendacionBeca = false;
                            break;
                        }
                        else if(booleano != 1 || booleano != 2){
                            System.out.println("Valor invalido, por favor intente nuevamente.");
                            continue;
                        }
                        }
                        
                        Beca nBeca = new Beca(cuposBeca, nombreBeca, promedioBeca, avanceBeca, estratoBeca, creditosBeca, ayudaBeca, recomendacionBeca);
                        System.out.println("La beca "+ nombreBeca +" ha sido creada con exito.");
                        break;
                    }
                    else if(opcion_5 == 4){
                        System.out.println("Has seleccionado la opcion 4 (Eliminar beca.)");
                        Scanner scanner5_4 = new Scanner(System.in);
                        System.out.println("Ingrese el numero que corresponde a la beca que quiere eliminar:");
                        Interfaz.mostrarBecas();
                        int becaSel = scanner5_4.nextInt();
                        scanner5_4.nextLine();
                        Beca delBeca = (Beca.getBecas()).get(becaSel-1);
                        Beca.eliminarBeca(delBeca);
                        System.out.println("La beca "+ delBeca.getConvenio() +" ha sido eliminada con exito.");
                        break;                     
                    }
                    else if(0 > opcion_5 || opcion_5 > 4){
                        System.out.println("Opcion invalida.");
                        continue;
                    }
                    break;
                    
                }
                break;

            case 6:
                Serializador.serializarListas();
                System.out.println("Has salido del programa");
                continuar = false;
                break;

            default:
                System.out.println("Opcion invalida");
                System.out.println("Desea continuar?");
                System.out.println("Opcion 1- SI");
                System.out.println("Opcion 2- NO");
                System.out.println("Por favor ingrese la opcion deseada");
                int continuarint=scanner.nextInt();
                scanner.nextLine();
                if (continuarint==1){
                    continue;
                } else{
                continuar=false;
                }
            }
        }

        // scanner.close();
    }

}

