package Java.Clase1.Conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){
        Connection conexion = null;
        //Variables para conectarnos a la base de datos
        var baseDatos = "estudiantes2022";
        var url = "jdbc:mysql://localhost:5432/"+baseDatos;
        var usuario = "root";
        var password = "ADMIN";

        //cargamos la clase de driver de mysql en memoria
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        }catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrió un error en la conexión: "+e.getMessage());
        }//Fin catch
        return conexion;
    }//Fin método Connection
}