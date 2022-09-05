# A linked list is a data structure made of a chain of node objects. Each node contains a value and a pointer to the next node in the chain.
# Linked lists are preferred over arrays due to their dynamic size (for the arrays and lists, more memories have to be created and relocated if more items are appended)
# and ease of insertion and deletion properties.

# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# A signly linked list class


class LinkedList:
    def __init__(self):
        self.head = None  # initialize linked list with a head address of None

    # insert at beginning, will first create a Node instance,
    # pass current head to its next attribute, and then update the current head to it (same applies to the empty linked list)
    def insert_at_beginning(self, value):
        newNode = Node(value, self.head)
        self.head = newNode

    # print method will print "your linked list is empty" for the empty linked list
    # if the linked list is not empty, use a iterator to iterate the linked list to the last element, concatenate them all to the string variable
    def print(self):
        if self.head is None:
            print('your linked list is empty')
            return
        else:
            iter = self.head
            str1 = ''
            while iter:
                str1 += str(iter.data) + '-->'
                iter = iter.next
            print(str1)

    # insert at end, will apply the same method for the insert_at_beginning method if the linked list is empty
    # if the linked list is not empty, use a iterator to iterate the linked list to the last element, and then set its next atttribute to the newNode
    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        else:
            iter = self.head
            while iter.next:
                iter = iter.next
            newNode = Node(value, None)
            iter.next = newNode

    # insert_values method will accept a list argument, and will return a new linked list
    def insert_values(self, values):
        self.head = None
        for value in values:
            self.insert_at_end(value)

    # len method will return the length of the linked list
    def len(self):
        if self.head is None:
            return 0
        else:
            count = 0
            iter = self.head
            while iter:
                count += 1
                iter = iter.next
            return count

    # remove-at method will remove the node at given index
    def remove_at(self, index):
        if index < 0 or index >= self.len():
            raise Exception('out of index error')
        else:
            if index == 0:
                self.head = self.head.next
                return
            else:
                count = 0
                iter = self.head
                while iter:
                    if count == index - 1:
                        iter.next = iter.next.next
                        break
                    iter = iter.next
                    count += 1

    # remove-at method will remove the node at given index
    def insert_at(self, index, value):
        if index < 0 or index > self.len():
            raise Exception('out of index errr')
        elif index == 0:
            self.insert_at_beginning(value)
        elif index == self.len():
            self.insert_at_end(value)
        else:
            count = 0
            iter = self.head
            while iter:
                if count == index - 1:
                    iter.next = Node(value, iter.next)
                    break
                iter = iter.next
                count += 1


ll = LinkedList()
# ll.insert_at_beginning(88)
# ll.insert_at_beginning(90)
# ll.insert_at_beginning(98)
# ll.insert_at_end(80)
# ll.insert_at_end(78)
ll.insert_values([0, 1, 2, 3, 4, 5, 6])
# ll.remove_at(0)
ll.insert_at(3, 7)
ll.print()
