class BTreeNode:
    def __init__(self):
        self.root = None
        self.t = 0
        self.keys = []
        self.children = []
        self.is_leaf = True
    def search(self, key):
        if self.root is None:
            return None
        return self._search(self.root,key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1


    def insert(self):
        pass

    def is_full(self):
        return len(self.keys) == (2*self.t -1)

class BTree:
    def __init__(self, t):
        self.t = t  # минимальная степень
        self.root = None  # начинаем с пустого дерева


