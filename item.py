class Item:
    def __init__(self, nome: str, tipoItem: str, potencia: int, qtd: int):
        self.nome = nome
        self.tipoItem = tipoItem
        self.potencia = potencia
        self.qtd = qtd

    def getQtd() -> int:
        return self.qtd

    def diminuiQtd() -> None:
            self.qtd -= 1
