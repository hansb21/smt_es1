from random import choice
from entidade import Entidade
class Fusao:
    def __init__(self):
        pass


    demons = ['Will O Wisp', 'Preta', 'Zhen', 'Erthys', "Shiisaa", 'Take-Minakata', 'Ame-no-Uzume', 'Inugami', 'Shikigami', 'Angel', 'Karasu Tengu' 'Mara', 'Beelzebub', 'Mada', 'Hresvelgr', 'Yatagarasu', 'Vishnu', 'Shiva', 'Cu Chulainn', 'Metatron', 'Genesha']

    # demons[i][0] = tipo
    #demons[i][1] = Ataques
    #demons[2-6] = maxHp, maxMp, atk, deF, luk,
    defdemons = {
                    str(demons[0]) : ["Escuro", ["Mudom", "Hama", "Zan", "Mordida"], 200, 120, 55, 34, 21],
                    str(demons[1]) : ["Escuro", ["Mudom", "Mudoon", "Hamaon", "Zio"], 215, 90, 43, 65, 38],
                    str(demons[2]) : ["Raio", ["Zio", "Agi", "Hama", "Zionga"], 170, 140, 45, 77, 38],
                    str(demons[3]) : ["Vento", ["Agi", "Agilao", "Zan", "Zanma"], 195, 190, 60, 35, 26],
                    str(demons[4]) : ["Luz", ["Mudom", "Hama", "Hamabarion", "Zan"], 250, 120, 70, 50, 44],
                    str(demons[5]) : ["Fogo", ["Agilao", "Bufu", "Agidyne", "Hama"], 215, 90, 43, 65, 38],
                    str(demons[6]) : ["Raio", ["Zio", "Agi", "Mudom", "Ziobarion"], 170, 140, 80, 77, 38],
                    str(demons[7]) : ["Vento", ["Agi", "Hama", "Zan", "Zanma"], 195, 160, 60, 55, 26],
                    str(demons[8]) : ["Gelo", ["Bufu", "Hama", "Bufula", "Mordida"], 170, 130, 35, 54, 34],
                    str(demons[9]) : ["Escuro", ["Mudobarion", "Mudoon", "Hamaon", "Zionga"], 215, 110, 84, 70, 38],
                    str(demons[10]) : ["Raio", ["Zio", "Espingarda", "Hama", "Zionga"], 160, 80, 41, 33, 26],
                    str(demons[11]) : ["Fogo", ["Agi", "Agilao", "Corte", "Espingarda"], 195, 190, 60, 45, 40],
                    str(demons[12]) : ["Gelo", ["Bufubarion", "Hamabarion", "Hama", "Mudo"], 250, 140, 75, 64, 41],
                    str(demons[13]) : ["Luz", ["Hamabarion", "Mudoon", "Hamaon", "Ziodyne"], 215, 120, 65, 68, 39],
                    str(demons[14]) : ["Raio", ["Ziobarion", "Agibarion", "Hama", "Zionga"], 200, 180, 78, 42, 38],
                    str(demons[15]) : ["Vento", ["Hamaon", "Agilao", "Zanbaryon", "Zanma"], 195, 190, 78, 56, 32],
                    str(demons[16]) : ["Gelo", ["Bufula", "Hama", "Bufudyne", "Mordida"], 200, 130, 60, 44, 25],
                    str(demons[17]) : ["Escuro", ["Mudom", "Mudoon", "Hamaon", "Zio"], 215, 90, 43, 65, 38],
                    str(demons[18]) : ["Luz", ["Hamabarion", "Hamaon", "Mudobarion", "Mudoon"], 180, 146, 47, 77, 38],
                    str(demons[19]) : ["Fogo", ["Agi", "Agibarion", "Zan", "Mudoon"], 215, 190, 54, 37, 22],
}
    def createFusions(self) -> dict:
        fusoes = {}

        for i in self.defdemons.keys():
            for j in self.defdemons.keys():
                if [i, j] not in fusoes.values():
                    fusao = choice(self.demons)
                    if fusao in fusoes.keys():
                        fusoes[fusao].append([i, j])
                    else:
                        fusoes[fusao] = [[i, j]]
        return fusoes

    def Fusao(self, fusoes: dict, demonio1: Entidade, demonio2: Entidade) -> Entidade:
        r_fusao = 0
        for i, j in fusoes.items():
            if i == [demonio1.name(), demonio2.name()]:
                r_fusao = j
        return r_fusao
