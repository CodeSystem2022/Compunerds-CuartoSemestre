package utn.servicio;

import utn.estudiantes.modelo.Estudiante;
import utn.repositorio.EstudianteRepositorio;

import java.util.List;

@Service 
public class EstudianteServicio implements IEstudianteServicio {
    @Autowired 
    private EstudianteRepositorio estudianteRepositorio;

    @Override
    public List<Estudiante> listarEstudiantes() {
        List<Estudiante> estudiantes= estudianteRepositorio.findAll();
        return estudiantes;
    }

    @Override
    public Estudiante buscarEstudiantePorId(Integer idEstudiante) {
        Estudiante estudiante= estudianteRepositorio.findById(idEstudiante).orElse(null);
        return estudiante;
    }

    @Override
    public void guardarEstudiante(Estudiante estudiante) {

    }

    @Override
    public void eliminarEstudiante(Estudiante estudainte) {

    }
}