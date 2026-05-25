class Miembro:
    
    def __init__(self, dni, nombre):

        if not dni.strip():
            raise ValueError(
                "El DNI no puede estar vacío."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self.__dni = dni.strip()
        self.__nombre = nombre.strip()

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
                f"El libro '{libro.getTitulo()}' "
                f"ya fue agregado al miembro."
            )

        self.__libros_prestados.append(libro)

    def removerLibro(self, libro):

        if libro not in self.__libros_prestados:
            raise LookupError(
                f"El libro '{libro.getTitulo()}' "
                f"no figura entre los préstamos "
                f"de {self.__nombre}."
            )

        self.__libros_prestados.remove(libro)

    
    def __str__(self):

        cantidad = len(self.__libros_prestados)

        return (
            f"Nombre: {self.__nombre} | "
            f"DNI: {self.__dni} | "
            f"Libros prestados: {cantidad}"
        )