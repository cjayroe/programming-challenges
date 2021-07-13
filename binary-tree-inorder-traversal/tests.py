import unittest
from . import solution

class TestInOrderTraversal(unittest.TestCase):
    def setUp(self) -> None:
        self.inOrderTraversal = solution.InOrderTraversal()

    def test_one(self):
        self.assertTrue(self.inOrderTraversal.inorder_traversal())

    def test_basic_binary_tree(self):
        print(self.inOrderTraversal.build_binary_tree([1,2,3,None, None, 4, 5]))

if __name__ == '__main__':
    unittest.main()