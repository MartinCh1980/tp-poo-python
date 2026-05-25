from facultad import Facultad
from estudiante import Estudiante
from curso import Curso

class SistemaFacultad:

    def __init__(self):
        self.__facultad = Facultad()

    def mostrarMenu(self):
        print("\n╔══════════════════════════════════════════════╗")
        print("║      SISTEMA DE GESTIÓN DE FACULTAD         ║")
        print("╠══════════════════════════════════════════════╣")
        print("║  0 - Salir                                  ║")
        print("║  1 - Agregar estudiante                     ║")
        print("║  2 - Agregar curso                          ║")
        print("║  3 - Mostrar estudiantes                    ║")
        print("║  4 - Mostrar cursos                         ║")
        print("║  5 - Inscribir estudiante en curso          ║")
        print("║  6 - Dar de baja estudiante de curso        ║")
        print("╚══════════════════════════════════════════════╝")

    def __pedirMatricula(self):
        """Método auxiliar: pide y valida la matrícula, retorna str."""
        matriculaTexto = input("  Matrícula: ").strip()
        if not matriculaTexto.isdigit():
            raise ValueError("La matrícula debe ser un número entero positivo.")
        if int(matriculaTexto) <= 0:
            raise ValueError("La matrícula no puede ser negativa ni cero.")
        return matriculaTexto  # ← str, compatible con Estudiante.getMatricula()

    def ejecutar(self):

        while True:

            self.mostrarMenu()
            opcion = input("\n  Seleccione una opción: ").strip()

            try:

                if opcion == "0":
                    print("\n  Cerrando sistema...")
                    break

                elif opcion == "1":
                    nombre    = input("  Nombre: ").strip()
                    apellido  = input("  Apellido: ").strip()
                    matricula = self.__pedirMatricula()  # ← str
                    carrera   = input("  Carrera: ").strip()

                    estudiante = Estudiante(nombre, apellido, matricula, carrera)
                    self.__facultad.agregarEstudiante(estudiante)

                elif opcion == "2":
                    nombre   = input("  Nombre del curso: ").strip()
                    codigo   = input("  Código del curso: ").strip()
                    profesor = input("  Profesor: ").strip()

                    capacidadTexto = input("  Capacidad máxima: ").strip()
                    if not capacidadTexto.isdigit():
                        raise ValueError("La capacidad debe ser un número entero.")
                    capacidad = int(capacidadTexto)
                    if capacidad <= 0:
                        raise ValueError("La capacidad debe ser mayor a cero.")

                    curso = Curso(nombre, codigo, profesor, capacidad)
                    self.__facultad.agregarCurso(curso)

                elif opcion == "3":
                    self.__facultad.mostrarEstudiantes()

                elif opcion == "4":
                    self.__facultad.mostrarCursos()

                elif opcion == "5":
                    matricula = self.__pedirMatricula()  # ← str, mismo tipo que en Estudiante
                    codigo    = input("  Código del curso: ").strip()
                    self.__facultad.inscribirEstudiante(matricula, codigo)

                elif opcion == "6":
                    matricula = self.__pedirMatricula()  # ← str, mismo tipo que en Estudiante
                    codigo    = input("  Código del curso: ").strip()
                    self.__facultad.darDeBajaEstudiante(matricula, codigo)

                else:
                    print("\n  Opción inválida.")

            except ValueError as error:
                print(f"\n  [ERROR DE VALIDACIÓN]\n  {error}")

            except LookupError as error:
                print(f"\n  [ERROR DE BÚSQUEDA]\n  {error}")

            except RuntimeError as error:
                print(f"\n  [ERROR DE OPERACIÓN]\n  {error}")

            except Exception as error:
                print(f"\n  [ERROR GENERAL]\n  {error}")


sistema = SistemaFacultad()
sistema.ejecutar()