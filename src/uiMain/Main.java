package uiMain;

import java.util.Scanner;
import gestorAplicacion.administracion.*;
import gestorAplicacion.usuario.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args){

        //solo lo puse para hacer una prueba
        Estudiante estudiante=new Estudiante(0, null, null, null, 0, null, 0);
        //lo de arriba se puede borrar


        Scanner scanner=new Scanner(System.in);
        Boolean continuar=true;
        System.out.println("Bienvenido a ....");
        while(continuar){
            //Aun no esta contruido la interfaz (mensajes bonitos en la terminal)
            System.out.println("Ingrese la opcion deseada: ");
            int opcion = scanner.nextInt();
            switch(opcion) {
            case 1:
                //La funcionalidad estrella (MATRICULAR MATERIA)
                //Con esta sacamos cinco
                System.out.println("Has seleccionado la opción 1 (Matricular materia)");
                matricularMateria(estudiante);
                //Le estoy pasando un estudiante como parametro porque no sabia como lo ibamos a hacer
                //el parametro sirve para decirle a la funcionalidad cual estudiante va a proceder con la matriculación de una materia
                break;
            case 2:
                System.out.println("Has seleccionado la opción 2");
                break;
            case 3:
                System.out.println("Has seleccionado la opción 3");
                break;
            case 4:
                System.out.println("Has seleccionado la opción 3");
                break;
            default:
                System.out.println("Opción inválida");
                continuar=false;
                break;
            }
        }

        scanner.close();
    }

    public static void matricularMateria(Estudiante estudiante){
    	Scanner scanner = new Scanner(System.in); 
    	ArrayList<Materia> materiasDisponibles=new ArrayList<Materia>();
        ArrayList<Materia> materiasTotales=Materia.getMateriasTotales();
        ArrayList<Materia> materiasInscritas=estudiante.getMaterias();

        /*
         * PRIMERO: 
         * Quitamos las materias que el estudiante no puede ver por los prerrequisitos
         * 
         */
        for (int i=0; i<materiasTotales.size();i++){
            Materia materia=materiasTotales.get(i);
            boolean anadir=true;
            for (int j=0; j<materia.getPrerrequisitos().size();j++){
                Materia prerrequisito=materia.getPrerrequisitos().get(j);
                for (int t=0;t < materiasInscritas.size();t++){
                    if (prerrequisito==materiasInscritas.get(t)){
                        anadir=false;
                        break;
                    }
                }
            }
            if (anadir){
                materiasDisponibles.add(materia);
            }
        }

        /*
         * SEGUNDO:
         * Revisamos cuales materias al ser matriculadas al estudiante le hacen sobrepasar el limite de creditos
         * Y tambien revisamos la disponibilidad en los cupos de la materia
         * 
         */
        for (int l=0;l<materiasDisponibles.size();l++){
            Materia materia=materiasDisponibles.get(l);
            int limitesCreditos=Coordinador.getLimitesCreditos();
            if (materia.getCupos()<=0){
                materiasDisponibles.remove(l);
            }
            if (estudiante.getCreditos()+materia.getCreditos()>limitesCreditos){
                materiasDisponibles.remove(l);
            }
        }

        /*
         * TERCERO:
         * En esta parte le mostramos una lista de posibles opciones a matricular
         * Dependiendo de la respuesta del usuario el ciclo se romperá o continuará hasta que el usuario quiera
         */
        while(true){
            ArrayList<Grupo> materiasMostradas=new ArrayList<Grupo>();
            int numero=1;
            for (int m=0;m<materiasDisponibles.size();m++){
                Materia materia=materiasDisponibles.get(m);
                String imprimir="";
                imprimir=" "+materia.getNombre()+" Grupo ";
                for (int n=0; n<materia.getGrupos().size(); n++){
                    int grupo=materia.getGrupos().get(n).getNumero();
                    int cantidad=materia.getGrupos().get(n).getCupos();
                    if (cantidad==0){
                        continue;
                    } else{
                        System.out.println(numero+imprimir+grupo+"("+cantidad+ " cupos)");
                        materiasMostradas.add(materia.getGrupos().get(n));
                        numero++;
                    }
                }
            }
            System.out.println("Por favor ingrese el numero correspondiente a la materia que desea matricular");
            int eleccion=scanner.nextInt();
            if (0<eleccion && eleccion<=numero){
                /*
                 * CUARTO:
                 * Si el estudiante selecciono alguna de la lista, entonces procedemos con la matriculación
                 * 
                 */
                Grupo grupoSeleccionado=materiasMostradas.get(eleccion-1);
                materiasInscritas.add(grupoSeleccionado.getMateria());
                grupoSeleccionado.agregarEstudiante(estudiante);
                grupoSeleccionado.getMateria().setCupos(grupoSeleccionado.getMateria().getCupos()-1);
                grupoSeleccionado.setCupos(grupoSeleccionado.getCupos()-1);
                estudiante.setCreditos(estudiante.getCreditos()+grupoSeleccionado.getMateria().getCreditos());
                estudiante.setMaterias(materiasInscritas);
                scanner.close();
                String imprimir="Materia "+grupoSeleccionado.getMateria().getNombre()+", grupo "+grupoSeleccionado.getNumero();
                System.out.println(imprimir+ ". Ha sido matriculado al estudiante: "+estudiante.getNombre());
                break;
            } else{
                System.out.println("Opción invalida");
                System.out.println("Desea continuar?");
                System.out.println("Opción 1- SI");
                System.out.println("Opción 2- NO");
                System.out.println("Por favor ingrese la opción deseada");
                int continuar=scanner.nextInt();
                if (continuar==1){
                    continue;
                }else{
                    break;
                }
            }
        }
    }

}
