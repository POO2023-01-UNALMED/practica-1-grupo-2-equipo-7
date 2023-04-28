package uiMain;

import java.util.ArrayList;
import gestorAplicacion.administracion.*;
import java.util.Scanner;
import gestorAplicacion.usuario.*;
import java.util.Random;

public interface Interfaz {
    
    // METODOS USADOS EN GENERAR HORARIO: 
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
            scanner.nextLine();
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
  
    public static void asignacionDeHorarioGenerado(Horario horario){
        /*
         * Decide si conservar un horario o no, ademas de asignarlo a un estudiante si es posible 
         */
        Scanner scanner=new Scanner(System.in);

        System.out.println("Desea Conservar el horario?\n1. Si\n2. No");
        int opt2=scanner.nextInt();
        scanner.nextLine();
        if (opt2==1){
            System.out.println("Escoja un estudiante: ");
            System.out.println(Estudiante.mostrarEstudiantes());

            System.out.print("Eleccion: -> ");
            int opt3=scanner.nextInt();
            scanner.nextLine();

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

    public static void matricularMateriaParte4(Estudiante estudiante, Grupo grupo){
        /*
         * La parte 4 de matricular materia es para matricularle al estudiante un grupo en especifico 
         */
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

    //METODO USADO EN BECA
    public static void mostrarBecas(){
        int i = 1;
        for (Beca beca: Beca.getBecas()){
            String a = beca.getConvenio();
            System.out.println(i +". "+ a + ".");
            i += 1;
        }
    } 

    //METODOS USADOS EN MATRICULAR MATERIA
    public static void matricularMateria(){
        /*
         *La parte 1 de la funcionalidad matricular materia:
        * Es para seleccionar al estudiante que se le va a matricular una materia 
         */
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
                    if (seleccionado.isMatriculaPagada()==false){
                        System.out.println("La matricula del estudiante no esta pagada");
                        invalido=true;
                    } else if (seleccionado.getCreditos()>=Coordinador.getLimitesCreditos()){
                        System.out.println("El estudiante no puede matricular más materias");
                        invalido=true;
                    }else{
                        System.out.println("Estudiante seleccionado, nombre: "+seleccionado.getNombre()+" ID: "+seleccionado.getId());
                        matricularMateriaParte2(seleccionado);
                        salir=true;
                    }
                }

            }else{

                System.out.println("Opcion invalida");
                invalido=true;

            }
            if (invalido){

                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opcion deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion3=scanner.nextInt();
                scanner.nextLine();
                if (opcion3!=1){
                    salir=true;
                }

            }
        }
    }
    
    public static void matricularMateriaParte2(Estudiante estudiante){
        /*
         * La parte 2 de la funcionalidad matricular materia:
         * Es para seleccionar la materia que se desea matricular
         */
        Scanner scanner = new Scanner(System.in); 
        boolean salir=false;
        while(salir==false){

            Boolean invalido=false;
            System.out.println("Como desea buscar la materia?\n1- Mediante una lista de las materias disponibles\n2- Mediante una busqueda manual");
            int opcion=scanner.nextInt();
            scanner.nextLine();
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
                scanner.nextLine();

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

                    if (seleccionada.getCupos()==0){
                        System.out.println("Materia sin cupos disponibles");
                        invalido=true;
                    }else if(Materia.comprobarPrerrequisitos(estudiante, seleccionada)==false){
                        System.out.println("El estudiante no cumple con los prerrequisitos de la materia");
                        invalido=true;
                    }else if(estudiante.getCreditos()+seleccionada.getCreditos()>Coordinador.getLimitesCreditos()){
                        System.out.println("El estudiante tiene creditos insuficientes");
                        invalido=true;
                    }else{
                        System.out.println("Materia seleccionada "+seleccionada.getNombre());
                        matricularMateriaParte3(estudiante, seleccionada);
                        salir=true; 
                    }  
                }

            }else{

                System.out.println("Opcion invalida");
                invalido=true;
            }

            if (invalido){

                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opcion deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion2=scanner.nextInt();
                scanner.nextLine();
                if (opcion2!=1){
                    salir=true;
                }

            }
        }
    }
    
    public static void matricularMateriaParte3(Estudiante estudiante, Materia materia){
        /*
         * La parte 3 de la funcionalidad matricular materia:
         * Es para seleccionar el grupo de la materia seleccionada 
         * Y tambien para finalizar la funcionalidad
         */
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
            scanner.nextLine();
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
                scanner.nextLine();

                if (opcion2==1){
                    System.out.println(estudiante.getHorario().mostrarHorario());
                }

            }else{
                System.out.println("Opcion invalida");
                System.out.println("Desea intentarlo otra vez o desea salir?");
                System.out.println("Ingrese la opcion deseada: \n1- Intentarlo otra vez\n2- Salir");
                int opcion3=scanner.nextInt();
                scanner.nextLine();
                if (opcion3!=1){
                    salir=true;
                }
            }
        }
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
    
    //METODOS USADOS EN AGREGAR GRUPO
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

}
