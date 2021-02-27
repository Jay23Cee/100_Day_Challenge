#Search for anode  to remove if the node is found. delete the node

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def delete_Node(root, key):
    #If root doesn't exist , just return it
    if not root:
        return root
    #Find the node in the left subtree if key value is less than root value
    if root.val > key:
        root.left = delete_Node(root.left, key)
    #Find the node in right subtree if key value is greater than root value,
    elif root.val < key:
        root.right = delete_Node(root.right, key)
    #Delete the node if root.value == key
    else:
        #If there is no right children delete the node and new root would be root.left
        if not root.right:
            return root.left
    #If there is no left children delete the node and new root would be root.right
        if not root.left:
            return root.right
    
    # If both left and right children exist in the node replace its value with
    # the minminum value in the right subtree. Now delete the minimum node 
    # in the right subtree
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val= temp_val.val
    
    #Delete the minimum node in right subtree
        root.right = delete_Node(root.right, root.val)
    
    return root


def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)




