
class Tipo:
    def __init__(self, nome : str, fraqueza, resistencia, repelir, absorver):
        self.nome = nome
        self.fraqueza = fraqueza
        self.resistencia = resistencia
        self.repelir = repelir
        self.absorver = absorver

    def getNome(self):
        return self.nome
