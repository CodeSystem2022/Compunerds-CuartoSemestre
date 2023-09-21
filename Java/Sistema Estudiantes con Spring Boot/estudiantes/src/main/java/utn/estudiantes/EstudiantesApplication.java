package utn.estudiantes;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import utn.modelo.Estudiantes2022;
import utn.servicio.EstudianteServicio;

import org.slf4j.LoggerFactory;
import org.slf4j.Logger;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
	@Autowired
	private EstudianteServicio estudianteServicio;
	private static final Logger logger = LoggerFactory.getLogger(EstudiantesApplication.class);

	String nl= System.lineSeparator();

	public static void main(String[] args) {
		logger.info("Iniciando la applicacion...");
		//Levantar la fabrica de Spring
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("App finalizada");
	}

	@Override
	public void run(String... args) throws Exception {
		logger.info("Ejecutando el metodo run de Spring");
	}
}
