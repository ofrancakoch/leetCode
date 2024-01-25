class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertElementAtStart(self, data):
        new_element = Node(data) 
        if self.head == None:
            self.head = new_element 
            return 
        else:
            new_element.next = self.head 
            self.head = new_element 
    
    def printAllElements(self):
        startElement = self.head 
        while(startElement): 
            print(startElement.data) 
            startElement = startElement.next 

    def insertElementAtEnd(self, data):
        element = Node(data)
        lastElement = self.head
        while lastElement:
            if lastElement.next == None:
                element.next = lastElement.next
                lastElement.next = element
                return 
            else:
                lastElement = lastElement.next

    def insertByIndex(self, data, index):
        element = Node(data)
        position = self.head
        counter = 0

        if counter == index:
            self.insertElementAtStart(data)

        while position:
            if counter == index - 1:
                element.next = position.next
                position.next = element
                return
            else:
                position = position.next
                counter += 1

    def countElements(self):
        counter = 0
        position = self.head
        while position:
            position = position.next
            counter += 1
                
        return counter
        
    def removeFirstOne(self):
        if self.head == None:
            return 
        
        self.head = self.head.next

    def removeLastOne(self):
        quantity = self.countElements()
        counter = 0
        element = self.head
        if element == None:
            return 
        while element:
            if counter == quantity - 2:
                element.next = None
                return 
            else:
                element = element.next
                counter += 1

    def removeByIndex(self, index):
        counter = 0
        element = self.head
        if element == None:
            return 
        while element:
            if counter == index - 1:
                element.next = element.next.next
                return 
            else:
                element = element.next
                counter += 1

lista = LinkedList()
lista.insertElementAtStart(9)
lista.insertElementAtStart(8)
lista.insertElementAtEnd(81)
lista.insertElementAtStart(26)
lista.insertElementAtEnd(76)
lista.insertByIndex(100000,1)
#lista.removeFirstOne()
#lista.removeLastOne()
#lista.removeByIndex(1)
lista.printAllElements()
print("\n")
print(lista.countElements())
