class Biblioteca:
    
    def __init__(self):

        self.__libros = []
        self.__miembros = []

    # Altas 

    def agregarLibro(self, libro):

        for libroExistente in self.__libros:

            if libroExistente.getIsbn() == libro.getIsbn():
                raise ValueError(
                    f"Ya existe un libro con ISBN "
                    f"'{libro.getIsbn()}'."
                )

        self.__libros.append(libro)

        print(
            f"\n  Libro '{libro.getTitulo()}' "
            f"agregado correctamente."
        )

    def agregarMiembro(self, miembro):

        for miembroExistente in self.__miembros:

            if miembroExistente.getDni() == miembro.getDni():
                raise ValueError(
                    f"Ya existe un miembro con DNI "
                    f"'{miembro.getDni()}'."
                )

        self.__miembros.append(miembro)

        print(
            f"\n  Miembro '{miembro.getNombre()}' "
            f"agregado correctamente."
        )

    # Búsquedas 

    def buscarLibro(self, isbn):

        for libro in self.__libros:

            if libro.getIsbn() == isbn:
                return libro

        raise LookupError(
            f"No existe un libro con ISBN '{isbn}'."
        )

    def buscarMiembro(self, dni):

        for miembro in self.__miembros:

            if miembro.getDni() == dni:
                return miembro

        raise LookupError(
            f"No existe un miembro con DNI '{dni}'."
        )

    # Mostrar información 

    def mostrarLibros(self):

        if not self.__libros:
            print(
                "\n  No hay libros registrados."
            )
            return

        print("\n╔══════════════ LIBROS ══════════════╗")

        for libro in self.__libros:
            print(libro)

    def mostrarMiembros(self):

        if not self.__miembros:
            print(
                "\n  No hay miembros registrados."
            )
            return

        print("\n╔════════════ MIEMBROS ═════════════╗")

        for miembro in self.__miembros:

            libros = [
                libro.getTitulo()
                for libro in miembro.getLibrosPrestados()
            ]

            librosTexto = (
                ", ".join(libros)
                if libros
                else "Ninguno"
            )

            print(
                f"{miembro} | "
                f"Libros: {librosTexto}"
            )

    # Préstamos 

    def prestarLibro(self, isbn, dni):

        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        libro.prestar(miembro)
        miembro.agregarLibro(libro)

        print(
            f"\n  Préstamo realizado correctamente."
            f"\n  Libro: {libro.getTitulo()}"
            f"\n  Miembro: {miembro.getNombre()}"
        )

    # Devoluciones 

    def devolverLibro(self, isbn, dni):

        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro not in miembro.getLibrosPrestados():
            raise RuntimeError(
                f"El miembro '{miembro.getNombre()}' "
                f"no posee el libro "
                f"'{libro.getTitulo()}'."
            )

        libro.devolver()
        miembro.removerLibro(libro)

        print(
            f"\n  Devolución realizada correctamente."
            f"\n  Libro: {libro.getTitulo()}"
            f"\n  Miembro: {miembro.getNombre()}"
        )