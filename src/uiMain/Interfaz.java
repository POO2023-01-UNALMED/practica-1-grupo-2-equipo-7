package uiMain;

import java.util.ArrayList;
import gestorAplicacion.administracion.*;
import java.util.Scanner;
import gestorAplicacion.usuario.*;;

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

}
