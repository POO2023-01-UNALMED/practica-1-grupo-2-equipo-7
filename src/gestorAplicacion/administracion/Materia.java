package gestorAplicacion.administracion;
import java.util.ArrayList;
import gestorAplicacion.usuario.*;
import java.io.Serializable;

public class Materia implements Serializable{
    
    //nombre y codigo las declare como constantes. �Estan de acuerdo? si
    private static final long serialVersionUID = 1L;
    private String nombre;
    private final int codigo;
    private String descripcion;
    private int creditos;
    private String facultad;
    //�Este atributo cupos si se necesita en esta clase?
    private int cupos;
    private ArrayList<Materia> prerrequisitos;
    private ArrayList<Grupo> grupos;
    // Es publico para que coordinador tenda acceso 
    public static ArrayList<Materia> materiasTotales = new ArrayList<Materia>();
    private String abreviatura;

    public Materia(String nombre, int codigo, String descripcion, int creditos, String facultad) {
        this.nombre = nombre;
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.creditos = creditos;
        this.facultad = facultad;
        this.prerrequisitos = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
        this.hacerAbreviatura(nombre);
        materiasTotales.add(this);

    }

    public Materia(String nombre, int codigo, String descripcion, int creditos, String facultad, ArrayList<Materia> prerrequisitos) {
        this(nombre, codigo, descripcion, creditos, facultad);
        this.prerrequisitos = prerrequisitos;
    }

    public Materia(String nombre, int codigo, String descripcion,int creditos, String facultad, ArrayList<Materia> prerrequisitos, ArrayList<Grupo> grupos) {
        this(nombre, codigo, descripcion, creditos, facultad, prerrequisitos);
        this.grupos = grupos;
    }
    
    public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
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
    
    public int cantidadCupos(){
        int cantidad = 0;
        for (Grupo pGrupo:getGrupos()){
            cantidad+=pGrupo.getCupos();
        }
        return cantidad;
    }

    public String getAbreviatura() {
        return abreviatura;
    }

    public void setAbreviatura(String abreviatura) {
        this.abreviatura = abreviatura;
    }

    //Esta un poco ambigua la definicion de este metodo
    public Grupo crearGrupo(int numero, Profesor profesor, ArrayList<String> horario, int cupos, Salon salon){
        
    	//Faltaría que implementen los respectivos metodos y atributos en la clase profesor
    	//para comprobar que si se pueda asignar al grupo.
    	Grupo grupo = new Grupo(this, numero, profesor, horario, cupos, salon);
    	
    	//No se si sería mejor crear otro metodo para añadir un grupo o añadirlo aquí mismo. Hay que hablarlo.
        cantidadCupos();
    	this.grupos.add(grupo);
    	
    	return grupo;
    }
    //Cambié el metodo de un void a uno que retorne un Grupo por requerimiento de mi funcionalidad Att: Sebastian
    
    
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
    
    public void eliminarGrupo(int numero){
    	Grupo grupo = this.grupos.get(numero-1);
    	grupo.getProfesor().desvincularGrupo(grupo);
    	grupo.getSalon().getHorario().liberarHorario(grupo.getHorario());
        this.grupos.remove(grupo);
        for(int i=numero-1;i<this.grupos.size();i++) {
        	Grupo grupoCamb = this.grupos.get(i);
        	int nGrupoAnt = grupoCamb.getNumero();
        	grupoCamb.setNumero(nGrupoAnt-1);
        }
        
    }
    
    public void agregarGrupo(int numero, Profesor profesor, ArrayList<String> horario, int cupos, Salon salon) {
    	//el metodo recibe los parametros necesarios para crear un nuevo grupo
    	boolean dispSalon = true;
    	boolean dispProfesor = true;
    	boolean daMateria = profesor.daMateria(this);
    	
    	//Se comprueba la disponibilidad del profesor y el salon para el horario ingresado
    	for(String hor:horario) {
    		dispProfesor = profesor.getHorario().comprobarDisponibilidad(hor);
    		dispSalon = salon.getHorario().comprobarDisponibilidad(hor);
    		
    		if(!dispProfesor||!dispSalon) {
    			break;
    		}
    	}
    	

    	//En caso de contar con disponibilidad, se procede a declarar el nuevo grupo y agregarselo a su respectiva meteria, profesor y salon
    	if(dispProfesor&&dispSalon&&daMateria) {
    		Grupo nGrupo = crearGrupo(numero,profesor,horario,cupos,salon);
    		salon.getHorario().ocuparHorario(horario, nGrupo);
    		profesor.vincularGrupo(nGrupo);
    	}
    }

    public Grupo buscarGrupoDeEstudiante(Estudiante estudiante){

        for (Grupo grupo: this.grupos){
            for (Estudiante e: grupo.getEstudiantes()){
                if (e == estudiante){
                    return grupo;
                }
            }
        }
        return null;
    }

    public static ArrayList<Materia> getMateriasTotales(){
        return materiasTotales;
    }

    public static int buscarMateria(String nombre, int codigo){
        /*
         * Si existe el estudiante retorna su indice en el Arraylist materiaTotales
         * Si no existe, retorna -1
         */
        for (int i = 0; i < materiasTotales.size(); i++){
            if (materiasTotales.get(i).getNombre().equals(nombre) && materiasTotales.get(i).getCodigo() == codigo){
                return i;
            }
        }
        return -1;
    }

    public static boolean puedeVerMateria(Estudiante estudiante,Grupo grupo){
        /*
         * Comprueba si un estudiante puede estar en un grupo
         */
        
        if (!(estudiante.getCreditos()+grupo.getMateria().getCreditos()<=Coordinador.getLimitesCreditos())){
            return false;
        }
        if (!estudiante.getHorario().comprobarDisponibilidad(grupo.getHorario())){
            return false;
        }
        if (!(grupo.getCupos()!=0)){
            return false;
        }
        if (!comprobarPrerrequisitos(estudiante,grupo.getMateria())){
            return false;
        }
        return true;
    } 

    public static boolean comprobarPrerrequisitos(Estudiante estudiante,Materia materia){
        /*
         * Comprueba si un estudiante cumple los pre-requisitos de una materia
         */
        
        ArrayList<Materia> materiasVistas = new ArrayList<Materia>();
        
        for (Grupo pGrupo:estudiante.getGruposVistos()){
            materiasVistas.add(pGrupo.getMateria());
        }

        for (Materia pMateria:materia.getPrerrequisitos()){
            if(!materiasVistas.contains(pMateria)){
                return false;
            }    
        }
        return true;
    }

    public void hacerAbreviatura(String nombre){
        String abreviatura = "";

        if (nombre.length() <= 13){
            this.abreviatura = nombre;
        }
        else{
            String[] palabras = nombre.split("\\s");
            for (String palabra : palabras){
                if (palabra.length() >= 3){
                    abreviatura += palabra.substring(0, 3) + " ";
                }
                else{
                    abreviatura += palabra.substring(0, palabra.length()) + " ";
                }
            }
            if (abreviatura.length() <= 13){
                this.abreviatura = abreviatura;
            }
            else{
                this.abreviatura = abreviatura.substring(0, 13);
            }
        }
    }
}
