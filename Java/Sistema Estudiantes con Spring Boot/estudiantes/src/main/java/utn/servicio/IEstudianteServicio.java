package utn.servicio;

import utn.modelo.Estudiante;
import java.util.List;

public interface IEstudianteServicio{
    public List<Estudiante> listarEstudiantes();
    public Estudiante buscarEstudiantePorId(Integer idEstudiante);
    public void guardarEstudiante(Estudiante estudiante);
    public void eliminarEstudiante(Estudiante estudiante);
}
