class Libro:

    def __init__(self, titulo, autor, isbn):

        titulo = str(titulo).strip()
        autor = str(autor).strip()
        isbn = str(isbn).strip()

        if not titulo:
            raise ValueError("El título no puede estar vacío.")

        if not autor:
            raise ValueError("El autor no puede estar vacío.")

        if not isbn:
            raise ValueError("El ISBN no puede estar vacío.")

        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

        self.__disponible = True
        self.__miembro_prestamo = None

    
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    def estaDisponible(self):
        return self.__disponible

    def getMiembroPrestamo(self):
        return self.__miembro_prestamo

    
    def prestar(self, miembro):

        if not self.__disponible:
            raise RuntimeError(
                f"El libro '{self.__titulo}' ya está prestado a "
                f"{self.__miembro_prestamo.getNombre()}."
            )

        self.__disponible = False
        self.__miembro_prestamo = miembro

    
    def devolver(self):

        if self.__disponible:
            raise RuntimeError(
                f"El libro '{self.__titulo}' no está prestado."
            )

        self.__disponible = True
        self.__miembro_prestamo = None

    
    def __str__(self):

        estado = (
            "Disponible"
            if self.__disponible
            else f"Prestado a: {self.__miembro_prestamo.getNombre()}"
        )

        return (
            f"Título: {self.__titulo} | "
            f"Autor: {self.__autor} | "
            f"ISBN: {self.__isbn} | "
            f"Estado: {estado}"
        )