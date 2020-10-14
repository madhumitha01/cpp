class LinkedList:
    """Defines a Singly Linked List.
    attributes: head
    """

    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insert(self, x, p):
        """Insert element x in the position after p"""
        temp = ListNode()
        temp.value = x
        temp.next = p.next
        p.next = temp

    def delete(self, p):
        """Delete the node following node p in the linked list."""
        p.next = p.next.next

    def show(self):
        """ Print all the elements of a list in a row."""
        i = self.head
        while i is not None:
            print(str(i.value))
            i = i.next

    def insertAtIndex(self, x, i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        m = self.head
        if m.next is None:
            z = ListNode()
            z.value = x
            m.next = z
        else:
            n = ListNode()
            t = ListNode()
            n.value = x
            t.next = self.head
            for d in range(i + 1):
                t = t.next
            n.next = t.next
            t.next = n

    def search(self, x):
        h = self.head
        while h.next:
            h = h.next
            if h.value == x:
                return h
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        i = self.head
        j = 0
        while i.next:
            j = j + 1
            i = i.next
        return j

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        i = self.head
        if i.next is None:
            return True
        else:
            return


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next.
    """

    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt


def main():
    L = LinkedList()
    L.insert(1, L.head)
    L.insert(2, L.head)
    L.insert(3, L.head)
    L.insert(4, L.head)
    L.insert(5, L.head)
    L.insert(7, L.head)
    print('List is: ')
    L.show()


if __name__ == '__main__':
    main()
