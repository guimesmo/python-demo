import random

class Frase:
    def __init__(self, conjunto, idioma_padrao="pt"):
        self.conjunto = conjunto
        self.idioma_padrao = idioma_padrao
        self.output = dict()
        self.parse()
        
    def __str__(self):
        return self.output.get(self.idioma_padrao, "Não definido")

    def parse(self):
        conjunto = self.conjunto.split("\n")
        for frase in conjunto:
            if frase:  # previne linha em branco
                idioma, frase = frase.split("|")
                self.output[idioma] = frase
    
def gerador_de_frase_i18n(idioma="pt"):
    with open("frases-i18n.txt", "r") as arquivo:
        conjuntos = arquivo.read().split("\n\n")
    frases = []
    for conjunto in conjuntos:
        frase_instancia = Frase(conjunto)
        frases.append(frase_instancia)
    frase = random.choice(frases)
    return frase.output.get(idioma)


def gerador_de_frase():
    with open("frases.txt", "r") as arquivo:
        frases = list(arquivo.readlines())
    return random.choice(frases)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        idioma = sys.argv[1]
    else:
        idioma = "pt"
    print(gerador_de_frase_i18n(idioma))
