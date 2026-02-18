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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root) != -1

    def checkBalance(self, node):
        if not node:
            return 0
        right_child = self.checkBalance(node.right)
        left_child = self.checkBalance(node.left)

        if left_child == -1 or right_child == -1:
            return -1

        if abs(right_child - left_child) > 1:
            return -1

        return 1 + max(right_child, left_child)
