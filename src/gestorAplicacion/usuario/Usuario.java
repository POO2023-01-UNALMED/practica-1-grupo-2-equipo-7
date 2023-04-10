package gestorAplicacion.usuario;
import java.io.Serializable;

public abstract class Usuario implements Serializable{
    private long id;
    private String nombre;
    private String tipo;
    private String pw;
    private static final long serialVersionUID = 1L;
    
    public abstract String toString();

    public Usuario(long id, String nombre, String pw){
        this.id = id;
        this.nombre = nombre;
        this.pw = pw;
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
}
