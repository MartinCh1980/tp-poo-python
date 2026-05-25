class Libro:
    
    def __init__(self, titulo, autor, isbn):

        if not titulo.strip():
            raise ValueError("El título no puede estar vacío.")

        if not autor.strip():
            raise ValueError("El autor no puede estar vacío.")

        if not isbn.strip():
            raise ValueError("El ISBN no puede estar vacío.")

        self.__titulo = titulo.strip()
        self.__autor = autor.strip()
        self.__isbn = isbn.strip()

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
                f"El libro '{self.__titulo}' no está disponible. "
                f"Actualmente lo tiene: {self.__miembro_prestamo.getNombre()}."
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

        if self.__disponible:
            estado = "Disponible"
        else:
            estado = (
                f"Prestado a: "
                f"{self.__miembro_prestamo.getNombre()}"
            )

        return (
            f"Título: {self.__titulo} | "
            f"Autor: {self.__autor} | "
            f"ISBN: {self.__isbn} | "
            f"Estado: {estado}"
        )