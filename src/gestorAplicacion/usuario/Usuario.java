package gestorAplicacion.usuario;
import java.io.Serializable;
import java.util.ArrayList;


public abstract class Usuario implements Serializable{
    private static final long serialVersionUID = 1L;
    private long id;
    private String nombre;
    private String tipo;
    private String pw;
    private static ArrayList<Usuario> usuariosTotales = new ArrayList<Usuario>();
    
    
    public abstract String toString();

    public Usuario(long id, String nombre, String pw){
        this.id = id;
        this.nombre = nombre;
        this.pw = pw;
        usuariosTotales.add(this);
    }

    public long getId() {
        return id;
    }
    public void setId(long id) {
        this.id = id;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }


    public String getPw() {
        return pw;
    }
    public void setPw(String pw) {
        this.pw = pw;
    }

    public static ArrayList<Usuario> getUsuariosTotales() {
        return Usuario.usuariosTotales;
    }

    public static void setUsuariosTotales(ArrayList<Usuario> usuariosTotales) {
        Usuario.usuariosTotales = usuariosTotales;
    }

}
