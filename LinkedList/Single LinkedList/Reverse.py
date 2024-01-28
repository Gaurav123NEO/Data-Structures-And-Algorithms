from Insert import LinkedList

def Reverse(head):
    prev = None
    current = head
    while(current):
        NewNode = current.next
        current.next = prev
        prev = current
        current = NewNode
    head = prev
    return head

if __name__ == '__main__':
    llist =  LinkedList()
    llist.Insert(11)
    llist.Insert(12)
    llist.Insert(13)
    llist.Insert(14)
    head = llist.Retrive()
    print("Before reversal:")
    llist.Display(head)
    print("\nAfter reversal:")
    llist.Display(Reverse(head))
