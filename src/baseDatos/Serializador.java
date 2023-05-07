package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import gestorAplicacion.administracion.*;
import gestorAplicacion.usuario.*;

public class Serializador {

    private static void serializar(ArrayList<? extends Object> lista, String nombre) {
    
        File archivo = new File("");

        try{
            File path = new File(archivo.getAbsolutePath()+"/src/baseDatos/temp/"+nombre+".txt"); 
            
            FileOutputStream f = new FileOutputStream(path);
            ObjectOutputStream o = new ObjectOutputStream(f);
            
            o.writeObject(lista);

            o.close();
            f.close();
        }
        catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo");
        }
        catch(IOException e){
            System.out.println("Error Flujo de inicializacion");
        }
        // catch(ClassNotFoundException e){
        //     e.printStackTrace();
        // }
    }

    public static void serializarListas(){
        // Aqui van las clases que vamos a serealizar: ejem:
        Serializador.serializar(Estudiante.getEstudiantes(), "Estudiantes");
        Serializador.serializar(Grupo.getGruposTotales(), "Grupos");
        Serializador.serializar(Materia.materiasTotales, "Materias");
        Serializador.serializar(Usuario.getUsuariosTotales(), "Usuarios");
        Serializador.serializar(Coordinador.getCoordinadoresTotales(), "Coordinadores");
        Serializador.serializar(Horario.getHorariosTotales(), "Horarios");
        Serializador.serializar(Salon.salones, "Salones");
        Serializador.serializar(Beca.getBecas(), "Becas");
        Serializador.serializar(Profesor.getProfesores(), "Profesores");

        // y asi ...
    }


}
