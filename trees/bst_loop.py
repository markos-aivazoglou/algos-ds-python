class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def contains(self, value):
        curr = self
        while curr:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False

    def insert(self, value):
        curr = self
        while curr:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    return
                else:
                    curr = curr.left
            elif value >= curr.value:
                if curr.right is None:
                    curr.right = BST(value)
                    return
                else:
                    curr = curr.right

    def remove(self, value):
        curr = self
        parent = None
        while curr and curr.value != value:
            parent = curr
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
        # value not in BST
        if curr is None:
            return
        # leaf node
        if curr.left is None and curr.right is None:
            # 	root node
            if parent is None:
                return
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        elif curr.left and curr.right:
            successor, parent = curr.find_successor()
            # 	parent different than value to remove
            if parent:
                parent.left = successor.right
            # 	parent was the same as the successor
            # 	ie, successor was the immediate right value
            else:
                curr.right = successor.right
            curr.value = successor.value

        elif curr.left:
            curr.replace(curr.left)
        elif curr.right:
            curr.replace(curr.right)

    def find_successor(self):
        prev = None
        curr = self.right

        while curr.left:
            prev = curr
            curr = curr.left
        return curr, prev

    def replace(self, node):
        self.value = node.value
        self.left = node.left
        self.right = node.right

    def __str__(self):
        if self is None:
            return "Empty Tree"
        else:
            return f"{self.value} -> {self.left} -> {self.right}"


if __name__ == "__main__":
    bst = BST(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(5)
    bst.insert(13)
    bst.insert(22)
    bst.insert(1)
    bst.insert(14)
    bst.insert(12)
    # bst.insert(3)
    # bst.insert(4)
    # print(bst)
    # bst.insert(2)
    print(bst)
    bst.remove(5)
    # print(bst.contains(4))
    # print(bst.contains(5))
    # bst.remove(10)
    # bst.remove(1)
    # print(bst.contains(5))
    # print(bst.contains(10))
    # print(bst.contains(15))
    # bst.remove(10)
    print(bst)
