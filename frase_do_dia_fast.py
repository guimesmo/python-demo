import random

class Frase:
    def __init__(self, conjunto, idioma_padrao="pt"):
        self.idioma_padrao = idioma_padrao
        self.output = dict()
        self.parse(conjunto)
        
    def __str__(self):
        return self.output.get(self.idioma_padrao, "Não definido")

    def parse(self, conjunto):
        for frase in [f for f conjunto.split("\n") if f]
            idioma, frase = frase.split("|")
            self.output[idioma] = frase
    
def gerador_de_frase_i18n(idioma="pt"):
    with open("frases-i18n.txt", "r") as arquivo:
        conjuntos = arquivo.read().split("\n\n")
    frases = [Frase(conjunto) for conjunto in conjuntos]
    return random.choice(frases).output.get(idioma)


def gerador_de_frase():
    with open("frases.txt", "r") as arquivo:
        frases = list(arquivo.readlines())
    return random.choice(frases)


if __name__ == '__main__':
    import sys
    idioma = "pt"
    if len(sys.argv) > 1:
        idioma = sys.argv[1]
    print(gerador_de_frase_i18n(idioma))
