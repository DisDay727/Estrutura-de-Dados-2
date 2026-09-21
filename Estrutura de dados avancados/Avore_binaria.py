# Classe que representa um nó da árvore Avoré binaria  todo no se chamará Node isso é boas praticas assim como toda raiz se chamara de root.
class Node:
    def __init__(self, value):
        self.value = value      # Valor armazenado no nó
        self.left = None        # Filho à esquerda
        self.right = None       # Filho à direita

# Classe que representa a árvore binária
class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)  # Cria a raiz

    # Inserção simples (exemplo: árvore binária de busca)
    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            print(f"Valor {value} já existe na árvore.")

    # Percurso em ordem (in-order traversal)
    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right)

    # Busca de valor
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


# ===== Exemplo de uso =====
if __name__ == "__main__":
    tree = BinaryTree(10)  # Raiz com valor 10
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)

    print("Percurso em ordem:", tree.inorder())  # [3, 5, 7, 10, 15]
    print("Buscar 7:", tree.search(7))           # True
    print("Buscar 20:", tree.search(20))         # False
