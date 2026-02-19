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
    def goodNodes(self, root: TreeNode) -> int:
        return self.checkPath(root, float("-inf"))

    def checkPath(self, node, maxNumber):
        is_good = 0
        if not node:
            return 0
        if node.val >= maxNumber:
            is_good = 1
            maxNumber = node.val
        return (
            is_good
            + self.checkPath(node.left, maxNumber)
            + self.checkPath(node.right, maxNumber)
        )
