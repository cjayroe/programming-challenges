# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __str__(self):
        node_array = []
        end = self.head

        while end:
            print(
                f'node {end.value}, prev {end.prev.value if end.prev else None}, next {end.next.value if end.next else None}')
            node_array.append(end.value)
            end = end.next

        return str(node_array)

    def setHead(self, node: Node):
        if not self.head:
            self.head = node
            self.tail = self.head
            return

        previous_head = self.head
        self.head.prev = node
        self.head = self.head.prev
        self.head.next = previous_head

    def setTail(self, node: Node):
        if not self.tail:
            self.head = node
            self.tail = self.head
            return

        previous_tail = self.tail
        self.tail.next = node
        self.tail = self.tail.next
        self.tail.prev = previous_tail

    def insertBefore(self, node: Node, nodeToInsert: Node):
        current_node = self.head
        previous_node = None

        while current_node:
            if id(current_node) == id(node):
                previous_node.next = nodeToInsert
                current_node.prev = nodeToInsert
                nodeToInsert.prev = previous_node
                nodeToInsert.next = current_node
                break

            previous_node = current_node
            current_node = current_node.next

    def insertAfter(self, node: Node, nodeToInsert: Node):
        current_node = self.head
        next_node = self.head.next

        while current_node:
            if id(current_node) == id(node):
                if next_node:
                    next_node.prev = nodeToInsert

                current_node.next = nodeToInsert
                nodeToInsert.next = next_node
                nodeToInsert.prev = current_node
                break

            current_node = current_node.next
            next_node = current_node.next

        if current_node == self.tail:
            self.tail = current_node.next

    def insertAtPosition(self, position, nodeToInsert: Node):
        index = 1
        current_node = self.head

        while current_node:
            if index == position:
                previous_node = current_node.prev
                current_node.prev = nodeToInsert

                if previous_node:
                    previous_node.next = nodeToInsert
    
                nodeToInsert.prev = previous_node
                nodeToInsert.next = current_node
                break

            index += 1


    def removeNodesWithValue(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                previous_node = current_node.prev
                next_node = current_node.next
                
                if previous_node:
                    previous_node.next = next_node

                if next_node:
                    next_node.prev = previous_node
                
                current_node = next_node

            current_node = current_node.next

    def remove(self, node: Node):
        current_node = self.head

        while current_node:
            if current_node.value == node.value:
                previous_node = current_node.prev
                next_node = current_node.next
                
                if previous_node:
                    previous_node.next = next_node

                if next_node:
                    next_node.prev = previous_node
                
                break

            current_node = current_node.next


    def containsNodeWithValue(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True

            current_node = current_node.next
        
        return False
