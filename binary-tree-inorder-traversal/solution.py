class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InOrderTraversal():
    def __init__(self):
        pass

    def inorder_traversal(self):
        return True

    def build_binary_tree(self, numbers: list):
        tree = None
        current_node = None
        previous_node = None
        left_skipped = False
        right_skipped = False

        for number in numbers:
            if not tree:
                tree = TreeNode(number)
                current_node = tree
                continue

            if current_node.left and current_node.right:
                previous_node = current_node
                current_node = current_node.left

            if left_skipped and right_skipped:
                current_node = previous_node
                left_skipped = False
                right_skipped = False
            
            if current_node.left and right_skipped:
                current_node = current_node.left
                left_skipped = False
                right_skipped = False
            
            if current_node.right and left_skipped:
                current_node = current_node.right
                left_skipped = False
                right_skipped = False

            
            if not current_node.left and not left_skipped:
                if not number:
                    left_skipped = True
                    current_node.left = None
                else:
                    current_node.left = TreeNode(number)
                
                continue

            if not current_node.right and not right_skipped:  
                if not number:
                    right_skipped = True
                    current_node.right = None
                else:
                    current_node.right = TreeNode(number)

                continue

        return tree
            
