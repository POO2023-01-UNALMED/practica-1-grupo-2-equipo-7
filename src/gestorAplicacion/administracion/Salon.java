package gestorAplicacion.administracion;
//import java.util.ArrayList;

public class Salon {
    private String lugar;
    private int aforo;
    private Horario horario;

    public Salon(String lugar,int aforo){
        this.lugar = lugar;
        this.aforo = aforo;
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