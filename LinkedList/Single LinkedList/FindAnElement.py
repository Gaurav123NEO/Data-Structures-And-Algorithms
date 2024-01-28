from Insert import LinkedList

def Locate(head, element):
    while(head):
        if head.data != element:
            head = head.next
        else:
            return True
    return False        

if __name__ == '__main__':
    llist =  LinkedList()
    llist.Insert(11)
    llist.Insert(12)
    llist.Insert(13)
    llist.Insert(14)
    head = llist.Retrive()
    llist.Display(head)
    a = Locate(head,14)
    print(a)
