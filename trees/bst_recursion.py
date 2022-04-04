class BinarySearchTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        if value < self.value:
            self.left = (
                self.left.insert(value) if self.left else BinarySearchTree(value)
            )
        else:
            self.right = (
                self.right.insert(value) if self.right else BinarySearchTree(value)
            )
        return self

    def contains(self, value):
        return self.find(value) is not None

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            return self.left.find(value) if self.left else None
        elif value > self.value:
            return self.right.find(value) if self.right else None

    def remove(self, value):
        if value < self.value:
            self.left = self.left.remove(value) if self.left else None
        elif value > self.value:
            self.right = self.right.remove(value) if self.right else None
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                self.replace(self.left)
            elif self.left is None:
                self.replace(self.right)
            else:
                self.value = self.right.min()
                self.right = self.right.remove(self.value)
        return self

    def replace(self, node):
        self.value = node.value
        self.left = node.left
        self.right = node.right

    def min(self):
        return self.left.min() if self.left else self.value

    def __str__(self):
        if self is None:
            return "Empty Tree"
        else:
            return f"{self.value} -> {self.left} -> {self.right}"


if __name__ == "__main__":
    bst = BinarySearchTree(10)
    # bst.insert(2)
    # bst.insert(3)
    # bst.insert(4)
    # print(bst)
    # bst.remove(1)
    bst.insert(15)
    bst.insert(2)
    bst.insert(5)
    bst.insert(13)
    bst.insert(22)
    bst.insert(1)
    bst.insert(14)
    bst.insert(12)
    print(bst)
    # print(bst.contains(4))
    # print(bst.contains(5))
    # bst.remove(10)
    # bst.remove(1)
    # print(bst.contains(5))
    # print(bst.contains(10))
    # print(bst.contains(15))
    bst.remove(10)
    print(bst)
