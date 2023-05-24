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
                this.horario = new Horario();
                salones.add(this);
        }
        
        public static String mostrarSalones() {
                String retorno = "";
                int i = 1;
                for(Salon salon:salones) {
                        retorno += (i++)+". "+salon.lugar+".\n";
                }
                return retorno;
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

        public Horario getHorario() {
                return horario;
        }

        public void setHorario(Horario horario) {
                this.horario = horario;
        }

        public static ArrayList<Salon> getSalones() {
                return salones;
        }

        public static void setSalones(ArrayList<Salon> salones) {
                Salon.salones = salones;
        }
    
}