#Python program to rotate a linked list

#Node Class
class Node:
    #Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #Function to initialize head
    def __init__(self):
        self.head = None

    #Function to insert a new node at the beginning
    def push(self, new_data):
        #allocate node and put the data
        new_node = Node(new_data)
        
        #Make next of new node as head
        new_node.next = self.head

        # move the head to point to the new Node
        self.head = new_node

    #Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data),
            temp = temp.next

    
    #This function rotates a linked list counter-clockwise 
    # and updates the head. the function assumes that K is smaller
    # than size of linked list. It doesn't modify the list if k is
    # greater than of equal to the size'
    
    def rotate(self, k):    
        if k == 0:
            return

        # let us understand the below code for example  k =4 
        #  list = 10 -> 20 -> 30 ->40 -> 50 -> 60
        current = self.head

        #current will either point to kth or Null after
        #this loop
        #current will point to node 40 in the above example
        count = 1
        while(count <k and current is not None):
            current = current.next
            count +=1

        #if current is None, k is greater than or equal 
        #to count of nodes in Linked list. Don't change 
        #the list in this case
        if current is None:
            return

        #current points to kth node. store it in a variable
        # kth node points to node 40 in the above example
        KthNode = current

        #current will point to the last node after this loop
     
        while(current.next is not None):
            current = current.next

        #change next of last node to previous head
   
        current.next = self.head

        #change head to (k +1)th node
        
        self.head = KthNode.next

        #CHANGE NEXT OF KTH NODE TO nULL
        KthNode.next = None


# Driver program to test above function
llist = LinkedList()

#Create a list 10->20->30->40->50->60
for i in range(60,0, -10):
    llist.push(i)

print ("given linked list")
llist.printList()
llist.rotate(4)

print("\nRotated Linked List")
llist.printList()


        
    
