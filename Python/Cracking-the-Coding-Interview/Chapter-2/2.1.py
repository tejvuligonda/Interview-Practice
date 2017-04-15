import LinkedList

def removeWithBuf(head):
    if (head == None):
        return head
    dups = set({head.data})
    prev = head
    it = head.next_node
    while (it != None):
        if (it.data in dups):
            toDelete = it
            prev.next_node = toDelete.next_node            
            it = it.next_node
        else:
            dups.add(it.data)
            prev = prev.next_node
            it = it.next_node
    return head

if __name__ == '__main__':
    LL = LinkedList.Node(1)
    LL.appendToTail(1)
    LL.appendToTail(1)
    LL.appendToTail(1)
    LL.appendToTail(1)
    LL.appendToTail(1)
    print(LL)
    print(removeWithBuf(LL))
    LL1 = LinkedList.Node(2)
    LL1.appendToTail(3)
    LL1.appendToTail(2)
    LL1.appendToTail(2)
    print(LL1)
    print(removeWithBuf(LL1))
