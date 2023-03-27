
import java.util.ArrayList;

public class Materia {
    
    //nombre y codigo las declare como constantes. ¿Estan de acuerdo?
    private final String nombre;
    private final int codigo;
    private int creditos;
    private String facultad;
    //¿Este atributo cupos si se necesita en esta clase?
    private int cupos;
    private ArrayList<Materia> prerrequisitos;
    private ArrayList<Grupo> grupos;

    public Materia(String nombre, int codigo, int creditos, String facultad, int cupos) {
        this.nombre = nombre;
        this.codigo = codigo;
        this.creditos = creditos;
        this.facultad = facultad;
        this.cupos = cupos;
        this.prerrequisitos = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
    }

    public Materia(String nombre, int codigo, int creditos, String facultad, int cupos, ArrayList<Materia> prerrequisitos) {
        this(nombre, codigo, creditos, facultad, cupos);
        this.prerrequisitos = prerrequisitos;
    }

    public Materia(String nombre, int codigo, int creditos, String facultad, int cupos, ArrayList<Materia> prerrequisitos, ArrayList<Grupo> grupos) {
        this(nombre, codigo, creditos, facultad, cupos, prerrequisitos);
        this.grupos = grupos;
    }
    
    public String getNombre() {
        return this.nombre;
    }
    
    public int getCodigo() {
        return this.codigo;
    }
    
    public int getCreditos() {
        return this.creditos;
    }

    public void setCreditos(int creditos) {
        this.creditos = creditos;
    }

    public String getFacultad() {
        return this.facultad;
    }

    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }

    public int getCupos() {
        return this.cupos;
    }

    public void setCupos(int cupos) {
        this.cupos = cupos;
    }

    public ArrayList<Materia> getPrerrequisitos() {
        return this.prerrequisitos;
    }

    public void setPrerrequisitos(ArrayList<Materia> prerrequisitos) {
        this.prerrequisitos = prerrequisitos;
    }

    public ArrayList<Grupo> getGrupos() {
        return this.grupos;
    }

    public void setGrupos(ArrayList<Grupo> grupos) {
        this.grupos = grupos;
    }
    
    //Esta un poco ambigua la definicion de este metodo
    public void crearGrupo(){
        
    }
    
    //Este metodo tambien tenemos que hablarlo
    public String mostrarContenidos(){
        return "";
    }
    
    public boolean existenciaGrupo(Grupo grupoBuscado){
        
        if (!grupos.isEmpty()){
            
            for (Grupo grupo: grupos){
                
                if (grupo.equals(grupoBuscado)){
                    return true;
                }
            }
            
            return false;
        }
        else{
            return false;
        }
    }
    
    public void eliminarGrupo(Grupo grupo){
        this.grupos.remove(grupo);
    }
     
}
