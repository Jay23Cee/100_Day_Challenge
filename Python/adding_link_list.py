#Python program to add two numbers represented by linked list

#Node

class Node:
        #Constructor to initialize the node object
        def __init__(self, data):
            self.data = data
            self.next=None

class LinkedList:
    #function to initilize the head
    def __init__(self):
        self.head = None
    
    #Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Add contents of two linked lists and return the head
    #node of resultant list
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        #While both list exists
        while (first is not None or second is not None):
            


        