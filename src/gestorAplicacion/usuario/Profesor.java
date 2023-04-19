package gestorAplicacion.usuario;
import java.util.ArrayList;
import gestorAplicacion.administracion.*;
import java.io.Serializable;

public class Profesor implements Serializable{
    private String nombre;
    private String facultad;
    private Horario horario;
    private ArrayList<Materia> materiasDadas = new ArrayList<Materia>(10);
    private ArrayList<Grupo> grupos = new ArrayList<Grupo>();
    private static ArrayList<Profesor> profesores =new ArrayList<Profesor>();
    private static final long serialVersionUID = 1L;
    
    public Profesor(String nombre, String facultad, Horario horario, ArrayList<Materia> materiasDadas, ArrayList<Grupo> grupos){
        this.nombre = nombre;
        this.facultad = facultad;
        this.horario = horario;
        this.materiasDadas = materiasDadas;
        this.grupos = grupos;
        Profesor.profesores.add(this);
    }

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFacultad() {
        return facultad;
    }
    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }

    public ArrayList<Materia> getMateriasDadas() {
        return materiasDadas;
    }
    public void setMateriasDadas(ArrayList<Materia> materiasDadas) {
        this.materiasDadas = materiasDadas;
    }

    public ArrayList<Grupo> getGrupos() {
        return grupos;
    }
    public void setGrupos(ArrayList<Grupo> grupos) {
        this.grupos = grupos;
    }

    public static ArrayList<Profesor> getProfesores() {
        return profesores;
    }
    public static void setProfesores(ArrayList<Profesor> profesores) {
        Profesor.profesores = profesores;
    }
    
    //FALTA: ORGANIZAR LAS FUNCIONALIDADES QUE NOS UNIERON Y HACER EL CONSTRUCTOR CORRESPONDIENTE

    public void setHorario(Horario horario) {
    	this.horario = horario;
    }
    
    public Horario getHorario() {
    	return this.horario;
    }
    
    public void vincularGrupo(Grupo g) {
    	this.grupos.add(g);
    	this.horario.ocuparHorario(g.getHorario(), g);
    }
    
    public void desvincularGrupo(Grupo g){
        if (grupos.contains(g)){
            int indice = grupos.indexOf(g);
            ArrayList<String> horLibre = grupos.get(indice).getHorario();
            this.horario.liberarHorario(horLibre);
            grupos.remove(indice);
        }
    }

    public boolean daMateria(Materia materia) {
    	return this.materiasDadas.contains(materia);
    }

    public boolean recomendarEstudiante(Estudiante estudiante){
        for (Profesor profesor : Profesor.getProfesores()){
            int chance = 0;
            int suerte = (int)(Math. random()*10+1);
            for(Grupo grupo : Estudiante.getGruposVistos()){
                if (grupo.getProfesor().equals(profesor.getNombre()) == true){
                    chance += 5;
                }
                if (estudiante.getFacultad().equals(profesor.getFacultad()) == true){
                    chance += 3;
                }
                if (chance >= suerte){
                    return true;
                }else if (chance < suerte){
                    return false;
                }   
            }
        }
    }

}
