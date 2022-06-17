#Node class 
class Node:

    #functions to initialize the node object
    def __init__(self,data):
        self.data = data # assign the data
        self.next = None #Initialize the next as null

    #linked list class  
    class LinkedList:
        #fuction to initialize the linked list object
        def __init__(self):
            self.head = None 