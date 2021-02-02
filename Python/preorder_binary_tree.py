import sys
import math

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    
#Insert Node
    def insert(self, data):
        # If there's data == true
        if self.data:

            #if being sent is less than current data
            if data < self.data:
                
                #if current left node is empty
                if self.left is None:
                    #current left node equals data sent
                    self.left = Node(data)
                else:
                    #current left node calls insert
                    self.left.insert(data)

            #if data is greater than current data go right node
            elif data > self.data:
                #if current right node is empty
                if self.right is None:

                    #current right node equals data received
                    self.right = Node(data)
                else:
                    #current right node calls insert
                    self.right.insert(data)

        #There's no current node and this is the first.            
        else:
            self.data = data
            

#Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

#Recursive function to construct binary tree






#Inorder traversal
#left -> Root -> right
    def inorderTraversal(root):
        res=[]
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


#Preorder Traversal
#Root -> Left -> Right
def PreorderTraversal(root):
    if not root:
        return
    
    print("{}".format(root.data), end=" ")
    PreorderTraversal(root.left)
    PreorderTraversal(root.right)



def stringtotree(string_s):
  
    string = string_s.split(',')
    for x in range(len(string)-1):
        if x == 0:
            new_root = Node(int(string[x]))
        else:
            new_root.insert(int(string[x]))

    return new_root



def treeToString(root:Node , string:list):
    # base case
    if root is None or root is '':
        return
    
    # push the root data as character
    string.append(str(root.data))
    string.append(',')
    #if leaf node, then return node
    if not root.left and not root.right:
        return
    
    # for left subtree
    # string.append('(')
    treeToString(root.left, string)
    # string.append(')')

    #only if right child is present to
    #avoid extra parenthesis
    if root.right:
        # string.append('(')
        treeToString(root.right, string)
        # string.append(')')


def buildTreeUtil(nodes,start,end):
    #base case
    if start>end:
        return None
    
    #Get the middle element and make it root
    mid=(start+end)//2
    node=nodes[mid]
    
    #Using index in Inorder traversal, construct 
    #Left and right subtress
    node.left = buildTreeUtil(nodes, start, mid-1)
    node.right =  buildTreeUtil(nodes,mid+1, end)
    return node

#This function converts an unbalanced BST to a Balance BST
def buildTree(root):
    #store nodes of given BST insorted order
    nodes=[]
    storeBSTNodes(root,nodes)

    #constructs BST from nodes[]
    n=len(nodes)
    return buildTreeUtil(nodes,0,n-1)

#Recursive function to construct binary tree
def storeBSTNodes(root,nodes):
    #base case
    if not root:
        return
    
    #Stores nodes in Inorder ( which is sorted 
    # order for BST)
    storeBSTNodes(root.left,nodes)
    nodes.append(root)
    storeBSTNodes(root.right,nodes)


#



if __name__ == "__main__": 
    # root = Node(27)
    # root.insert(14)
    # root.insert(35)
    # root.insert(10)
    # root.insert(19)
    # root.insert(31)
    # root.insert(42)

    # string =[]
    # treeToString(root,string)
    # string_s=''.join(string)
    # #print(root.PrintTree())
    # # print(root.PreorderTraversal(root))
    # print(root.inorderTraversal(root))
    
    # new_tree = stringtotree(string_s)
    # #(new_tree.PrintTree())
    # print(new_tree.inorderTraversal(new_tree))

    root = Node(10)
    root.left = Node(8)
    root.left.left= Node(7)
    root.left.left.left =Node(6)
    root.left.left.left.left =  Node(5)
    root= buildTree(root)
    print("PrintOrder traveral of balance BST is :" )
    PreorderTraversal(root)


    



 