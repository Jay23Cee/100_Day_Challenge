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
        while current:
            item_val = current.value
            current = current.next
            yield item_val
    
    def print_forward(self):
        for node in self.iter():
            print(node)

    def search_item(self,val):
        for node in self.iter():
            if val == node:
                return True
        return False
    
    def delete(self,value):
        #Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        
        elif current.value == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        else:
            while current:
                if current.value == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        
        if node_deleted:
            self.count -= 1

items = doubly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.append_item('JavaScript')
items.append_item('SQL')

print("Original List:")
items.print_forward()

items.delete("Java")
items.delete("Python")
print("\nList after deleting two items:")
items.print_forward()

        
            


            