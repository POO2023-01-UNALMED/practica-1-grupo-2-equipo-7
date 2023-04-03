import java.util.*;

public class Grupo {
	private Materia materia;
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

	public int getNumero() {
		return this.numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public Profesor getProfesor() {
		return this.profesor;
	}

	public void setProfesor(Profesor profesor) {
		this.profesor = profesor;
	}

	public String getHorario() {
		return this.horario;
	}

	public void setHorario(String horario) {
		this.horario = horario;
	}

	public int getCupos() {
		return this.cupos;
	}

	public void setCupos(int cupos) {
		this.cupos = cupos;
	}

	public String getSalon() {
		return this.salon;
	}

	public void setSalon(String salon) {
		this.salon = salon;
	}

	public ArrayList<Estudiante> getEstudiantes() {
		return this.estudiantes;
	}

	public void setEstudiantes(ArrayList<Estudiante> estudiantes) {
		this.estudiantes = estudiantes;
	}
	
	public Materia getMateria() {
		return this.materia;
	}
	
	public void setMateria(Materia materia) {
		this.materia = materia;
	}
}
