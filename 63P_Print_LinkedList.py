# Print Linkedlist Using Line by Line

from decimal import localcontext


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    # Initialize a Linked List using self.head and self.tail to None value
    def __init__(self):
        self.head = None
        self.tail = None

    # Now to insert a value in Linked List in a already defined LL

    def __iter__(self):
        node = self.head
        while node:
            # yield in Python can be used like the return statement in a function. When done so, the function instead of returning the output, it returns a generator that can be iterated upon.
            yield node
            node = node.next

    def insertLinkedList(self, value, location):
        # first create Node with reqeusted value
        newNode = Node(value)
        # check if head exist or not, if not then assign the head and tail value to it
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        # now if head exists, then check the location provided to insert in linkedlist
        else:
            if location == 0:
                # if location is 0 means we have to assign head value to the requested value.
                newNode.next = self.head
                self.head = newNode
                # next, if locaton is last i.e. -1, here we have to initialize self.tail with value of newNode, since newNode will be the future tail. assign newNode.next as None to finish the LL with tail nature.
            elif location == -1:
                newNode.next = None
                self.tail = newNode
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = newNode

            else:
                # now to insert the linkedlist in middle, we have to traverse to all the linkedlist and using a temporary object as temp with location value to iterate inside the loop
                tempNode = self.head
                index = 0

                while index < (location - 1):
                    # keep assigning the next value of tempnode till the location is reached in LL
                    tempNode = tempNode.next
                    index += 1
                # assign a dummy value of nextNode to temp store current LL value
                nextNode = tempNode.next
                tempNode.next = newNode  # now place a newNode in middle
                # given newly placed newNode with the temp stored value of current LL value
                newNode.next = nextNode


def printReverseLL(head):
    if head == None:
        return
    printReverseLL(head.next)
    print(head.value)


def printLL(head):
    temp = head
    while temp != None:
        print(temp.value)
        temp = temp.next


def compareLL(firstLL, secondLL):
    condition_checker = True
    temp1, temp2 = firstLL, secondLL
    while temp1 and temp2:
        if temp1.value != temp2.value:
            condition_checker = False
        temp1, temp2 = temp1.next, temp2.next

    if condition_checker == True:
        print("Condition OK!")
    else:
        print("Condition NOT OK!")


def mergeLL(firstLL, secondLL):
    if firstLL == None and secondLL == None:
        return
    if firstLL == None:
        return secondLL
    if secondLL == None:
        return firstLL

    if firstLL.value < secondLL.value:
        temp = firstLL
        temp.next = mergeLL(firstLL.next, secondLL)
    else:
        temp = secondLL
        temp.next = mergeLL(firstLL, secondLL.next)

    return temp


def removeDuplicate(ekahs):
    temp = ekahs

    while temp:
        while temp.next and temp.next.value == temp.value:
            temp.next = temp.next.next
        temp = temp.next

    return ekahs


first_singleLinkedList = SLinkedList()
second_singleLinkedList = SLinkedList()


first_singleLinkedList.insertLinkedList(1, 0)
first_singleLinkedList.insertLinkedList(2, 1)
first_singleLinkedList.insertLinkedList(3, 2)
first_singleLinkedList.insertLinkedList(3, 3)
first_singleLinkedList.insertLinkedList(3, 4)
first_singleLinkedList.insertLinkedList(5, 5)
second_singleLinkedList.insertLinkedList(3, 0)
second_singleLinkedList.insertLinkedList(5, 1)
second_singleLinkedList.insertLinkedList(6, 2)


printLL(first_singleLinkedList.head)
printLL(second_singleLinkedList.head)
compareLL(first_singleLinkedList.head, second_singleLinkedList.head)
printLL(mergeLL(first_singleLinkedList.head, second_singleLinkedList.head))

removeDuplicate(first_singleLinkedList.head)

printLL(first_singleLinkedList.head)
