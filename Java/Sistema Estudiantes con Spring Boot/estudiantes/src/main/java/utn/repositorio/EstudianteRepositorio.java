package utn.repositorio;

import org.springframework.data.jpa.repository.JpaRepository;

import utn.modelo.Estudiante;

public interface EstudianteRepositorio extends JpaRepository<Estudiante, Integer> {

}