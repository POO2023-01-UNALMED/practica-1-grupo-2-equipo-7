package gestorAplicacion.usuario;

import java.util.ArrayList;
import gestorAplicacion.administracion.*;
import java.io.Serializable;

public class Estudiante extends Usuario implements Serializable{
    private static final long serialVersionUID = 1L;
    private String programa;
    private int semestre;
    private String facultad;
    private int creditos;
    private ArrayList<Materia> materias; 
    private ArrayList<Grupo> grupos;
    private Horario horario;
    private static ArrayList<Estudiante> estudiantes;

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos) {
        super(id,nombre,pw);
        this.programa = programa;
        this.semestre = semestre;
        this.facultad = facultad;
        this.creditos = creditos;
        this.materias = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
        
    }

    public String toString(){
        return "Nombre: "+ getNombre()+ "\nDocumento: "+ getId();
    }

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos, ArrayList<Materia> materias) {
        this(id,nombre,pw,programa,semestre,facultad,creditos);
        this.materias = materias;
    }
    
    public String mostrarMaterias() {
    	String retorno = "";
    	for (Grupo grupo:grupos) {
    		retorno += "- "+grupo.getMateria().getNombre()+" | Grupo "+grupo.getNumero()+"\n";
    	}
    	return retorno;
    }

    public static long buscarEstudiante(String nombre, long id){
        /*
         * Si existe el estudiante retorna su indice en el Arraylist estudiante
         * Si no existe, retorna -1
         */
        for (int i = 0; i < estudiantes.size(); i++){
            if (estudiantes.get(i).getNombre().equals(nombre) && estudiantes.get(i).getId() == id){

                return i;
            }
        }
        return -1;
    }

    public String getPrograma() {
        return programa;
    }

    public void setPrograma(String programa) {
        this.programa = programa;
    }

    public int getSemestre() {
        return semestre;
    }

    public void setSemestre(int semestre) {
        this.semestre = semestre;
    }

    public String getFacultad() {
        return facultad;
    }

    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }

    public int getCreditos() {
        return creditos;
    }

    public void setCreditos(int creditos) {
        this.creditos = creditos;
    }

    public ArrayList<Materia> getMaterias() {
        return materias;
    }

    public void setMaterias(ArrayList<Materia> materias) {
        this.materias = materias;
    }

    public static ArrayList<Estudiante> getEstudiantes() {
        return Estudiante.estudiantes;
    }

    public static void setEstudiantes(ArrayList<Estudiante> estudiantes) {
        Estudiante.estudiantes = estudiantes;
    }

    public void eliminarMateria(Materia materia){
        this.materias.remove(materia);
    }

    public void eliminarGrupo(Grupo grupo){
        this.grupos.remove(grupo);
        this.eliminarMateria(grupo.getMateria());
        this.horario.liberarHorario(grupo.getHorario());
    }

}
