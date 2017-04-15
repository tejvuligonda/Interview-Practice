class Node():

    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def appendToTail(self,newData): 
        n = self;
        tail = Node(newData)
        while (n.next_node != None):
            n = n.next_node
        n.next_node = tail
    
    def __str__(self):
        if (self.next_node == None):
            return '|'+str(self.data)+'|//'
        else: 
            return '|'+str(self.data)+'|->'+str(self.next_node)


def deleteNode(head,val):
    iterator = head 
    print(iterator.data)
    if (head.data == val):
        print(iterator.data)
        head = head.next_node
        return head
    while (iterator.next_node.data != val and iterator.next_node != None):
        iterator = iterator.next_node
    if (iterator.next_node == None):
        return head
    iterator.next_node = iterator.next_node.next_node
    return head

if __name__ == '__main__':
    x = Node(7)
    x.appendToTail(8)
    x.appendToTail(9)
    x.appendToTail(10)
    print(x)
    x = deleteNode(x,8)
    print(x)
    x = deleteNode(x,10)
    print(x)
