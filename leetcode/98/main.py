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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkChild(root, float("-inf"), float("inf"))

    def checkChild(self, node: Optional[TreeNode], low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return self.checkChild(node.left, low, node.val) and self.checkChild(
            node.right, node.val, high
        )
