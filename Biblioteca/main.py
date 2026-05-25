from biblioteca import Biblioteca
from libro import Libro
from miembro import Miembro


class SistemaBiblioteca:

    def __init__(self):

        self.__biblioteca = Biblioteca()

   
    def mostrarMenu(self):

        print("\n╔══════════════════════════════════════════╗")
        print("║      SISTEMA DE GESTIÓN BIBLIOTECA      ║")
        print("╠═════════════════════════════════════════╣")
        print("║  0 - Salir                              ║")
        print("║  1 - Agregar libro                      ║")
        print("║  2 - Agregar miembro                    ║")
        print("║  3 - Mostrar libros                     ║")
        print("║  4 - Mostrar miembros                   ║")
        print("║  5 - Prestar libro                      ║")
        print("║  6 - Devolver libro                     ║")
        print("╚══════════════════════════════════════════╝")

    
    def ejecutar(self):

        while True:

            self.mostrarMenu()

            opcion = input(
                "\n  Seleccione una opción: "
            ).strip()

            try:

                if opcion == "0":

                    print(
                        "\n  Cerrando sistema..."
                    )
                    break

                elif opcion == "1":

                    titulo = input(
                        "  Título: "
                    ).strip()

                    autor = input(
                        "  Autor: "
                    ).strip()

                    isbn = input(
                        "  ISBN: "
                    ).strip()

                    libro = Libro(
                        titulo,
                        autor,
                        isbn
                    )

                    self.__biblioteca.agregarLibro(
                        libro
                    )

                elif opcion == "2":

                    dni = input(
                        "  DNI: "
                    ).strip()

                    nombre = input(
                        "  Nombre: "
                    ).strip()

                    miembro = Miembro(
                        dni,
                        nombre
                    )

                    self.__biblioteca.agregarMiembro(
                        miembro
                    )

                elif opcion == "3":

                    self.__biblioteca.mostrarLibros()

                elif opcion == "4":

                    self.__biblioteca.mostrarMiembros()

                elif opcion == "5":

                    isbn = input(
                        "  ISBN del libro: "
                    ).strip()

                    dni = input(
                        "  DNI del miembro: "
                    ).strip()

                    self.__biblioteca.prestarLibro(
                        isbn,
                        dni
                    )

                elif opcion == "6":

                    isbn = input(
                        "  ISBN del libro: "
                    ).strip()

                    dni = input(
                        "  DNI del miembro: "
                    ).strip()

                    self.__biblioteca.devolverLibro(
                        isbn,
                        dni
                    )

                else:

                    print(
                        "\n  Opción inválida."
                    )

            except ValueError as error:

                print(
                    f"\n  [ERROR DE VALIDACIÓN]"
                    f"\n  {error}"
                )

            except LookupError as error:

                print(
                    f"\n  [ERROR DE BÚSQUEDA]"
                    f"\n  {error}"
                )

            except RuntimeError as error:

                print(
                    f"\n  [ERROR DE OPERACIÓN]"
                    f"\n  {error}"
                )

            except Exception as error:

                print(
                    f"\n  [ERROR GENERAL]"
                    f"\n  {error}"
                )


sistema = SistemaBiblioteca()
sistema.ejecutar()