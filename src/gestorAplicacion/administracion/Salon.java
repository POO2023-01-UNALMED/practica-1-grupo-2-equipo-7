package gestorAplicacion.administracion;
import java.util.ArrayList;

public class Salon {
    private String lugar;
    private int aforo;
    private Grupo[][] horario = new Grupo[7][24];

    public Salon(String lugar,int aforo){
        this.lugar = lugar;
        this.aforo = aforo;
    }

    public void agregarGrupo(ArrayList<String> horario,Grupo grupo){
        for (int i = 0;i<horario.size();i++){
            
            // tiene que dar el horario en formato: "1-08-10" "Dia-hora inicio-hora final" todo en horario militar
            String detalles = horario.get(i);
            int dia = Integer.parseInt(detalles.substring(0, 1))-1;
            int horaInicio = Integer.parseInt(detalles.substring(2, 4));
            int horaFinal = Integer.parseInt(detalles.substring(5, 7))-1;
            
            for (int e =horaInicio;e<=horaFinal;e++){
                this.horario[dia][e] = grupo;
            }

        }
    }

    public boolean comprobarDisponibilidadSalon(String hora){
        
        int dia = Integer.parseInt(hora.substring(0, 1))-1;
        int horaInicio = Integer.parseInt(hora.substring(2, 4));
        int horaFinal = Integer.parseInt(hora.substring(5, 7))-1;
        
        boolean boo = true;

        for (int e =horaInicio;e<=horaFinal;e++){
            if (this.horario[dia][e] != null){
                boo = false;
            }
        }
        return boo;
    }

    // public void verHorario() {
    //     for(int i=0;i<7;i++){
    //         System.out.println("");
    //         System.out.print(i+1+": ");
    //         for(int e =0;e<24;e++){
    //             System.out.print((this.horario[i][e]).getSalon());
    //         }
    //     }
    // }

}
