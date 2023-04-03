
import java.util.ArrayList;

public class Materia {
    
    //nombre y codigo las declare como constantes. �Estan de acuerdo?
    private final String nombre;
    private final int codigo;
    private String descripcion;
    private int creditos;
    private String facultad;
    //�Este atributo cupos si se necesita en esta clase?
    private int cupos;
    private ArrayList<Materia> prerrequisitos;
    private ArrayList<Grupo> grupos;

    public Materia(String nombre, int codigo, String descripcion, int creditos, String facultad, int cupos) {
        this.nombre = nombre;
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.creditos = creditos;
        this.facultad = facultad;
        this.cupos = cupos;
        this.prerrequisitos = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
    }

    public Materia(String nombre, int codigo, String descripcion, int creditos, String facultad, int cupos, ArrayList<Materia> prerrequisitos) {
        this(nombre, codigo, descripcion, creditos, facultad, cupos);
        this.prerrequisitos = prerrequisitos;
    }

    public Materia(String nombre, int codigo, String descripcion,int creditos, String facultad, int cupos, ArrayList<Materia> prerrequisitos, ArrayList<Grupo> grupos) {
        this(nombre, codigo, descripcion, creditos, facultad, cupos, prerrequisitos);
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
    public void crearGrupo(int numero, Profesor profesor, String horario, int cupos, String salon){
        
    	//Faltaría que implementen los respectivos metodos y atributos en la clase profesor
    	//para comprobar que si se pueda asignar al grupo.
    	Grupo grupo = new Grupo(numero, profesor, horario, cupos, salon);
    	
    	//No se si sería mejor crear otro metodo para añadir un grupo o añadirlo aquí mismo. Hay que hablarlo.
    	this.grupos.add(grupo);
    	
    }
    
    //Este metodo tambien tenemos que hablarlo
    public String mostrarContenidos(){
        String contenido =  "Materia: " + this.nombre +
        					"\nCodigo: " + this.codigo +
        					"\nCreditos: " + this.creditos +
        					"\nFacultad: " + this.facultad +
        					"\nDescripcion:\n" + this.descripcion;
        return contenido;
        					
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