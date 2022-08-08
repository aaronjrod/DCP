class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

        # Print the Tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(str(self.data)),
        if self.right:
            self.right.print_tree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res