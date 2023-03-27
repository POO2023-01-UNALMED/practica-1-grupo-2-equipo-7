import java.util.ArrayList;

public class Estudiante extends Usuario {
    private String programa;
    private int semestre;
    private String facultad;
    private int creditos;
    private ArrayList<Materia> materias;

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos) {
        super(id,nombre,pw);
        this.programa = programa;
        this.semestre = semestre;
        this.facultad = facultad;
        this.creditos = creditos;
        this.materias = new ArrayList<materias>();
        //Si es necesario declarar un nuevo array al crear el objeto o no?
        
    }

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos, ArrayList<Materia> materias) {
        this(id,nombre,pw,programa,semestre,facultad,creditos);
        this.materias = materias;
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
    
    
}
