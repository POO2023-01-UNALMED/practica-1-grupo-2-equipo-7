package gestorAplicacion.usuario;

import java.util.ArrayList;
import gestorAplicacion.administracion.*;
import java.io.Serializable;

public class Estudiante extends Usuario implements Serializable{
    private static final long serialVersionUID = 1L;
    private String programa;
    private int semestre;
    private int creditos;
    private ArrayList<Materia> materias; 
    private ArrayList<Grupo> grupos;
    private Horario horario;
    private static ArrayList<Estudiante> estudiantes=new ArrayList<Estudiante>();
    private int estrato;
    private int sueldo;
    private int valorMatricula;
    private boolean matriculaPagada;
    private double promedio;
    private double avance;
    private final static int creditosParaGraduarse = 120;
    private ArrayList<Double> notas = new ArrayList<Double>();;
    private Beca beca;
    private ArrayList<Grupo> gruposVistos = new ArrayList<Grupo>();

    public Estudiante(long id, String nombre, String programa, int semestre, String facultad, int estrato, int sueldo) {
        super(id,nombre,facultad);
        super.setTipo("Estudiante");
        this.programa = programa;
        this.semestre = semestre;
        this.materias = new ArrayList<Materia>();
        this.grupos = new ArrayList<Grupo>();
        this.estrato = estrato;
        this.sueldo = sueldo;
        this.valorMatricula = 1234567 * estrato;
        this.horario = new Horario();
        Estudiante.estudiantes.add(this);
    }

    public String toString(){
        return "Nombre: "+ getNombre()+ " Documento: "+ getId();
    }

    public Estudiante(long id, String nombre, String programa, int semestre, String facultad, int estrato, int sueldo, ArrayList<Materia> materias, ArrayList<Grupo> gruposVistos) {
        this(id,nombre,programa,semestre,facultad, estrato, sueldo);
        this.materias = materias;
        this.gruposVistos = gruposVistos;
    }
    
    public String mostrarMaterias() {
    	String retorno = "";
        int i = 1;
    	for (Grupo grupo:grupos) {
    		retorno += "" + (i++) + "- "+grupo.getMateria().getNombre()+" | Grupo "+grupo.getNumero()+"\n";
    	}
    	return retorno;
    }

    public static int buscarEstudiante(String nombre, long id){
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

    public int getEstrato() {
        return estrato;
    }

    public void setEstrato(int estrato) {
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

    public ArrayList<Grupo> getGruposVistos() {
        return gruposVistos;
    }
    public void setGruposVistos(ArrayList<Grupo> gruposVistos) {
        this.gruposVistos = gruposVistos;
    }

    public void setHorario(Horario horario) {
        this.horario = horario;
    }


    public void eliminarMateria(Materia materia){
        this.materias.remove(materia);
        this.creditos -= materia.getCreditos();
    }

    public void eliminarGrupo(Grupo grupo){
        this.grupos.remove(grupo);
        this.eliminarMateria(grupo.getMateria());
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

    public static String mostrarEstudiantes(){
        String estudiantes = "";
        int i = 1;
        for (Estudiante estudiante : Estudiante.estudiantes){
            estudiantes += "\n" + (i++) + ". " + estudiante;
        }
        return estudiantes.substring(1, estudiantes.length());
    }

    public Materia buscarMateriaPorNombre(String nombre){
        
        for (Materia materia : this.materias){
            if (materia.getNombre().equals(nombre)){
                return materia;
            }
        }
        return null;
    }

    public boolean buscarMateriaEnInscritas(String nombre, int codigo){
        
        for (Materia materia : this.materias){
            if (materia.getNombre().equals(nombre) && materia.getCodigo()==codigo){
                return true;
            }
        }
        return false;
    }

    public void desmatricularMaterias(){
        /*
         * Desmatricula todas las materia de un estudiante
         */
        for (Grupo grupo: this.grupos){
            grupo.getMateria().setCupos(grupo.getMateria().getCupos()+1);
            grupo.setCupos(grupo.getCupos()+1);
            this.setCreditos(this.getCreditos()-grupo.getMateria().getCreditos());
            grupo.eliminarEstudiante(this);
            this.eliminarGrupo(grupo);
            this.setMaterias(new ArrayList<Materia>());
        }
        
    }

    public ArrayList<Grupo> getGrupos() {
        return grupos;
    }

    public Horario getHorario() {
        return horario;
    }

    public double getPromedio() {
        return promedio;
    }
    public void setPromedio(double promedio) {
        this.promedio = promedio;
    }

    public double getAvance() {
        return avance;
    }

    public void setAvance(double avance) {
        this.avance = avance;
    }

    public void setGrupos(ArrayList<Grupo> grupos) {
        this.grupos = grupos;
    }

    
}
