class Socio:
    """Un socio de la biblioteca. Puede tener como máximo MAX_LIBROS libros a la vez."""

    # Constante de clase: el 3 vive acá, en un solo lugar, y no "suelto" en el código.
    MAX_LIBROS = 3

    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
        self._libros = []  # arranca vacía

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def libros(self):
        # Devolvemos una COPIA: si alguien hace socio.libros.append(...) desde afuera,
        # no se saltea las validaciones de agregar_libro().
        return list(self._libros)

    def puede_pedir(self):
        return len(self._libros) < self.MAX_LIBROS

    def agregar_libro(self, libro):
        if not self.puede_pedir():
            raise ValueError(
                f"{self._nombre} ya tiene el máximo de {self.MAX_LIBROS} libros"
            )
        self._libros.append(libro)

    def quitar_libro(self, libro):
        if libro not in self._libros:
            raise ValueError(f"{self._nombre} no tiene el libro '{libro.titulo}'")
        self._libros.remove(libro)

    def __str__(self):
        return f"{self._nombre} (DNI {self._dni}) - {len(self._libros)} libro(s) prestado(s)"
