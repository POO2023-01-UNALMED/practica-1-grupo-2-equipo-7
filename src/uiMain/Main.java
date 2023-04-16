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
import java.util.ArrayList;
import baseDatos.Deserializador;

public class Main {
    public static void main(String[] args){

        //solo lo puse para hacer una prueba
        Estudiante estudiante=new Estudiante(0, null, null, null, 0, null, 0);
        //lo de arriba se puede borrar


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
                //La funcionalidad estrella (MATRICULAR MATERIA)
                //Con esta sacamos cinco
                System.out.println("Has seleccionado la opción 1 (Matricular materia)");
                matricularMateria(estudiante);
                //Le estoy pasando un estudiante como parametro porque no sabia como lo ibamos a hacer
                //el parametro sirve para decirle a la funcionalidad cual estudiante va a proceder con la matriculación de una materia
                break;
            case 2:
                System.out.println("Has seleccionado la opción 2 (Generar Horario).");
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
                    //Funcionalidad agregar grupo//
                }
                else if(opcion_3 == 4){
                    System.out.println("Has seleccionado la opción 4 (Eliminar grupo.)");
                    //Funcionalidad eliminar grupo//
                }
                else if(opcion_3 > 4){
                    System.out.println("Opción inválida.");
                    continue;
                }
                break;
            case 4:
                System.out.println("Has seleccionado la opción 4 (Desmatricular Alumno).");
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
