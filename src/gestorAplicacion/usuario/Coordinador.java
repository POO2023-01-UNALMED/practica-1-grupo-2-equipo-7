package gestorAplicacion.usuario;

import java.util.ArrayList;

import gestorAplicacion.administracion.*;

public class Coordinador extends Usuario {
    private String facultad;
    private int limitesCreditos;
    // private static ArrayList<Materia> materiasTotales;

    public Coordinador(String facultad,int limitesCreditos,long id, String nombre, String pw) {
        super(id, nombre,pw);
        this.facultad = facultad;
        this.limitesCreditos = limitesCreditos;
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

        Horario horario;

        Object[] resultado = new Object[2];

        ArrayList<String> totalPosibles;

        boolean ok;

        for (int i=0;i<=materias.size();i++){
            Materia pMateria = materias.get(i);
            String posible;

            ArrayList<Grupo> grupos = pMateria.getGrupos();
            for (int e=0;e<=grupos.size();e++){
                Grupo pGrupo = grupos.get(e);
                
                //trabajo en progreso
            }

        }

        resultado[0] = ok;
        resultado[1] = horario;

        return resultado;

    }

    // Getters

    public String getFacultad() {
        return this.facultad;
    }
        
    public int getLimitesCreditos() {
        return this.limitesCreditos;
    }



    // Setters

    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }

    public void setLimitesCreditos(int limitesCreditos) {
        this.limitesCreditos = limitesCreditos;
    }

}