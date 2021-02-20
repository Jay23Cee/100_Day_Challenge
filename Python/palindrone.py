#Check if linkedlistis a palindrome

#Node class
class Node:
    #constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #function to initialize head
    def __init__(self):
        self.head = None
    
    #A utility function to check if str is palindrome
    def isPalindromeUtil(self, string):
        return (string == string[::-1])

    #Returns true if string formed by linked list is
    #Palindrome
    def isPalindrome(self):
        node = self.head

        #Append all nodes to form a string
        temp = []
        while (node is not None):
            temp.append(node.data)
            node = node.next
        string = "".join(temp)
        return self.isPalindromeUtil(string)
    
    #Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next


#Driver program to test above function
llist = LinkedList()
llist.head = Node('a')
llist.head.next = Node('bc')
llist.head.next.next = Node("d")
llist.head.next.next.next = Node("dcb")
llist.head.next.next.next.next = Node("a")
print('True' if llist.isPalindrome() else "false")

    