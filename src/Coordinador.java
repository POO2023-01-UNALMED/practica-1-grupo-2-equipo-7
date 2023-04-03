public class Coordinador extends Usuario {
    private String facultad;
    private int limitesCreditos;

    public Coordinador(String facultad,int limitesCreditos,long id, String nombre, String pw) {
    
        //podemos ponerlos ahora o despues con el super o con los set del metodo
        // super(id,nombre,tipo,pw);
        super(id, nombre,pw);
        this.facultad = facultad;
        this.limitesCreditos = limitesCreditos;
    }


    //Metodos

    public void crearMateria(){
        // Agrega una materia a la "base de datos" pero antes necesitamos saber como funciona la serializacion

        // Faltan los atributos para crear una materia

        Materia materia = new Materia();
    }

    public String desmatricular(Estudiante estudiante, Grupo grupo){
        // Es desmatricular de... ya no eres estudiante o desmatricular de... ya no estar en una materia

        boolean estaMatriculado = grupo.existenciaEstudiante(estudiante);

        if (estaMatriculado){

            grupo.eliminarEstudiante(estudiante);
            return "El estudiante ha sido desmatriculado de la materia y su respectivo grupo";

        }

        else{

            return "El estudiante no estaba matriculado";

        }

    }

    public void contratarProfesor(){
        // Agrega profesor a la base de datos, de nuevo como funcionara?

        Profesor profesor = new Profesor();
    }


    // FUSIONE resturarEstudiantesInscritosEnMateria Y resturarProfesoresInvolucradosEnMateria EN resturarMateria.
    public void resturarMateria(Materia materia){
        for (int i=0;i<materia.getGrupos().size();i++){
            Grupo puntero_Grupo = materia.getGrupos().get(i);
            puntero_Grupo.getProfesor().desvincularGrupo(puntero_Grupo);

            for (int j=0;j<puntero_Grupo.getEstudiantes().size();j++){
                Estudiante puntero_Estudiante = puntero_Grupo.getEstudiantes().get(j);
                puntero_Estudiante.desmatricularMateria(materia);
            }   
        }
    }

    // Getters

    public String getFacultad() {
        return this.facultad;
    }
        
    public int getLimitesCreditos() {
        return this.limitesCreditos;
    }



    // Setters

    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }

    public void setLimitesCreditos(int limitesCreditos) {
        this.limitesCreditos = limitesCreditos;
    }

    // FALTAN LO SETTERS Y LOS GETTERS DE LOS ATRIBUTOS QUE VIENE DE USUARIO.


}