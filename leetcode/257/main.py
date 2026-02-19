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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.results = []
        self.pathFinder(root, "")
        return self.results

    def pathFinder(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            self.results.append(path + str(node.val))
            return

        self.pathFinder(node.left, path + str(node.val) + "->")
        self.pathFinder(node.right, path + str(node.val) + "->")
