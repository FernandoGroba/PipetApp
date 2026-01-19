import datetime


class Mascota:
    def __init__(self, nombre, peso, especie, ultima_pipeta=None,       id_db=None):
        self.id = id_db
        self.nombre = nombre
        self.peso = peso
        self.especie = especie
        self.ultima_pipeta = ultima_pipeta

    def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Peso: {self.peso} | Especie: {self.especie} | Utima Pipeta: {self.ultima_pipeta}'

    def __lt__(self, otra):
        # Si a una le falta la fecha, la consideramos "menor" (más urgente)
        if not self.ultima_pipeta:
            return True
        if not otra.ultima_pipeta:
            return False
        return self.ultima_pipeta < otra.ultima_pipeta

    def calcular_proxima_pipeta(self):
        if self.ultima_pipeta:
            return self.ultima_pipeta + datetime.timedelta(days=21)
        return None
