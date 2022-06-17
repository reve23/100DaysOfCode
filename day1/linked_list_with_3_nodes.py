#a simple python program to intorduce a linked list 

#Node class 
class Node:
    #function to initialize the node object
    def __init__(self,data):
        self.data = data #assign the data
        self.next = None # initialize the next as null value

#LinkedList class contains a Node object
class LinkedList:

    #function to initialize head of linked list
    def __init__(self):
        self.head = None

#code execeution starts here
if __name__ == '__main__':
    #start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
            Three nodes have been created. We have references to these three blocks as head, second and third

            llist.head            second              third
                |                    |                  |
                |                    |                  |
            +----+------+       +----+------+      +----+------+
            | 1  | None |       | 2  | None |      | 3  | None |
            +----+------+       +----+------+      +----+------+
    '''
    llist.head.next = second; #link first node with second

    '''
            Now next of first Node refers to second. So they both are linked

            llist.head            second              third
                |                    |                  |
                |                    |                  |
            +----+------+       +----+------+      +----+------+
            | 1  | o----------->|| 2  | null |     | 3  | null |
            +----+------+       +----+------+      +----+------+
    '''

    second.next = third # link second node to  third node

    '''
            Now next of second Node refers to third. so all three nodes are linked
             llist.head            second              third
                 |                   |                  |
                 |                   |                  |
            +----+------+       +----+------+      +----+------+
            | 1  | o----------->|| 2  | o-------->|| 3  | null |
            +----+------+       +----+------+      +----+------+
    '''
