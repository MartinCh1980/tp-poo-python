from biblioteca import Biblioteca
from libro import Libro
from miembro import Miembro


class SistemaBiblioteca:

    def __init__(self):
        self.__biblioteca = Biblioteca()

   

    def validarISBN13(self, isbn):

        if not isbn.isdigit():
            raise ValueError("El ISBN debe contener solo números.")

        if len(isbn) != 13:
            raise ValueError("El ISBN debe tener exactamente 13 dígitos.")

        if not (isbn.startswith("978") or isbn.startswith("979")):
            raise ValueError("El ISBN debe comenzar con 978 o 979.")

        suma = 0

        for i in range(12):
            digito = int(isbn[i])

            if i % 2 == 0:
                suma += digito
            else:
                suma += digito * 3

        digito_control = (10 - (suma % 10)) % 10

        if digito_control != int(isbn[12]):
            raise ValueError("ISBN inválido (dígito de control incorrecto).")

        return isbn

    def validarDNI(self, dniTexto):

        if not dniTexto.isdigit():
            raise ValueError("El DNI debe contener solo números.")

        if len(dniTexto) not in (7, 8):
            raise ValueError("El DNI debe tener 7 u 8 dígitos.")

        return int(dniTexto)

    

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

            opcion = input("\n  Seleccione una opción: ").strip()

            try:

                if opcion == "0":
                    print("\n  Cerrando sistema...")
                    break

                
                elif opcion == "1":

                    titulo = input("  Título: ").strip()
                    autor = input("  Autor: ").strip()
                    isbn = input("  ISBN (13 dígitos): ").strip()

                    if titulo == "":
                        raise ValueError("El título no puede estar vacío.")

                    if autor == "":
                        raise ValueError("El autor no puede estar vacío.")

                    isbn = self.validarISBN13(isbn)

                    libro = Libro(titulo, autor, isbn)
                    self.__biblioteca.agregarLibro(libro)

                

                elif opcion == "2":

                    dniTexto = input("  DNI (7 u 8 dígitos): ").strip()
                    nombre = input("  Nombre: ").strip()

                    if nombre == "":
                        raise ValueError("El nombre no puede estar vacío.")

                    dni = self.validarDNI(dniTexto)

                    miembro = Miembro(dni, nombre)
                    self.__biblioteca.agregarMiembro(miembro)

                
                elif opcion == "3":
                    self.__biblioteca.mostrarLibros()

                
                elif opcion == "4":
                    self.__biblioteca.mostrarMiembros()

                
                elif opcion == "5":

                    isbn = input("  ISBN del libro: ").strip()
                    dniTexto = input("  DNI del miembro: ").strip()

                    isbn = self.validarISBN13(isbn)
                    dni = self.validarDNI(dniTexto)

                    self.__biblioteca.prestarLibro(isbn, dni)

                
                elif opcion == "6":

                    isbn = input("  ISBN del libro: ").strip()
                    dniTexto = input("  DNI del miembro: ").strip()

                    isbn = self.validarISBN13(isbn)
                    dni = self.validarDNI(dniTexto)

                    self.__biblioteca.devolverLibro(isbn, dni)

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


sistema = SistemaBiblioteca()
sistema.ejecutar()