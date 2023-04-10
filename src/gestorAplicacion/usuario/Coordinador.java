package gestorAplicacion.usuario;

import java.util.ArrayList;

import gestorAplicacion.administracion.*;
import java.io.Serializable;

public class Coordinador extends Usuario implements Serializable{
    private String facultad;
    private final static int limitesCreditos=20;
    // private static ArrayList<Materia> materiasTotales;
    private static final long serialVersionUID = 1L;

    public Coordinador(String facultad,long id, String nombre, String pw) {
        super(id, nombre,pw);
        this.facultad = facultad;
    }


    //Metodos

    public String toString(){
        return "Nombre: "+ getNombre()+ "\nDocumento: "+ getId();
    }

    public void crearMateria(String nombre, int codigo, int creditos){
        // Generarlo aqui o en el main?
        Materia materia = new Materia(nombre,codigo, "Sin descripcion", creditos, "Sin facultad", 0);
        // materiasTotales.add(materia);
    }

    public String desmatricular(Estudiante estudiante, Grupo grupo){
        // Desmatricular no seria simplemente llamar un metodo de estudiante?
        // Tambien seria que dentro de materias de estudiante no este esta materia

        boolean estaMatriculado = grupo.existenciaEstudiante(estudiante);

        if (estaMatriculado){
            grupo.eliminarEstudiante(estudiante);
            return "El estudiante ha sido desmatriculado de la materia y su respectivo grupo";
        }
        else{
            return "El estudiante no estaba matriculado";
        }
    }

    public void contratarProfesor(String nombre, String facultad){
        Profesor profesor = new Profesor(nombre,facultad);
    }


    // FUSIONE resturarEstudiantesInscritosEnMateria Y resturarProfesoresInvolucradosEnMateria EN resturarMateria.
    public void resturarMateria(Materia materia){
        for (int i=0;i<materia.getGrupos().size();i++){
            Grupo puntero_Grupo = materia.getGrupos().get(i);
            puntero_Grupo.getProfesor().desvincularGrupo(puntero_Grupo);

            for (int j=0;j<puntero_Grupo.getEstudiantes().size();j++){
                Estudiante puntero_Estudiante = puntero_Grupo.getEstudiantes().get(j);
                puntero_Estudiante.desmatricularMateria(materia);
            }   
        }
    }


    // ligadura dinamica?
    public Object[] crearHorarioAleatorio(ArrayList<Materia> materias){
        /**
         * Toma una lista de materias que se desean ver.
         * 
         * Crear un horario aleatorio en base de los grupos disponibles.
         * 
         * Retorna una lista estatica de dos elementos: Un booleano que nos dira si fue posible o no
         *  crear el horaio y el horario generado.
         */

        Object[] resultado = new Object[3];
                
        Horario horario =  new Horario();
        boolean ok = true;
        Materia materiaObstaculo = null;


        int[] gPosible = new int[materias.size()];        
        int i =0; // indice de materias
        
        while (true){
            ArrayList<String> pClases = materias.get(i).getGrupos().get(gPosible[i]).getHorario();
            if (!horario.comprobarDisponibilidad(pClases)){
                if(gPosible[i]==materias.get(i).getGrupos().size()-1){
                    ok = false;
                    horario = null;
                    materiaObstaculo = materias.get(i);
                    break;
                }
                else{
                    gPosible[i]++;
                }
            }
            
            else if(i==materias.size()-1){
                for (int k=0;k<materias.size();k++){
                    Grupo grupo = materias.get(k).getGrupos().get(gPosible[k]);
                    horario.ocuparHorario(grupo);
                }
                break;
            }
            
            else{
                i++;
            };
            // }
        }

        resultado[0] = ok;
        resultado[1] = horario;
        resultado[2] = materiaObstaculo;

        return resultado;

    }

    /*Metodo eliminarMateria: Rectificará que la materia que se quiere eliminar de la base de datos
    sí se encuentre en esta, y además eliminarla correctamente de las materias de los estudiantes 
    que la tienen inscrita y de los profesores relacionados a esta*/

    public void eliminarMateria(Materia materia){
        if(materiasTotales.contains(materia)){
            materiasTotales.remove(materia);
            resturarMateria(materia);
        }
        
    }

    /*Método agregarMateria: 
     * 
     * 
     * 
     */
                                                                                                                     
    // Getters

    public String getFacultad() {
        return this.facultad;
    }
        
    public static int getLimitesCreditos() {
        return limitesCreditos;
    }



    // Setters

    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }
}