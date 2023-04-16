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
    private short estrato;
    private int sueldo;
    private int valorMatricula;
    private boolean matriculaPagada;
    private double promedio;
    private double avance;
    private final static int creditosParaGraduarse = 120;
    private ArrayList<Double> notas = new ArrayList<Double>();;
    private Beca beca;

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos, short estrato, int sueldo) {
        super(id,nombre,pw);
        this.programa = programa;
        this.semestre = semestre;
        this.facultad = facultad;
        this.creditos = creditos;
        this.materias = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
        this.estrato = estrato;
        this.sueldo = sueldo;
        this.valorMatricula = 1234567 * estrato;
        
    }

    public String toString(){
        return "Nombre: "+ getNombre()+ "\nDocumento: "+ getId();
    }

    public Estudiante(long id, String nombre, String pw, String programa, int semestre, String facultad, int creditos, short estrato, int sueldo, ArrayList<Materia> materias) {
        this(id,nombre,pw,programa,semestre,facultad,creditos, estrato, sueldo);
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

    public short getEstrato() {
        return estrato;
    }

    public void setEstrato(short estrato) {
        this.estrato = estrato;
    }

    public int getSueldo() {
        return sueldo;
    }

    public void setSueldo(int sueldo) {
        this.sueldo = sueldo;
    }
    
    public boolean isMatriculaPagada() {
        return matriculaPagada;
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

    public boolean pagarMatricula(){

        if (this.sueldo >= this.valorMatricula){
            this.sueldo -= this.valorMatricula;
            this.matriculaPagada = true;
            return true;
        }

        this.matriculaPagada = false;
        return false;
    }

    private void calcularPromedio(){
        double promedio = 0;

        for (double nota: this.notas){
            promedio += nota;
        }
        promedio = promedio / ((double) this.notas.size());
        this.promedio = promedio;
    }

    private void calcularAvance(){
        double creditosVistos = 0;

        for (Materia materia: materias){
            creditosVistos += materia.getCreditos();
        }

        this.avance = (creditosVistos * 100.0) / creditosParaGraduarse;
    }

    private void agregarNotas(ArrayList<Double> notas){

        for (double nota: notas){
            this.notas.add(nota);
        }
        this.calcularPromedio();
    }

}
