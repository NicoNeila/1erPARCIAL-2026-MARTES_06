class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel = self.nivel + 1
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", Tipo: " + self.tipo + ", Nivel: " + str(self.nivel)
    
    