class Curso:
    
    def __init__(
        self,
        nombre,
        codigo,
        profesor,
        capacidad_max
    ):

        if not nombre.strip():
            raise ValueError(
                "El nombre del curso es obligatorio."
            )

        if not codigo.strip():
            raise ValueError(
                "El código del curso es obligatorio."
            )

        if not profesor.strip():
            raise ValueError(
                "El profesor es obligatorio."
            )

        if (
            isinstance(capacidad_max, bool)
            or not isinstance(capacidad_max, int)
            or capacidad_max <= 0
        ):
            raise ValueError(
                "La capacidad máxima debe ser "
                "un entero positivo."
            )

        self.__nombre = nombre.strip()
        self.__codigo = codigo.strip()
        self.__profesor = profesor.strip()
        self.__capacidad_max = capacidad_max
        self.__estudiantes_inscriptos = []

    
    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getProfesor(self):
        return self.__profesor

    def getCapacidadMax(self):
        return self.__capacidad_max

    def getEstudiantesInscriptos(self):
        return self.__estudiantes_inscriptos.copy()

    def getCantidadInscriptos(self):
        return len(self.__estudiantes_inscriptos)

    def getCuposDisponibles(self):
        return (
            self.__capacidad_max
            - len(self.__estudiantes_inscriptos)
        )

    
    def inscribirEstudiante(self, estudiante):

        if estudiante in self.__estudiantes_inscriptos:
            raise RuntimeError(
                f"El estudiante "
                f"'{estudiante.getNombre()} "
                f"{estudiante.getApellido()}' "
                f"ya está inscripto "
                f"en '{self.__nombre}'."
            )

        if self.getCuposDisponibles() == 0:
            raise RuntimeError(
                f"El curso '{self.__nombre}' "
                f"no tiene cupos disponibles."
            )

        self.__estudiantes_inscriptos.append(estudiante)

    def darDeBajaEstudiante(self, estudiante):

        if estudiante not in self.__estudiantes_inscriptos:
            raise LookupError(
                f"El estudiante "
                f"'{estudiante.getNombre()} "
                f"{estudiante.getApellido()}' "
                f"no está inscripto "
                f"en '{self.__nombre}'."
            )

        self.__estudiantes_inscriptos.remove(estudiante)

    
    def __str__(self):

        return (
            f"Curso: {self.__nombre} | "
            f"Código: {self.__codigo} | "
            f"Profesor: {self.__profesor} | "
            f"Inscriptos: "
            f"{self.getCantidadInscriptos()}/"
            f"{self.__capacidad_max}"
        )