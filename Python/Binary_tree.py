class Node:

    def __init__(self,data):
        self.left= None
        self.right= None
        self.data = data

    
    def insert(self,data):

# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

            #Return the unchanged nodepointer
        return data 
#findval method to compare the value with nodes

    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" is not Found"
            return self.left.findval(lkpval)
        elif lkpval >self.data:
            if self.right is None:
                return str(lkpval)+" is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data)+ " is found"

#A function to do inorder traversal of Binary Search Tree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print ( root.data),
        inorder(root.right)
    
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

    


# print the tree
def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print(self.data),
    if self.right:
        self.right.PrintTree()

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.insert(4)

print(root.findval(7))
print(root.findval(14))



print("\n delete")
root = deleteNode(root,31)
