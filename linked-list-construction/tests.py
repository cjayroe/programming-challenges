import unittest
from .solution import DoublyLinkedList, Node

class LinkedListConstructionTest(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_tail(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.assertEqual(1, self.list.head.value)
        self.assertEqual(None, self.list.head.prev)
        self.assertEqual(5, self.list.tail.value)
        self.assertEqual(4, self.list.tail.prev.value)

    def test_head(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setHead(node6)
        self.assertEqual(6, self.list.head.value)
        self.assertEqual(None, self.list.head.prev)
        self.assertEqual(1, self.list.head.next.value)
        
    def test_insert_before(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setTail(node6)
        self.list.insertBefore(node6, node7)
        self.list.insertBefore(node2, node7)
        self.assertEqual(7, self.list.tail.prev.value)
        self.assertEqual(7, self.list.head.next.value)
        
    def test_insert_after(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setTail(node6)
        self.list.insertAfter(node6, node7)
        self.list.insertAfter(node1, node7)
        self.assertEqual(7, self.list.tail.value)
        self.assertEqual(7, self.list.head.next.value)

    def test_contains_value(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setTail(node6)
        self.assertEqual(self.list.containsNodeWithValue(4), True)
        self.assertEqual(self.list.containsNodeWithValue(8), False)

    def test_remove(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setTail(node6)
        self.list.remove(node2)
        self.assertEqual(3, self.list.head.next.value)
        self.list.remove(node3)
        self.assertEqual(4, self.list.head.next.value)

    def test_remove_all(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setTail(node6)
        self.list.removeNodesWithValue(2)
        self.assertEqual(False, self.list.containsNodeWithValue(2))

    def test_insert_at(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        self.list.setTail(node1)
        self.list.setTail(node2)
        self.list.setTail(node3)
        self.list.setTail(node4)
        self.list.setTail(node5)
        self.list.setTail(node6)
        self.list.insertAtPosition(2, node7)
        self.assertEqual(2, self.list.head.next.value)

if __name__ == '__main__':
    unittest.main()