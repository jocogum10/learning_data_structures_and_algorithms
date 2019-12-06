class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
        
    def insert_at_end(self, value):
        new_node = Node(value)
        
        if not self.first_node:                          # if there are no elements yet in the linked list
            self.first_node = new_node
            self.last_node = new_node
        else:                                       
            new_node.previous_node = self.last_node # else, set the new node's previous node as the last node
            self.last_node.next_node = new_node     # set the last node's next node to the new node
            self.last_node = new_node               # set the last node as the new node
            
    def remove_from_front(self):
        removed_node = self.first_node              # set the node to be removed
        self.first_node = self.first_node.next_node # set the first node to be the next node
        return removed_node                         # return the removed node
        
        
class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()
    
    def enque(self, value):
        self.queue.insert_at_end(value)
        
    def deque(self):
        removed_node = self.queue.remove_from_front
        return removed_node
        
    def tail(self):
        return self.queue.last_node.data
 
if __name__ == '__main__':
    node_1 = Node("once")
    node_2 = Node("upon")
    node_1.next_node = node_2
    node_3 = Node("a")
    node_2.next_node = node_3
    node_4 = Node("time")
    node_3.next_node = node_4
    
    dlist = DoublyLinkedList(node_1)
    print(dlist.remove_from_front().data)
    
    q = Queue()
    q.enque(dlist)
    b = q.tail()
    print(b.first_node.data)