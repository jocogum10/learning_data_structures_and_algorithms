class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class LinkedList:
    def __init__(self, first_node=None):
        self.first_node = first_node
        
    def read(self, index):
        current_node = self.first_node              # begin at the first node
        current_index = 0                           # begin at the first index
        while(current_index <= index):              # check if current index is equal to index
            print(current_node.data)                # return the data of the current node
            current_node = current_node.next_node   # go to the next node
            current_index += 1
    
    def index_of(self, value):                      
        current_node = self.first_node              # begin at the first node
        current_index = 0                           # begin at the first index
        while True:
            if current_node.data == value:          # check if the value looking for is the current node data
                print(current_index)
                break
            current_node = current_node.next_node   # go to the next node
            current_index += 1
            
    def insert_at_index(self, index, value):
        new_node = Node(value)
        
        if index == 0:
            new_node.next_node = first_node         # if inserting on the first node, point the next_node of new_node to the first node
            self.first_node = new_node              # and then set the new_node to be the first node of the linked list
        else:
            current_node = first_node
            current_index = 0
            while current_index < (index-1):        # find the index immediately before the index of where we insert the new node
                current_node = current_node.next_node
                current_index += 1
            
            new_node.next_node = currrent_node.next_node    # set the new node's next node to the current node's next node
            current_node.next_node = new_node       # set the current node's next node to be the new node
    
    def delete_at_index(self, index):
        if index == 0:
            self.first_node = first_node.next_node  # set the first node to be the first node's next node
        else:
            current_node = first_node               # find the index immediately before the index where we want to delete
            current_index = 0
            while current_index < (index-1):
                current_node = current_node.next_node
                current_index += 1
            node_after_deleted_node = current_node.next_node._next_node # get the node after the node where we want delete
            current_node.next_node = node_after_deleted_node
            

            

if __name__ == '__main__':
    node_1 = Node("once")
    node_2 = Node("upon")
    node_1.next_node = node_2
    node_3 = Node("a")
    node_2.next_node = node_3
    node_4 = Node("time")
    node_3.next_node = node_4

    list = LinkedList(node_1)

    list.read(3)
    list.index_of('a')