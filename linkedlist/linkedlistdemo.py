## Function to crete a linked list
def create_linked_list(input_list):
    
    head = None
    tail = None
    
    for value in input_list:
        
        if head is None:
            head = Node(value)
            tail = head            
        else:
            tail.next = Node(value)
            tail = tail.next        # update the tail
            
    return head
