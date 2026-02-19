from typing import Optional
from types import List


class TreeNode:
    pass


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.calcTree(root, 0)
        return self.sum

    def calcTree(self, node, currentVal):

        if not node.left and not node.right:
            self.sum += (currentVal * 10) + node.val
            return

        if node.left:
            self.calcTree(node.left, (currentVal * 10) + node.val)
        if node.right:
            self.calcTree(node.right, (currentVal * 10) + node.val)
