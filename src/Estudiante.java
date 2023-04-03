import java.util.ArrayList;
import java.util.Scanner;
public class Estudiante extends Usuario {
    private String programa;
    private int semestre;
    private String facultad;
    private int creditos;
    private ArrayList<Materia> materias;
    private ArrayList<Grupo> grupos;

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos) {
        super(id,nombre,pw);
        this.programa = programa;
        this.semestre = semestre;
        this.facultad = facultad;
        this.creditos = creditos;
        this.materias = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
        //Si es necesario declarar un nuevo array al crear el objeto o no?

    }

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos, ArrayList<Materia> materias) {
        this(id,nombre,pw,programa,semestre,facultad,creditos);
        this.materias = materias;
    }

    public void matricularMateria() {
    	Scanner scanner = new Scanner(System.in); 
    	int opcion;
    	
    	System.out.println("¿Cómo desea realizar la búsqueda?"
    			+ "\n1: Por nombre."
    			+ "\n2: Por créditos."
    			+ "\n3: Por código");
    	do {
    		opcion = scanner.nextInt();
    	
    		switch(opcion) {
    			default:
    				System.out.println("Ha ingresado un valor inválido. Intente nuevamente");
    		}
    	}while(opcion<1 || opcion>3);
    }
    
    public String mostrarMaterias() {
    	String retorno = "";
    	for (Grupo grupo:grupos) {
    		retorno += "- "+grupo.getMateria().getNombre()+" | Grupo "+grupo.getNumero()+"\n";
    	}
    	return retorno;
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
