class Facultad:
    
    def __init__(self):
        self.__estudiantes = []
        self.__cursos = []

   
    def agregarEstudiante(self, estudiante):

        for estudianteExistente in self.__estudiantes:
            if (
                estudianteExistente.getMatricula()
                == estudiante.getMatricula()
            ):
                raise ValueError(
                    f"Ya existe un estudiante "
                    f"con matrícula "
                    f"'{estudiante.getMatricula()}'."
                )

        self.__estudiantes.append(estudiante)
        print(
            f"\n  Estudiante agregado "
            f"correctamente."
            f"\n  ID: {estudiante.getId()}"
        )

    def agregarCurso(self, curso):

        for cursoExistente in self.__cursos:
            if (
                cursoExistente.getCodigo()
                == curso.getCodigo()
            ):
                raise ValueError(
                    f"Ya existe un curso "
                    f"con código "
                    f"'{curso.getCodigo()}'."
                )

        self.__cursos.append(curso)
        print("\n  Curso agregado correctamente.")

    
    def buscarEstudiante(self, matricula):

        for estudiante in self.__estudiantes:
            if estudiante.getMatricula() == matricula:
                return estudiante

        raise LookupError(
            f"No existe un estudiante "
            f"con matrícula '{matricula}'."
        )

    def buscarCurso(self, codigo):

        for curso in self.__cursos:
            if curso.getCodigo() == codigo:
                return curso

        raise LookupError(
            f"No existe un curso "
            f"con código '{codigo}'."
        )

    
    def inscribirEstudiante(self, matricula, codigo_curso):

        estudiante = self.buscarEstudiante(matricula)
        curso = self.buscarCurso(codigo_curso)

        curso.inscribirEstudiante(estudiante)
        estudiante.agregarCurso(curso)

        print("\n  Inscripción realizada correctamente.")

    
    def darDeBajaEstudiante(self, matricula, codigo_curso):

        estudiante = self.buscarEstudiante(matricula)
        curso = self.buscarCurso(codigo_curso)

        # Curso y Estudiante ya validan internamente
        curso.darDeBajaEstudiante(estudiante)
        estudiante.removerCurso(curso)

        print("\n  Baja realizada correctamente.")

    
    def mostrarCursos(self):

        if not self.__cursos:
            print("\n  No hay cursos registrados.")
            return

        print("\n╔══════════════ CURSOS ══════════════╗")

        for curso in self.__cursos:
            print(curso)
            estudiantes = [
                f"{e.getNombre()} {e.getApellido()}"
                for e in curso.getEstudiantesInscriptos()
            ]
            estudiantesTexto = (
                ", ".join(estudiantes)
                if estudiantes
                else "Ninguno"
            )
            print(f"  Estudiantes: {estudiantesTexto}")

    def mostrarEstudiantes(self):

        if not self.__estudiantes:
            print("\n  No hay estudiantes registrados.")
            return

        print("\n╔═══════════ ESTUDIANTES ═══════════╗")

        for estudiante in self.__estudiantes:
            print(estudiante)
            cursos = [
                curso.getNombre()
                for curso in estudiante.getCursosInscriptos()
            ]
            cursosTexto = (
                ", ".join(cursos)
                if cursos
                else "Ninguno"
            )
            print(f"  Cursos: {cursosTexto}")