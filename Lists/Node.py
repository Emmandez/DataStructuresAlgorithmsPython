class Node(object):

    #Constructor
    def __init__(self, value):
        self.value =  value
        #The pointer points to nothing until it has a new object
        self.nextNode = None
    

class linkedList(object):
    head = None
    tail = None
    size = 0

    def addToFront(self, nodeVal):
        node = nodeVal
        node.nextNode = self.head
        self.head = node
        self.size+=1


    
    def getSize(self):
        return self.size
    
    def printList(self):
        current = self.head
        print("HEAD-> ",end="")

        while(current!=None):
            #print(type(current.value.value))
            print(current.value,"-> ",end="")
            current = current.nextNode
        print("null")



    
