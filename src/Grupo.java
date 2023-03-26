// !! falta getters y setters, Agregue los que necesitaba

import java.util.*;

public class Grupo {
    private int numero;
    private Profesor profesor;
    private String horario; 
    //En esta parte no se que tipo de dato es la variable horario
    private int cupos;
    private String salon;
    private ArrayList<Estudiante> estudiantes;

    public Grupo(int numero, Profesor profesor, String horario, int cupos, String salon){
      this.numero=numero;
      this.profesor=profesor;
      //Otra vez lo mismo, el tipo de dato de horario
      this.horario=horario;
      this.cupos=cupos;
      this.salon=salon;
      this.estudiantes=new ArrayList<Estudiante>();
    } 

    public void mostrarInformacionGrupo(){
      System.out.println("Número del grupo: "+this.numero+", Profesor: "+this.profesor+", Horario: "+this.horario+", Cupos: "+this.cupos+", Salón: "+this.salon);
    }

    public boolean existenciaEstudiante(Estudiante estudiante){
      for (int j=0;j<this.estudiantes.size();j++){
        if (this.estudiantes.get(j)==estudiante){
          return true;
        }
      }
      return false;
    }

    public void eliminarEstudiante(Estudiante estudiante){
      for (int i=0;i<this.estudiantes.size();i++){
        if (this.estudiantes.get(i)==estudiante){
          this.estudiantes.remove(i);
        }
      }
    }

    public void agregarEstudiante(Estudiante estudiante){
      this.estudiantes.add(estudiante);
    }


    // Getters

    public Profesor getProfesor() {
        return profesor;
    }

    public ArrayList<Estudiante> getEstudiantes() {
        return estudiantes;
    }

}
