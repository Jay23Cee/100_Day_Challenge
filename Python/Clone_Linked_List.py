# A Linked List node with a random pointer
class Node:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random  = random


#Recur#sive function to print a linked list
def traverse(head):

    #traverse the linked list
    while head:
        #print current node data and random pointer data
        if head.random:
            print(head.data , f"({head.random.data})", end=" -> ")
        else:
            print(head.data, "(X)", end=" -> ")
        
        #advance to the next node
        head = head.next

    print("null")

#Function to clone a linked list having random pointers
# Function to clone a linked list having random pointers
def cloneLinkedList(head):
 
    ## 1. Create a duplicate of each node of the original linked list
 
    # traverse the original linked list
    curr = head
    while curr:
        # take a pointer to the next node in the original list
        next = curr.next
 
        # duplicate each node of the linked list
        dup = Node(curr.data)
 
        # associate each duplicate node with the next child of the original node
        curr.next = dup
        dup.next = next
 
        # advance to the next node in the original list
        curr = next
 
    ## 2. Update the random pointers of the duplicated nodes
 
    # traverse the modified list
    curr = head
    while curr:
 
        # if a random pointer for the original node exists, set it for the clone
        if curr.random:
            curr.next.random = curr.random.next
 
        # advance to the next node in the original list
        curr = curr.next.next
 
    ## 3. Extract the duplicate nodes from the modified list
 
    # construct a dummy node whose next pointer points to the head
    # of the cloned linked list
    dummy = Node(-1)
 
    # maintain a tail node for the clone
    tail = dummy
 
    # traverse the modified list
    curr = head
    while curr:
        # take a pointer to the next node in the original list
        next = curr.next.next
 
        # extract the duplicate
        dup = curr.next
        tail.next = dup
        tail = dup
 
        # restore the original linked list
        curr.next = next
 
        # advance to the next node in the original list
        curr = next
 
    # return head node of the cloned list
    return dummy.next

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.random = head.next.next.next
    head.next.next.random = head.next

    print("Original linked list:")
    traverse(head)

    clone = cloneLinkedList(head)

    print("\nCloned linked list:")
    traverse(clone)

