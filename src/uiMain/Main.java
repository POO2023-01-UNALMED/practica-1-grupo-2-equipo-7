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
import java.util.Random;

import baseDatos.Serializador;
import baseDatos.Deserializador;

public class Main {
    public static void main(String[] args){
        Deserializador.deserializarListas();
        Scanner scanner=new Scanner(System.in);
        Boolean continuar=true;
        Boolean logueado = false;
        System.out.println("Bienvenido al Portal de Servicios Academicos S.M.M");
        
        // Zona de Pruebas -------------------------------------------------------------------

        // Estudiante.getEstudiantes().get(0).setSueldo(99999999);
        // Estudiante.getEstudiantes().get(0).pagarMatricula();
        // Materia.getMateriasTotales().get(0).setCupos(20);
        
        // System.out.println(Estudiante.getEstudiantes().get(0).getMaterias().get(0).getNombre());
        // System.out.println(Grupo.getGruposTotales().get(0).getEstudiantes().get(0).getNombre());
        
 
        // Zona de Pruebas -------------------------------------------------------------------

        Usuario usuario = null;
        while(!logueado) {
        	Scanner scanner2 = new Scanner(System.in);
        	System.out.println("Seleccione como desea ingresar a la plataforma:\n1. Crear nuevo usuario.\n2. Ingresar usuario existente.");
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
        			else if (existenciaUsuario(nomb)) {
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
        		long id = generarId();
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
        			else if (!existenciaId(id)){
        				System.out.println("El id ingresado no corresponde a ningun usuario registrado en el sistema.");
        			}
        			else if (encontrarUsuario(id).getTipo()=="Estudiante") {
        				System.out.println("Error. Solo pueden ingresar coordinadores en la plataforma.");
        			}
        			else {
        				Usuario usuarioE = (Coordinador)encontrarUsuario(id);
        				boolean pwCorect = false;
        				while(!pwCorect){
        					System.out.println("Ingrese la contrasena:");
        					String cont = scanner3.nextLine();
        					if(!verificarPw(usuarioE,cont)) {
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
        						usuario = (Coordinador)usuarioE;
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
            System.out.println("A continuacion encontrara los diferentes servicios ofrecidos por la plataforma.");
            System.out.println("Ingrese la opcion deseada: \n1. Matricular Materia.\n2. Generar Horario.\n3. Eliminar o agregar Materia / Grupo.\n4. Desmatricular Alumno. \n5. Busqueda y Postulacion de Becas. \n6. Salir y Guardar");
            int opcion = scanner.nextInt();
            switch(opcion) {
            case 1:
                System.out.println("Has seleccionado la opcion 1 (Matricular materia)");
                matricularMateria();
                break;
            case 2:
                System.out.println("Has seleccionado la opcion 2 (Generar Horario).");
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
            Coordinador m = (Coordinador) usuario;
                System.out.println("Has seleccionado la opcion 3 (Eliminar o agregar Materia / Grupo).");
                System.out.println("Ingrese la opcion que se ajuste a su busqueda:\n1.Agregar Materia.       2.Eliminar Materia.\n3.Agregar Grupo.         4.Eliminar Grupo.");
                int opcion_3 = scanner.nextInt();
                if(opcion_3 == 1){
                    System.out.println("Has seleccionado la opcion 1 (Agregar materia.)");
                    if(opcion_3 == 1){
                        System.out.println("Has seleccionado la opción 1 (Agregar materia.)");
                        boolean fin = false;
                        Materia materiaN = null;
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
                            System.out.println("Ingresa el código de la materia que desea agregar.");
                            int codigo = scanner3_1.nextInt();
                            for (Materia materia : Materia.getMateriasTotales()){
                                if (materia.getCodigo() == codigo){
                                    System.out.println("El código que intenta asignarle a la materia, ya le corresponde a una existente.");
                                    fin = true;
                                }
                            }
                            System.out.println("Ingrese una breve descripción de la materia.");
                            String descrip = scanner3_1.nextLine();
                            System.out.println("Ingresa los créditos que le asigna a la materia.");
                            int creditos = scanner3_1.nextInt();
                            System.out.println("Ingrese la facultad a la que pertenece la materia");
                            String facu = scanner3_1.nextLine();
                            
                            System.out.println("Ingrese los prerrequisitos que tiene la materia para poder ser inscritas por el estudiante (separadas por comas con su respectivo espacio)");
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
                            m.agregarMateria(nombre, codigo, descrip, creditos, facu, pRequisitos);
                            System.out.println("La materia "+ nombre + "ha sido creada con éxito.");
                            break;                                                                 
                        }
                        
                    }
                }
                else if(opcion_3 == 2){
                    System.out.println("Has seleccionado la opción 2 (Eliminar materia.)");
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
                                m.eliminarMateria(materia);
                                break;
                            }
                        }
                        System.out.println("La materia "+ nomMat + "ha sido eliminada con éxito.");
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
		                    
		                    if (opcion_profe==1) {
		                    	System.out.println("Seleccione uno de los siguientes profesores");
		                    	System.out.print(Profesor.mostrarProfesMateria(materiaSel));
		                    	int seleccionProfe = scanner4.nextInt();
		                    	ArrayList<Profesor> preProfes = Profesor.profesoresDeMateria(materiaSel);
		                    	profesorSel = preProfes.get(seleccionProfe-1);
		                    	break;
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
		                			correcto = formatoHorario(hora);
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
			            }
			            if(salida) {break;}
			            int numSel = materiaSel.getGrupos().size();
			            materiaSel.agregarGrupo(numSel+1, profesorSel, horarioSel, cuposSel, salonSel);
			            if (materiaSel.getGrupos().size()==numSel+1) {
			            	System.out.println("El grupo "+numSel+" de la materia "+materiaSel+" ha sido asignado correctamente");
			            }
			            else {
			            	System.out.println("El grupo no ha sido agregado. El salón y/o el profesor no contaba/n con disponibilidad en el horario asignado.");
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
                    	if(materiaNom.equals("Salida")) {
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
                    		if (numSel<0||numSel>materiaSel.getGrupos().size()) {
                    			System.out.println("El numero de grupo ingresado no existe. Ingrese el numero de un grupo valido.");
                    		}
                    		else if(numSel==0) {
                    			salida = true;
                    			break;
                    		}
                    		else {
                    			materiaSel.eliminarGrupo(numSel);
                    			System.out.println("El grupo "+numSel+" de la materia "+materiaSel+" ha sido eliminado con exito");
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
                                System.out.println("El estudiante no tiene ninguna materia matriculada. Intente otra opción o retroceda para seleccionar otro estudiante\n");
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
                System.out.println("Has seleccionado la opcion 5 (Busqueda y Postulacion Becas).");
                boolean end = false;
                while(!end){
                    Scanner scanner_5 = new Scanner(System.in); 
                    System.out.println("Ingrese el número que corresponde a la opción que mejor se adapta a su búsqueda:");
                    System.out.println("1.Ver listado de becas existentes actualmente.       2.Comprobar si un estudiante es candidato a beca.\n3.Crear nueva beca.                                  4. Eliminar beca.");
                    int opcion_5 = scanner_5.nextInt();
                    if (opcion_5 == 1){
                        System.out.println("Has seleccionado la opción 1 (Ver listado de becas existentes actualmente.)");
                        System.out.println("A continuación podrá ver la lista de becas existentes en el momento:");
                        mostrarBecas();
                    }
                    else if(opcion_5 == 2){
                        Scanner scanner5_2 = new Scanner(System.in);
                        System.out.println("Has seleccionado la opción 2 (Comprobar si un estudiante es candidato a beca.)");
                        System.out.println("Ingrese el nombre del estudiante");
                        String estNombre = scanner5_2.nextLine();
                        System.out.println("Ingrese el número que corresponde a la beca que quiere aplicar el estudiante.");
                        mostrarBecas();
                        int nBeca = scanner5_2.nextInt();
                        Beca tipoBeca = (Beca.getBecas()).get(nBeca-1);

                        for(Estudiante est : Estudiante.getEstudiantes()){
                            if(est.getNombre().equals(estNombre) == true){
                                if(tipoBeca.getCupos() == 0){
                                    System.out.println("La beca "+tipoBeca+" no cuenta con vacantes disponibles en el momento.");
                                }
                                else if (e.candidatoABeca(est,tipoBeca)){
                                    System.out.println("El estudiante cumple con los requisitos para aplicar a la beca " +tipoBeca+".");
                                }
                                else if (e.candidatoABeca(est,tipoBeca) == false){
                                    System.out.println("El estudiante no cumple con los requisitos para aplicar a la beca " +tipoBeca+".");
                                }                                
                            }
                        }
                    }else if(opcion_5 == 3){
                        System.out.println("Has seleccionado la opción 3 (Crear nueva beca.)");
                        Scanner scanner5_3 = new Scanner(System.in);
                        System.out.println("Ingrese el número de cupos totales que tendrá la nueva beca:");
                        int cuposBeca =  scanner5_3.nextInt();
                        System.out.println("Ingrese el nombre de la beca:");
                        String nombreBeca =  scanner5_3.nextLine();
                        System.out.println("Ingrese el promedio requerido que debe tener el estudiante para poder aplicar a la beca:");
                        double promedioBeca =  scanner5_3.nextDouble();
                        System.out.println("Ingrese el número que representa el porcentaje de avance con el que debe contar el estudiante para poder aplicar a la beca:");
                        double avanceBeca =  scanner5_3.nextDouble();
                        System.out.println("Ingrese el número de créditos inscritos en el semestre que debe tener el estudiante para aplicar beca:");
                        int creditosBeca =  scanner5_3.nextInt();
                        System.out.println("Ingrese la ayuda económica a la que puede acceder el estudiante una vez tenga la beca (Sin puntos ni comas):");
                        int ayudaBeca =  scanner5_3.nextInt();
                        System.out.println("¿La beca necesita de recomendación por parte de un profesor?");
                        System.out.println("1.Sí.          2.No.");
                        int booleano =  scanner5_3.nextInt();
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
                            System.out.println("Valor inválido, por favor intente nuevamente.");
                            continue;
                        }
                        }
                        
                        Beca nBeca = new Beca(cuposBeca, nombreBeca, promedioBeca, avanceBeca, creditosBeca, ayudaBeca, recomendacionBeca);
                    }
                    else if(opcion_5 == 4){
                        System.out.println("Has seleccionado la opción 4 (Eliminar beca.)");
                        Scanner scanner5_4 = new Scanner(System.in);
                        System.out.println("Ingrese el número que corresponde a la beca que quiere eliminar:");
                        mostrarBecas();
                        int becaSel = scanner5_4.nextInt();
                        Beca delBeca = (Beca.getBecas()).get(becaSel-1);
                        Beca.eliminarBeca(delBeca);                     
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
                if (continuarint==1){
                    continue;
                } else{
                continuar=false;
                }
            }
        }

        // scanner.close();
    }
    
    //METODO USADO EN AGREGAR GRUPO
    public static boolean formatoHorario(String horario) {
    	boolean formato = false;
    	if (horario.length()==7) {
    		String hi = horario.substring(2, 4);
    		String hf = horario.substring(5, 7);
    		String diaS = horario.substring(0,1);
    		
    		if(hi.matches("\\d+")&&hf.matches("\\d+")&&diaS.matches("\\d+")) {
    			int horI = Integer.parseInt(hi);
    			int horF = Integer.parseInt(hf);
    			int dia = Integer.parseInt(diaS);
    			
    			if(dia>=0&&dia<=7&&horario.substring(1,2).equals("-")&&hi.matches("\\d+")&&horI>=0&&horI<=23) {
    				if(horI>=0&&horI<=23&&horario.substring(4,5).equals("-")&&hi.matches("\\d+")&&horF>horI&&horF>0&&horF<=23) {
    					formato = true;
    				}
    			}
    		}
    	}
    	return formato;
    }

    //METODOS USADOS PARA EL LOG
    public static long generarId() {
    	int min = 10000;
    	int max = 99999;
    	int id;
    	boolean existe = false;
    	do {
    		id = new Random().nextInt(max-min)+min;
    		for (Usuario usuario:Usuario.getUsuariosTotales()) {
    			if (usuario.getId()==id) {
    				existe=true;
    				break;
    			}
    		}
    	}while(existe);
    	return id;
    }
    
    public static boolean existenciaUsuario(String nombre) {
    	boolean exist = false;
    	for (Usuario usuario:Usuario.getUsuariosTotales()) {
    		if (usuario.getNombre()==nombre) {
    			exist = true;
    			break;
    		}
    	}
    	return exist;
    }
    
    public static boolean existenciaId(long id) {
    	boolean exist = false;
    	for (Usuario usuario:Usuario.getUsuariosTotales()) {
    		if (usuario.getId()==id) {
    			exist = true;
    			break;
    		}
    	}
    	return exist;
    }
    
    public static Usuario encontrarUsuario(long id) {
    	Usuario encontrado = null;
    	for (Usuario usuario:Usuario.getUsuariosTotales()) {
    		if (usuario.getId()==id) {
    			encontrado = usuario;
    		}
    	}
    	return encontrado;
    }
    
    public static boolean verificarPw(Usuario usuario, String pw) {
    	if (usuario.getPw().equals(pw)) {
    		return true;
    	}
    	else {
    		return false;
    	}
    }
    
    //METODOS USADOS EN MATRICULAR MATERIA

    /*
     * La parte 1 de la funcionalidad matricular materia:
     * Es para seleccionar al estudiante que se le va a matricular una materia
     */
    public static void matricularMateria(){
        Scanner scanner = new Scanner(System.in);
        boolean salir=false;

    	while(salir==false){

            Boolean invalido=false;
            System.out.println("Desea buscar al estudiante mediante una lista o mediante su ID o su nombre?");
            System.out.println("Ingrese la opcion deseada: \n1- Lista de estudiantes disponibles\n2- Buscar al estudiante");
            int opcion=scanner.nextInt();
            scanner.nextLine();

            if (opcion==1){

                System.out.println("Lista de estudiantes disponibles para matricular: ");
                ArrayList<Estudiante> totalEstudiantes=new ArrayList<Estudiante>();
                for (Estudiante estudiante: Estudiante.getEstudiantes()){
                    if (estudiante.isMatriculaPagada()==false){
                        continue;
                    }
                    if (estudiante.getCreditos()==Coordinador.getLimitesCreditos()){
                        continue;
                    }
                    totalEstudiantes.add(estudiante);
                    System.out.println(totalEstudiantes.size()+" Nombre: "+estudiante.getNombre()+" ID: "+estudiante.getId());
                }

                System.out.println("Por favor ingrese el numero correpondiente al estudiante que desea seleccionar: ");
                int opcion2 = scanner.nextInt();
                scanner.nextLine();
                if (opcion2<=totalEstudiantes.size() && opcion2>=1){
                    Estudiante seleccionado=totalEstudiantes.get(opcion2-1);
                    System.out.println("Estudiante seleccionado, nombre: "+seleccionado.getNombre()+" ID: "+seleccionado.getId());
                    matricularMateriaParte2(seleccionado);
                    salir=true;

                }else{
                    System.out.println("Opcion invalida");
                    invalido=true;
                }

            }else if(opcion==2){

                System.out.println("Por favor ingrese el nombre del estudiante: ");
                String nombre=scanner.nextLine();
                System.out.println("Por favor ingrese el ID del estudiante: ");
                long id=scanner.nextLong();
                scanner.nextLine();
                int index=Estudiante.buscarEstudiante(nombre, id);

                if (index==-1){
                    System.out.println("Estudiante no encontrado");
                    invalido=true;

                }else{
                    Estudiante seleccionado=Estudiante.getEstudiantes().get(index);
                    System.out.println("Estudiante seleccionado, nombre: "+seleccionado.getNombre()+" ID: "+seleccionado.getId());
                    matricularMateriaParte2(seleccionado);
                    salir=true;
                }

            }else{

                System.out.println("Opcion invalida");
                invalido=true;

            }
            if (invalido){

                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opcion deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion3=scanner.nextInt();

                if (opcion3!=1){
                    salir=true;
                }

            }
        }
    }
    
    /*
     * La parte 2 de la funcionalidad matricular materia:
     * Es para seleccionar la materia que se desea matricular
     */
    public static void matricularMateriaParte2(Estudiante estudiante){
        Scanner scanner = new Scanner(System.in); 
        boolean salir=false;
        while(salir==false){

            Boolean invalido=false;
            System.out.println("Como desea buscar la materia?\n1- Mediante una lista de las materias disponibles\n2- Mediante una busqueda manual");
            int opcion=scanner.nextInt();
            ArrayList<Materia> materiasTotales=new ArrayList<Materia>(Materia.getMateriasTotales());
            if (opcion==1){

                ArrayList<Materia> materiasDisponibles=new ArrayList<Materia>();
                System.out.println("Lista de materias disponibles para matricular: ");
                int limitesCreditos=Coordinador.getLimitesCreditos();
                for (Materia materia: materiasTotales){
                    if (Materia.comprobarPrerrequisitos(estudiante, materia)==false){
                        continue;
                    }
                    if (materia.getCupos()<=0){
                        continue;
                    }else if (estudiante.getCreditos()+materia.getCreditos()>limitesCreditos){
                        continue;
                    }
                    materiasDisponibles.add(materia);
                    System.out.println(materiasDisponibles.size()+" Nombre: "+materia.getNombre()+" Cupos: "+materia.getCupos());
                }
                System.out.println("Por favor ingrese el numero correspondiente a la materia que desea matricular");
                int eleccion=scanner.nextInt();

                if (1<=eleccion && eleccion<=materiasDisponibles.size()){

                    Materia seleccionada = materiasDisponibles.get(eleccion-1);
                    System.out.println("Materia seleccionada "+seleccionada.getNombre());
                    matricularMateriaParte3(estudiante, seleccionada);
                    salir=true;

                } else{

                    System.out.println("Opcion invalida");
                    invalido=true;
                }

            }else if(opcion==2){

                System.out.println("Por favor ingrese el nombre de la materia deseada: ");
                String nombre=scanner.nextLine();
                System.out.println("Por favor ingrese el codigo de la materia deseada: ");
                int codigo=scanner.nextInt();
                scanner.nextLine();
                int index=Materia.buscarMateria(nombre, codigo);

                if (index==-1){

                    System.out.println("Materia no encontrada");
                    invalido=true;

                }else{

                    Materia seleccionada=materiasTotales.get(index);
                    System.out.println("Materia seleccionada "+seleccionada.getNombre());
                    matricularMateriaParte3(estudiante, seleccionada);
                    salir=true;
                }

            }else{

                System.out.println("Opcion invalida");
                invalido=true;
            }

            if (invalido){

                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opcion deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion2=scanner.nextInt();
                if (opcion2!=1){
                    salir=true;
                }

            }
        }
    }
    /*
     * La parte 3 de la funcionalidad matricular materia:
     * Es para seleccionar el grupo de la materia seleccionada 
     * Y tambien para finalizar la funcionalidad
     */
    public static void matricularMateriaParte3(Estudiante estudiante, Materia materia){
        Scanner scanner=new Scanner(System.in);
        Boolean salir=false;

        while (salir==false){

            System.out.println("Grupos disponibles para matricular: ");
            ArrayList<Grupo> gruposDisponibles=new ArrayList<Grupo>();

            for (Grupo grupo: materia.getGrupos()){
                if (!estudiante.getHorario().comprobarDisponibilidad(grupo.getHorario())){
                    continue;
                }
                if (grupo.getCupos()!=0){
                    gruposDisponibles.add(grupo);
                    System.out.println((gruposDisponibles.size())+" Grupo #"+grupo.getNumero()+ " cupos: "+grupo.getCupos()+" Profesor: "+grupo.getProfesor().getNombre());
                }
            }
            
            int opcion=scanner.nextInt();
            if (opcion>0 && opcion<=gruposDisponibles.size()){

                Grupo grupoSeleccionado=gruposDisponibles.get(opcion-1);
                ArrayList<Materia> materiasInscritas=new ArrayList<Materia>(estudiante.getMaterias());
                ArrayList<Grupo> gruposInscritos=new ArrayList<Grupo>(estudiante.getGrupos());
                gruposInscritos.add(grupoSeleccionado);
                materiasInscritas.add(materia);
                grupoSeleccionado.agregarEstudiante(estudiante);
                grupoSeleccionado.getMateria().setCupos(grupoSeleccionado.getMateria().getCupos()-1);
                grupoSeleccionado.setCupos(grupoSeleccionado.getCupos()-1);
                estudiante.setCreditos(estudiante.getCreditos()+materia.getCreditos());
                estudiante.setMaterias(materiasInscritas);
                estudiante.setGrupos(gruposInscritos);
                String imprimir="Materia "+materia.getNombre()+" - grupo #"+grupoSeleccionado.getNumero();
                System.out.println(imprimir+ ". Ha sido matriculado al estudiante: "+estudiante.getNombre());
                salir=true;

                System.out.println("Desea visualizar el horario del estudiante?: \n1- Si\n2- No");
                int opcion2=scanner.nextInt();

                if (opcion2==1){
                    System.out.println(estudiante.getHorario().mostrarHorario());
                }

            }else{
                System.out.println("Opcion invalida");
                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opcion deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion3=scanner.nextInt();
                if (opcion3!=1){
                    salir=true;
                }
            }
        }
    }
   //La parte 4 de matricular materia es para matricularle al estudiante un grupo en especifico
    public static void matricularMateriaParte4(Estudiante estudiante, Grupo grupo){
        ArrayList<Materia> materiasInscritas=new ArrayList<Materia>(estudiante.getMaterias());
        materiasInscritas.add(grupo.getMateria());
        grupo.agregarEstudiante(estudiante);
        grupo.getMateria().setCupos(grupo.getMateria().getCupos()-1);
        grupo.setCupos(grupo.getCupos()-1);
        ArrayList<Grupo> gruposInscritos=new ArrayList<Grupo>(estudiante.getGrupos());
        gruposInscritos.add(grupo);
        estudiante.setGrupos(gruposInscritos);
        estudiante.setCreditos(estudiante.getCreditos()+grupo.getMateria().getCreditos());
        estudiante.setMaterias(materiasInscritas);
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
        System.out.printf("%-3s %-60s %-20s %-10s%n", "Num", "Nombre", "Facultad","Codigo");
        
        for (Materia pMateria:ListaAMostrar){
            System.out.printf("%-3d %-60s %-20s %-10d%n",con,pMateria.getNombre(),pMateria.getFacultad(),pMateria.getCodigo());
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
            System.out.println(pHorario.mostrarHorario());
            asignacionDeHorarioGenerado(pHorario);
        }
        else{
            System.out.println("No fue posible generar el horario, ya que "+((Materia)informacion[2]).getNombre()+" es un obstaculo");
        }

        
            
        }
    
    // - Conexion de dos metodos
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

    // - Asignar horario
    public static void asignacionDeHorarioGenerado(Horario horario){
        /*
         * Decide si conservar un horario o no, ademas de asignarlo a un estudiante si es posible 
         */
        Scanner scanner=new Scanner(System.in);

        System.out.println("Desea Conservar el horario?\n1. Si\n2. No");
        int opt2=scanner.nextInt();
        if (opt2==1){
            System.out.println("Escoja un estudiante: ");
            System.out.println(Estudiante.mostrarEstudiantes());

            System.out.print("Eleccion: -> ");
            int opt3=scanner.nextInt();

            Estudiante seleccionEstudiante = Estudiante.getEstudiantes().get(opt3-1);
            Horario tempHorario = seleccionEstudiante.getHorario();
            seleccionEstudiante.setHorario(new Horario());

            boolean flag = true;
            for (Grupo pGrupo:horario.getGrupoContenidos()){
                if (!Materia.puedeVerMateria(seleccionEstudiante, pGrupo)){
                    flag = false;
                    break;   
                } 
            }
                

            if (flag){
                seleccionEstudiante.setHorario(horario);
                seleccionEstudiante.desmatricularMaterias();
                for (Grupo pGrupo:horario.getGrupoContenidos()){
                    matricularMateriaParte4(seleccionEstudiante, pGrupo);
                }
                System.out.println("Horario asignado con exito al estudiante "+seleccionEstudiante.getNombre());
            }else{
                seleccionEstudiante.setHorario(tempHorario);
                System.out.println("No es posible asignar el horario, el estudiante "+seleccionEstudiante.getNombre()+" no cumple los Pre-requisitos");
            }


        }
        else{
            System.out.println("Horario descartado");
        }
    }
    
    public static void mostrarBecas(){
        for (Beca beca: Beca.getBecas()){
            int i = 1;
            String a = beca.getConvenio();
            System.out.println(i +". "+ a + ".");
            i += 1;
            }
    } 



}

