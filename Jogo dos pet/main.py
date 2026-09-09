import time
import os
import json
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
                        " devorou todos os dados da lixeira"]
        aletorio_frases=random.choice(frase_alimento)
        print(f"\n🍖 {self.nome} {aletorio_frases} ")

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
        print(f"\n {self.nome} capotou de sono em uma das memórias RAM")

    def passar_tempo(self):
        self.fome = min(100, self.fome + 5)
        self.energia = max(0, self.energia - 3)
        self.felicidade = max(0, self.felicidade - 4)
        if self.fome >= 100 or self.energia <= 0 or self.felicidade <= 0:
            self.vivo = False

    def status(self):
        humor = "😀" if self.felicidade > 60 else "😐" if self.felicidade > 25 else "😢"
        print("\n" + "="*25)
        print(f" {self.nome.upper()} {humor}")
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

def salvar_jogo(pet):
    """Salva os dados do pet em um arquivo JSON"""
    with open("pet_save.json", "w", encoding="utf-8") as arquivo:
        json.dump(pet.to_dict(), arquivo, ensure_ascii=False, indent=4)
    print("\n💾 [Progresso salvo com sucesso!]")

def carregar_jogo():
    """Carrega os dados do pet se o arquivo existir"""
    if os.path.exists("pet_save.json"):
        with open("pet_save.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados
    return None

def main():
    print("Bem-vindo ao pet virtual, versão com salvamento!")
    
    dados_salvos = carregar_jogo()
    pet = None

    if dados_salvos:
        print(f"\nEncontramos um pet salvo: {dados_salvos['nome']}")
        opcao_save = input("Deseja carregar o jogo salvo? (1 - Sim / 2 - Não, criar novo): ").strip()
        if opcao_save == "1":
            os.system("cls")
            pet = Pet(
                nome=dados_salvos["nome"],
                fome=dados_salvos["fome"],
                energia=dados_salvos["energia"],
                felicidade=dados_salvos["felicidade"],
                vivo=dados_salvos["vivo"]
            )
            if not pet.vivo:
                print(f"\nAviso: O {pet.nome} já estava morto no último salvamento...")

    if not pet:
        nome_x = input("Qual vai ser o nome do seu novo pet? ").strip()
        pet = Pet(nome_x)
        salvar_jogo(pet)
        os.system("cls")
    
    while pet.vivo:
        pet.status()
        print("\nO que deseja fazer?")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Colocar para dormir")
        print("4 - Esperar um pouco")
        print("5 - Sair (Salvar e fechar)")
        
        escolha = input("Qual é a sua escolha? ").strip()
        
        if escolha == "1":
            pet.alimenta()
        elif escolha == "2":
            pet.brincar()
        elif escolha == "3":
            pet.dormir()
        elif escolha == "4":
            print(f"\nVocê não fez nada e o {pet.nome} ficou te olhando...")
        elif escolha == "5":
            salvar_jogo(pet)
            print("Jogo salvo! Até a próxima.")
            break
        else:
            os.system("cls")
            print("Escolha uma opção válida! O pet só sabe contar até 5. ")
            continue
            
        pet.passar_tempo()
        salvar_jogo(pet) 
        time.sleep(4)
        os.system("cls")
        
    if not pet.vivo:
        pet.status()
        print(f"\n{pet.nome} morreu e o antivírus sumiu com o corpo...")
        if os.path.exists("pet_save.json"):
            os.remove("pet_save.json")

if __name__ == "__main__":
    main()