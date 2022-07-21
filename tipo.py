
class Tipo:
    def __init__(self, nome : str, fraqueza : str, resistencia : str, repelir : str, absorver : str):
        self.nome = nome
        self.fraqueza = fraqueza
        self.resistencia = resistencia
        self.repelir = repelir
        self.absorver = absorver

    def getNome(self):
        return self.nome

    def getFraqueza(self):
        return self.fraqueza

    def getResistencia(self):
        return self.resistencia
    
    def getRepelir(self):
        return self.repelir

    def getAbsorver(self):
        return self.absorver
