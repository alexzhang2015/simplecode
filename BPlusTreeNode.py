class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def insert_key(self, key):
        self.keys.append(key)
        self.keys.sort()

    def insert_child(self, child):
        self.children.append(child)

    def split(self):
        half = len(self.keys) // 2
        new_node = BPlusTreeNode()

        new_node.keys = self.keys[half:]
        self.keys = self.keys[:half]

        if not self.is_leaf:
            new_node.children = self.children[half:]
            self.children = self.children[:half]

        return new_node


class BPlusTree:
    def __init__(self):
        self.root = BPlusTreeNode(is_leaf=True)

def insert(self, key):
    if key in self.search(key):
        return

    node = self.root
    if len(node.keys) == 3:
        new_node = BPlusTreeNode()
        self.root = new_node
        new_node.insert_child(node)
        new_node.insert_key(node.keys[1])
        new_node.children[0] = node.split()

        self.insert_non_full(new_node, key)
    else:
        self.insert_non_full(node, key)

    def insert_non_full(self, node, key):
        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1

        if node.is_leaf:
            node.insert_key(key)
        else:
            if len(node.children[index].keys) == 3:
                node.children.insert(index+1, node.children[index].split())
                node.insert_key(node.children[index].keys[1])

                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key)

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if key in node.keys:
            return node
        elif node.is_leaf:
            return None
        else:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            return self.search(key, node.children[index])


# 使用示例
tree = BPlusTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)

result = tree.search(10)
if result:
    print("找到了")
else:
    print("未找到")
