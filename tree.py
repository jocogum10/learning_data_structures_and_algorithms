class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right
        
    def search(self, value, node):
        if node is None or node.value == value:         # base case
            return node
        elif value < node.value:
            return self.search(value, node.left_child)  # if value is lesser than the current node value, search the left child
        else:
            return self.search(value, node.right_child) # if value is greater than the current node value, search the right child
    
    def insert(self, value, node):
        if value < node.value:                          # if the left child does not exist, insert value
            if node.left_child is None:
                node.left_child = TreeNode(value)
            else:                                       # else, do another insert on the left child node
                insert(value, node.left_child)
        elif value > node.value:                        # if the right child does not exist, insert value
            if node.right_child is None:
                node.right_child = TreeNode(value)
            else:                                       # else, do another insert on the right child node
                insert(value, right_child)
    
    def delete(self, value_to_delete, node):
        if node is None:                                # base case
            return None
        elif value_to_delete < node.value:
            node.left_child = delete(value_to_delete, node.left_child)  # if value to delete is lesser than the node value, set the left_child to the result of the delete of the left child
            return node                                 # return the result of the recursive function call
        elif value_to_delete > node.value:
            node.right_child = delete(value_to_delete, node.right_child)
            return node
        elif value_to_delete == node.value:
            if node.left_child is None:                 # if current node has no left child, delete it by returning the right child
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                node.right_child = self.lift(node.right_child, node)
                return node
    
    def lift(self,node, node_to_delete):
        if node.left_child:                             # if current node has left child, call lift to continue down to find successor node
            node.left_child = lift(node.left_child, node_to_delete)
            return node
        else:                                           # if current node has no left child, then current node is the successor node
            node_to_delete.value = node.value
            return node.right_child
            
    def traverse_and_print(self, node):
        if node is None:
            return
        self.traverse_and_print(node.left_child)
        print(node.value)
        self.traverse_and_print(node.right_child)
            
            
if __name__ == '__main__':
    node = TreeNode(1)
    node2 = TreeNode(10)
    root = TreeNode(5, node, node2)
    
    print(root.value)
    print(root.left_child.value)
    print(root.right_child.value)
    print(root.search(10, root).value)
    
    
    n1 = TreeNode('Alice in Wonderland')
    n3 = TreeNode('Lord of Flies')
    n5 = TreeNode('Robinson Crusoe')
    n7 = TreeNode('The Odyssey')
    n2 = TreeNode('Great Expectations', n1, n3)
    n6 = TreeNode('Pride and Prejudice', n5, n7)
    n4 = TreeNode('Moby Dick', n2, n6)
    n4.traverse_and_print(n4)
    