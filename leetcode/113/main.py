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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.results = []
        self.findPath(root, targetSum, [])
        return self.results

    def findPath(self, node, remainingSum, current):
        if not node:
            return

        if node.val == remainingSum and not node.left and not node.right:
            current.append(node.val)
            self.results.append(current)

        self.findPath(node.left, remainingSum - node.val, current + [node.val])
        self.findPath(node.right, remainingSum - node.val, current + [node.val])
