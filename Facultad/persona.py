class Persona:
    
    def __init__(self, nombre, apellido):

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not apellido.strip():
            raise ValueError(
                "El apellido no puede estar vacío."
            )

        self._nombre = nombre.strip()
        self._apellido = apellido.strip()

    
    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido

    
    def __str__(self):

        return (
            f"{self._nombre} "
            f"{self._apellido}"
        )