import questionary
import Pet_Virtual
import os
import time
from config import carregar_jogo, salvar_jogo
os.system("color 1a")  # Muda a cor do terminal para verde  
print("Iniciando o sistema Vitual Pet... \n")
dados_salvos = carregar_jogo()
pet = None

if dados_salvos:
    print(f"\nEncontramos um pet salvo: {dados_salvos['nome']}")
    opcao_save = input("Deseja carregar o jogo salvo? (1 - Sim / 2 - Não, criar novo): ").strip()
    if opcao_save == "1":
        os.system("cls")
        pet = Pet_Virtual.Pet(
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
    pet = Pet_Virtual.Pet(nome_x)
    salvar_jogo(pet)
    os.system("cls")
while pet.vivo:
    os.system("color 0a")
    pet.status()
    print("\nO que deseja fazer?")
    
    escolha = questionary.select("Escolha uma ação:", choices=[
        "1 - Alimentar",
        "2 - Brincar",
        "3 - Colocar para dormir",
        "4 - Esperar um pouco",
        "5 - Sair (Salvar e fechar)"
    ]).ask()
    
    match escolha:
        case "1 - Alimentar":
            pet.alimenta()
        case "2 - Brincar":
            pet.brincar()
        case "3 - Colocar para dormir":
            pet.dormir()
        case "4 - Esperar um pouco":
            print(f"\nVocê não fez nada e o {pet.nome} ficou te olhando...")
        case "5 - Sair (Salvar e fechar)":
            salvar_jogo(pet)
            print("Jogo salvo! Até a próxima.")
            break
        case None: # <-- AQUI ESTÁ A CORREÇÃO
            print("\n Saída forçada pelo usuário. Salvando e saindo...")
            salvar_jogo(pet)
            break
            
    pet.passar_tempo()
    salvar_jogo(pet) 
    time.sleep(4)
    os.system("cls")