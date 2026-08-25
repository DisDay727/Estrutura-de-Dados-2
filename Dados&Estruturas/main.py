class Food:
  # Alimentos

  def __init__(self, nome, tipo, valor, unt):
    self.nome = nome # Nome
    self.tipo = tipo # tipo
    self.valor = valor # valor
    self.dul = 3  # Durabilidade / Pedaços restantes
    self.unt = unt  # Quantidade de itens no inventário

  def eat(self):
    # Verificase ainda há pedaços (dul) ou unidades (unt)
    if self.dul > 0 and self.unt > 0:
      self.dul -= 1  # Diminui um pedaço
      print(f"Você comeu um pedaço de {self.nome}! Sobraram {self.dul} pedaços.")

      # Se o alimento acabou os pedaços, gastamos uma unidade inteira do inventário
      if self.dul == 0 and self.unt > 1:
        self.unt -= 1
        self.dul = 3  # Reseta os pedaços para a próxima unidade
        print(f"Uma unidade inteira acabou. Restam {self.unt} unidades.")
      elif self.dul == 0 and self.unt == 1:
        self.unt -= 1
        print(f"O seu estoque de {self.nome} acabou completamente!")

    else:
      print(f"Não há mais {self.nome} para comer!")

# Testando o código dos alimentos:
wip = Food("banana", "comida", "3 gold", 2)

print(f"Item: {wip.nome} | Pedaços: {wip.dul} | Unidades: {wip.unt}")
print("-" * 40)

# Comendo algumas vezes
wip.eat()  
wip.eat()  
wip.eat()  

# Testando o código das armas de uma mão

class Ss1:
  # Armas de uma mão
  def __init__(self, nome, tipo, raridade, dano, dul, unt, valor):
    self.nome = nome
    self.tipo = tipo
    self.raridade = raridade
    self.dano = dano
    self.dul = dul
    self.unt = unt
    self.valor = valor
    self.equipado = False

  def usar(self):
    if self.unt > 0:
      self.equipado = True
      print(
          f"Você equipou a arma: {self.nome} (Dano: {self.dano}, Raridade:"
          f" {self.raridade})"
      )
    else:
      print(f"Você não tem unidades de {self.nome} para equipar!")

  def guarda(self):
    if self.equipado:
      self.equipado = False
      print(f"Você guardou (desequipou) a arma: {self.nome}")
    else:
      print(f"A arma {self.nome} já está guardada.")


# Testando a classe:
espada = Ss1(
    nome="Espada Curta",
    tipo="Espada",
    raridade="Comum",
    dano=15,
    dul=100,
    unt=1,
    valor="50 gold",
)

# Ações
espada.usar()  # Saída: Você equipou a arma: Espada Curta...
print("Está equipado" )  

espada.guarda()  # Saída: Você guardou...
print("Está desequipado")

#Inventario

class Itens_inventario:
  def __init__(self,nome,tipo,unidades):
    self.nome=nome
    self.tipo=tipo
    self.unidades=unidades
class Inventario:
  def __init__(self) :
    self.itens=[] # Aqui recebemos uma array






class ItemInventario:
  def __init__(self, nome, tipo, quantidade):
    self.nome = nome
    self.tipo = tipo
    self.quantidade = quantidade

class Inventario:
  def __init__(self):
    # A lista que vai guardar todos os itens dentro do inventário
    self.itens = []

  def adicionar_item(self, item):
    # Adiciona um item à lista
    self.itens.append(item)
    print(f"[Inventário] {item.quantidade}x {item.nome} foi adicionado!")

  def mostrar_inventario(self):
    print("\n========= SEU INVENTÁRIO =========")
    if not self.itens:
      print("O inventário está vazio.")
    else:
      for i, item in enumerate(self.itens, start=1):
        print(f"{i}. {item.nome} ({item.tipo}) - Quantidade: {item.quantidade}")
    print("==================================")


# --- Testando o sistema ---

# 1. Criamos o inventário do jogador
mochila = Inventario()

# 2. Criamos alguns itens (podem ser baseados nas suas classes de Food ou Ss1)
item1 = ItemInventario("Banana", "Comida", 2)
item2 = ItemInventario("Espada Curta", "Arma", 1)

# 3. Adicionamos os itens ao inventário
mochila.adicionar_item(item1)
mochila.adicionar_item(item2)

# 4. Mostramos a mochila na tela
mochila.mostrar_inventario()