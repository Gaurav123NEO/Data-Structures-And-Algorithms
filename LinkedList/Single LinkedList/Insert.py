
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Insert(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def Display(self, head):
        current = head
        while(current):
            print(current.data, end=" --> ")
            current = current.next
    
    def Retrive(self):
        return self.head



