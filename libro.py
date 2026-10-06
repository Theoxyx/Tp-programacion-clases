class Libro:
    """Un libro de la biblioteca. Nace disponible y puede prestarse/devolverse."""

    def __init__(self, titulo, autor, isbn):
        # El guion bajo indica "atributo protegido": no se toca desde afuera.
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True  # todo libro nuevo está disponible

    # --- Propiedades de solo lectura (no tienen setter) ---
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def disponible(self):
        return self._disponible

    # --- Comportamiento ---
    def prestar(self):
        if not self._disponible:
            raise ValueError(f"El libro '{self._titulo}' ya está prestado")
        self._disponible = False

    def devolver(self):
        if self._disponible:
            raise ValueError(f"El libro '{self._titulo}' no estaba prestado")
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self._isbn}] {self._titulo} - {self._autor} ({estado})"
