
from xml.dom.minidom import Element

class BinarySearchTreeNode:

    def __init__(self, data) -> None:

        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        
        #if the value already exists
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # add in the right subtree
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        element = []

        # visit left tree
        if self.left:
            element += self.left.in_order_traversal()
        
        # visit base node
        element.append(self.data)

        # visit right tree
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            #val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False


# Helper method
def build_tree(element):

    root = BinarySearchTreeNode(element[0])

    for i in range(1, len(element)):
        root.add_child(element[i])

    return root

if __name__ == "__main__":

    numbers = [17, 4, 1, 20 , 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(21))











