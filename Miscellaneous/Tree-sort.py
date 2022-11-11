from random import

class Node():
    def __init__(self, digit):
        self.digit = digit
        self.left = None
        self.right = None
        self.perent = None

def insert_in_tree(root, unit):
    if root is None:
        root = unit
    else:
        if root.digit > unit.digit:
            if root.left is None:
                root.left = unit
            else:
                insert_in_tree(root.left, unit)
        elif root.digit < unit.digit:
            if root.right is None:
                root.right = unit
            else:
                insert_in_tree(root.right, unit)
                
def sort_max(root):
    if root != None:
        sort_max(root.right)
        print(root.digit)
        sort_max(root.left)

tree = Node(r)

sort_max(tree)