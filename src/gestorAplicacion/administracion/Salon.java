package gestorAplicacion.administracion;
import java.util.ArrayList;
import java.io.Serializable;

public class Salon implements Serializable{
    private String lugar;
    private int aforo;
    private Horario horario;
    public static ArrayList<Salon> salones= new ArrayList<Salon>();
    private static final long serialVersionUID = 1L;

    public Salon(String lugar,int aforo){
        this.lugar = lugar;
        this.aforo = aforo;
        salones.add(this);
    }
    
    public static ArrayList<Salon> getSalones() {
		return salones;
	}

	public static void setSalones(ArrayList<Salon> salones) {
		Salon.salones = salones;
	}

	public void setHorario(Horario horario) {
        this.horario = horario;
    }
    
    public Horario getHorario() {
        return this.horario;
    }
    
	public String getLugar() {
        return lugar;
	}
    
	public void setLugar(String lugar) {
        this.lugar = lugar;
	}
    
	public int getAforo() {
        return aforo;
	}
    
	public void setAforo(int aforo) {
        this.aforo = aforo;
	}
}