package gestorAplicacion.usuario;
import java.io.Serializable;
import java.util.ArrayList;


public abstract class Usuario implements Serializable{
    private static final long serialVersionUID = 1L;
    private long id;
    private String nombre;
    private String tipo;
    private String pw;
    private String facultad;
    private static ArrayList<Usuario> usuariosTotales = new ArrayList<Usuario>();
    
    
    public abstract String toString();

    public Usuario(long id, String nombre, String facultad) {
        this.id = id;
        this.nombre = nombre;
        this.facultad = facultad;
        usuariosTotales.add(this);
    }

    public Usuario(long id, String nombre, String pw, String facultad){
        this.id = id;
        this.nombre = nombre;
        this.pw = pw;
        this.facultad = facultad;
        usuariosTotales.add(this);
    }

    public static String mostrarUsuarios() {
    	String retorno = "";
    	int i = 1;
    	for(Usuario usuario:usuariosTotales) {
    		retorno += (i++)+". "+usuario.nombre+", id: "+usuario.id+"\n";
    	}
    	return retorno;
    }

    public boolean comprobacionFacultad(Usuario usuario){
        String facultad1 = this.getFacultad().toLowerCase();
        String facultad2 = usuario.getFacultad().toLowerCase();
        if (facultad1.equals(facultad2)){
            return true;
        }
        return false;
    }

    public void desmatricularDelSistema(Usuario usuario){

        for (Usuario u: Usuario.getUsuariosTotales()){

            if (usuario.equals(u)){
                    Usuario.getUsuariosTotales().remove(usuario);
                }
        }
    }

    public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
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

    public String getPw() {
        return pw;
    }
    public void setPw(String pw) {
        this.pw = pw;
    }
    
    public String getFacultad() {
        return facultad;
    }

    public void setFacultad(String facultad) {
        this.facultad = facultad;
    }

    public static ArrayList<Usuario> getUsuariosTotales() {
        return Usuario.usuariosTotales;
    }

    public static void setUsuariosTotales(ArrayList<Usuario> usuariosTotales) {
        Usuario.usuariosTotales = usuariosTotales;
    }

}
