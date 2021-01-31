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


#Inorder traversal
#left -> Root -> right
    def inorderTraversal(self, root):
        res=[]
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


#Preorder Traversal
#Root -> Left -> Right
    def PreorderTraversal(self, root):
        res =[]
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res


def treeToString(root:Node , string:list):
    # base case
    if root is None:
        return
    
    # push the root data as character
    string.append(str(root.data))

    #if leaf node, then return node
    if not root.left and not root.right:
        return
    
    # for left subtree
    string.append('(')
    treeToString(root.left, string)
    string.append(')')

    #only if right child is present to
    #avoid extra parenthesis
    if root.right:
        string.append('(')
        treeToString(root.right, string)
        string.append(')')





if __name__ == "__main__": 
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    string =[]
    treeToString(root,string)
    print(''.join(string))
    print(root.inorderTraversal(root))
    print(root.PreorderTraversal(root))
        