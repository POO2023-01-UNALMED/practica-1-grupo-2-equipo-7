import java.util.*;
package administracion;

public class Grupo {
		private Materia materia;
    private int numero;
    private Profesor profesor;
    private Horario horario; 
    private int cupos;
    private String salon;
    private ArrayList<Estudiante> estudiantes;

    public Grupo(Materia materia, int numero, Profesor profesor, Horario horario, int cupos, String salon){
      this.materia = materia;
      this.numero=numero;
      this.profesor=profesor;
      this.horario=horario;
      this.cupos=cupos;
      this.salon=salon;
      this.estudiantes=new ArrayList<Estudiante>();
    } 

    public String mostrarInformacionGrupo(){
			String retorno= "Número del grupo: "+this.numero+", Profesor: "+this.profesor+", Horario: "+this.horario+", Cupos: "+this.cupos+", Salón: "+this.salon;
			return retorno;
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
		  		this.cupos++;
		  		break;
        }
      }
    }

    public void agregarEstudiante(Estudiante estudiante){
      this.estudiantes.add(estudiante);
	  	this.cupos--;
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
