package gestorAplicacion.administracion;
import java.io.Serializable;
import java.util.*;
import gestorAplicacion.usuario.*;

public class Grupo implements Serializable{
	private static final long serialVersionUID = 1L;
	private Materia materia;
    private int numero;
    private Profesor profesor;
    private ArrayList<String> horario; 
    private int cupos;
    private Salon salon;
    private ArrayList<Estudiante> estudiantes;

    public Grupo(Materia materia, int numero, Profesor profesor, ArrayList<String> horario, int cupos, Salon salon){
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
        if (this.estudiantes.get(i).equals(estudiante)){
          		this.estudiantes.remove(i);
		  		this.cupos++;
				estudiante.eliminarGrupo(this);
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

	public ArrayList<String> getHorario() {
		return this.horario;
	}

	public void setHorario(ArrayList<String> horario) {
		this.horario = horario;
	}

	public int getCupos() {
		return this.cupos;
	}

	public void setCupos(int cupos) {
		this.cupos = cupos;
	}

	public Salon getSalon() {
		return this.salon;
	}

	public void setSalon(Salon salon) {
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
