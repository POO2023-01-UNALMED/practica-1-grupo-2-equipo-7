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
	private static ArrayList<Grupo> gruposTotales = new ArrayList<Grupo>();

    public Grupo(Materia materia, int numero, Profesor profesor, ArrayList<String> horario, int cupos, Salon salon){
      this.materia = materia;
      this.numero=numero;
      this.profesor=profesor;
      this.horario=horario;
      this.cupos=cupos;
      this.salon=salon;
      this.estudiantes=new ArrayList<Estudiante>();
	  Grupo.gruposTotales.add(this);
    } 
    
	public Grupo(Materia materia, int numero, Profesor profesor){
      this.materia = materia;
      this.numero=numero;
      this.profesor=profesor;
	  Grupo.gruposTotales.add(this);
    } 

    public String mostrarInformacionGrupo(){
			String retorno= "Número del grupo: "+this.numero+", Profesor: "+this.profesor+", Horario: "+this.horario+", Cupos: "+this.cupos+", Salón: "+this.salon;
			return retorno;
		}


    public boolean existenciaEstudiante(Estudiante estudiante){
      for (int j=0;j<this.estudiantes.size();j++){
        if (this.estudiantes.get(j).getId() == estudiante.getId()){
          return true;
        }
      }
      return false;
    }

	public void eliminarEstudiante(Estudiante estudiante){
		int indice = -1;
		for (int i=0;i<this.estudiantes.size();i++){
			if (this.estudiantes.get(i).getNombre().equals(estudiante.getNombre())){
					indice = i;
					this.cupos++;
					estudiante.eliminarGrupo(this);
					break;
			}
		}
		if (indice != -1){
			this.estudiantes.remove(indice);
		}
    }

	public static Grupo buscarGrupo(Materia materiaE, Grupo grupoE){
		int indicei = -1;
		int indicej = -1;
		for (int i = 0; i<Materia.getMateriasTotales().size(); i++){
			Materia materia = Materia.getMateriasTotales().get(i);
			if (materia.getNombre().equals(materiaE.getNombre())){
				indicei = i;
				for (int j = 0; j<materia.getGrupos().size(); j++){
					Grupo grupo = materia.getGrupos().get(j);
					if (grupo.getNumero() == grupoE.getNumero()){
						indicej = j;
						break;
					}
				}
			}
		}
		return Materia.getMateriasTotales().get(indicei).getGrupos().get(indicej);
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

	public static ArrayList<Grupo> getGruposTotales() {
		return gruposTotales;
	}
	
}
