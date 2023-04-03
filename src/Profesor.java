import java.util.ArrayList;

public class Profesor {
    private String nombre;
    private ArrayList<Materia> materiasDadas = new ArrayList<Materia>(10);
    private ArrayList<Grupo> grupos = new ArrayList<Grupo>();
    private String facultad;
    
    public Profesor(String nombre, String facultad){
        this.nombre = nombre;
        this.facultad = facultad;
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
    
    //FALTA: ORGANIZAR LAS FUNCIONALIDADES QUE NOS UNIERON Y HACER EL CONSTRUCTOR CORRESPONDIENTE

    public void desvincularGrupo(Grupo g){
        if (grupos.contains(g)){
            int indice = grupos.indexOf(g);
            grupos.remove(indice);

        }
    }


}
