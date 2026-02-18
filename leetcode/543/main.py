from typing import Optional


class TreeNode:
    pass


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dimeter = 0

        self.calculate_height(root)

        return self.max_dimeter

    def calculate_height(self, node):
        if not node:
            return 0

        left_h = self.calculate_height(node.left)
        right_h = self.calculate_height(node.right)

        self.max_dimeter = max(self.max_dimeter, left_h + right_h)

        return 1 + max(left_h, right_h)
