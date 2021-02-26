#count the numbers of Items of a given doublelinked list

class Node(object):
    #Singly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    class doubly_linked_list(object):
        def __init__(self):
                self.head = None
                self.tail = None
                self.count = 0

        def append_item(self,data):
            #Append an item
            new_item = Node(data, None, None)
            if self.head is None:
                self.head = new_item
                self.tail = self.head
            else:
                new_item.prev = self.tail
                self.tail.next =new_item
                self.tail= new_item
            
            self.count +=1
            
    
        