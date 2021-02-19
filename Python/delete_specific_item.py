#Delete a specific item from a given doubly linked list

class Node(object):
    #Single linked node
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, value):
        #Append an item
        new_item =  Node(value, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count +=1

    def iter(self):
        #Iterate the list
        current = self.head
        
            