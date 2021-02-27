#Search for anode  to remove if the node is found. delete the node

class TreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
    
def minValueNode(node):
    current = node

    #loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
    return current

#Given a binary search tree and a key, this function
#delete the data and returns the new host

def deleteNode(root, data):
    #Base case
    if root is None:
        return root
    
    #If the key to be deleted
    #is smaller than the root's
    #key then it lies in left subtree

    if data < root.data:
        root.left = deleteNode(root.left,data)

    #if the Kye to be delete
    #is greater than the root data
    #then it lies in the right subtree
    elif(data > root.data):
        root.right = deleteNode(root.right, data)
    
    #if key is same as root's key, then this is the node
    # to be deleted
    else:

        #Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # node with two children:
        #get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        #Copy the inorder successor's
        #content to this node
        root.data = temp.data

        #Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)
    
    return root


def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)
print("Original node:")
print(preOrder(root))
root = deleteNode(root, 5)
print("After deleting specified node:")
print(preOrder(root))

