class Miembro:

    def __init__(self, dni, nombre):

        nombre = str(nombre).strip()

        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        if isinstance(dni, bool) or not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero.")

        self.__dni = dni
        self.__nombre = nombre
        self.__libros_prestados = []

    
    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getLibrosPrestados(self):
        return self.__libros_prestados.copy()

   
    def agregarLibro(self, libro):

        if libro in self.__libros_prestados:
            raise RuntimeError(
                f"El libro '{libro.getTitulo()}' ya está asignado al miembro."
            )

        self.__libros_prestados.append(libro)

    def removerLibro(self, libro):

        if libro not in self.__libros_prestados:
            raise LookupError(
                f"El libro '{libro.getTitulo()}' no pertenece a {self.__nombre}."
            )

        self.__libros_prestados.remove(libro)

    
    def __str__(self):

        cantidad = len(self.__libros_prestados)

        return (
            f"Nombre: {self.__nombre} | "
            f"DNI: {self.__dni} | "
            f"Libros prestados: {cantidad}"
        )