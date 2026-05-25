from persona import Persona


class Estudiante(Persona):
    
    _contador_id = 1

    def __init__(
        self,
        nombre,
        apellido,
        matricula,
        carrera
    ):

        super().__init__(nombre, apellido)

        # matricula llega como str desde el menú
        if not str(matricula).strip():
            raise ValueError(
                "La matrícula no puede estar vacía."
            )

        if not carrera.strip():
            raise ValueError(
                "La carrera no puede estar vacía."
            )

        self.__id = Estudiante._contador_id
        Estudiante._contador_id += 1

        self.__matricula = str(matricula).strip()
        self.__carrera = carrera.strip()

        self.__cursos_inscriptos = []

    
    def getId(self):
        return self.__id

    def getMatricula(self):
        return self.__matricula

    def getCarrera(self):
        return self.__carrera

    def getCursosInscriptos(self):
        return self.__cursos_inscriptos.copy()

   
    def agregarCurso(self, curso):

        if curso in self.__cursos_inscriptos:
            raise RuntimeError(
                f"El curso '{curso.getNombre()}' "
                f"ya está asignado al estudiante."
            )

        self.__cursos_inscriptos.append(curso)

    def removerCurso(self, curso):

        if curso not in self.__cursos_inscriptos:
            raise LookupError(
                f"El curso '{curso.getNombre()}' "
                f"no figura entre las inscripciones "
                f"del estudiante."
            )

        self.__cursos_inscriptos.remove(curso)

    
    def __str__(self):

        return (
            f"ID: {self.__id} | "
            f"{super().__str__()} | "
            f"Matrícula: {self.__matricula} | "
            f"Carrera: {self.__carrera}"
        )