# Classe que representa um nó da árvore
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Filho esquerdo
        self.right = None  # Filho direito

# Classe que representa a árvore binária
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserção dinâmica
    def insert(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Apenas números são permitidos.")
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Se for igual, não insere (evita duplicatas)
        return node

    # Busca dinâmica
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

    # Remoção dinâmica
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Caso 1: Nó sem filhos
            if node.left is None and node.right is None:
                return None
            # Caso 2: Um filho
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Caso 3: Dois filhos
            else:
                min_val = self._min_value(node.right)
                node.value = min_val
                node.right = self._delete_recursive(node.right, min_val)
        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node.value

    # Percurso em ordem (in-order)
    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right)


# ----------------- EXEMPLO DE USO -----------------
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Inserindo valores dinamicamente
    for num in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(num)

    print("Árvore em ordem:", bst.inorder())

    # Busca
    print("Buscar 40:", bst.search(40))
    print("Buscar 100:", bst.search(100))

    # Remoção
    bst.delete(30)
    print("Após remover 30:", bst.inorder())
