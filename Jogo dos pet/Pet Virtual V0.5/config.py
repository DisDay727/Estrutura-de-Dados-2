 #salvamento do jogo em arquivo JSON
import json
import os

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