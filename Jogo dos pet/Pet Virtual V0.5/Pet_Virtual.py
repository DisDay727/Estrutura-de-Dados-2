import random
class Pet:
    def __init__(self, nome, fome=50, energia=50, felicidade=50, vivo=True):
        self.nome = nome
        self.fome = fome
        self.energia = energia
        self.felicidade = felicidade
        self.vivo = vivo 

    def alimenta(self):
        self.fome = max(0, self.fome - 25)
        self.felicidade = min(100, self.felicidade + 5)
        frase_alimento=[" comeu dados não usados do seu computador",
                        " devorou todos os dados da lixeira"," comeu arquivos do seu sistema"," comeu dados do seu copia e colar","comeu cripto moedas do seu computador"]
        aletorio_frases=random.choice(frase_alimento)
        print(f"\n {self.nome} {aletorio_frases} ")

    def brincar(self):
        if self.energia >= 15:
            self.felicidade = min(100, self.felicidade + 20)
            self.energia = max(0, self.energia - 15)
            self.fome = min(100, self.fome + 10)
            print(f"\n {self.nome} adorou brincar com você! (ele escondeu arquivos no seu system32)")
        else:
            print(f"\n {self.nome} está cansado demais para brincar agora")

    def dormir(self):
        self.energia = min(100, self.energia + 40)
        self.fome = min(100, self.fome + 5)
        frase_dormir=[" dormiu profundamente"," dormiu na sua RAM"," dormiu debaixo do seu mouse"," dormiu no seu disco rígido"," dormiu no seu teclado"]
        aletorio_frases=random.choice(frase_dormir)
        print(f"\n {self.nome} 💤 {aletorio_frases}")

    def passar_tempo(self):
        self.fome = min(100, self.fome + 5)
        self.energia = max(0, self.energia - 3)
        self.felicidade = max(0, self.felicidade - 4)
        if self.fome >= 100 or self.energia <= 0 or self.felicidade <= 0:
            self.vivo = False

    def status(self):
        humor = "Feliz" if self.felicidade > 60 else "Neutro" if self.felicidade > 25 else "Triste"
        print("\n" + "="*25)
        print(f"          {self.nome.upper()} {humor}")
        print("="*25)
        print(f"Fome:      [{'|'*(10-self.fome//10):<10}] {100-self.fome}/100")
        print(f"Energia:   [{'|'*(self.energia//10):<10}] {self.energia}/100")
        print(f"Felicidade:[{'|'*(self.felicidade//10):<10}] {self.felicidade}/100")
        print("="*25)

    def to_dict(self):
        """Converte os dados do pet para um formato dicionário (salvar em JSON)"""
        return {
            "nome": self.nome,
            "fome": self.fome,
            "energia": self.energia,
            "felicidade": self.felicidade,
            "vivo": self.vivo
        }