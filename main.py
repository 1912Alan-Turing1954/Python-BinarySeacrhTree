class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    
    
    def __init__(self):
        self.type = ''
        self.root = None
        
    def insert(self, data):
        newNode = Node(data)
        
        if self.root is None:
            self.root = newNode
        else:
            self.insertNode(self.root, newNode)
                
    def insertNode(self, node, newNode):
        if newNode.data < node.data:
            if node.left is None:
                node.left = newNode
            else:
                self.insertNode(node.left, newNode)
        else:
            if node.right is None:
                node.right = newNode
            else:
                self.insertNode(node.right, newNode)

    # def remove(self, node, key):
        
    def remove(self, node, key):
    
        # Base Case
        if node is None:
            return node
    
        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key < node.key:
            self.remove(node.left, key)
    
        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif key < node.key:
            self.remove(node.right, key)
    
        # If key is same as root's key, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
    
            elif node.right is None:
                temp = node.left
                node = None
                return temp
    
            
    
            # Copy the inorder successor's
            # content to this node
            node.key = temp.key
    
            # Delete the inorder successor
            self.remove(node.right, temp.key)
    
        return node

tree = BinaryTree()

tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.insert(29)
tree.insert(6)


tree.remove(left, 1)

    