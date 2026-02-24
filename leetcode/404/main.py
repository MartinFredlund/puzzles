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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sum(root, False)

    def sum(self, node, left):
        if not node:
            return 0

        if not node.left and not node.right:
            return node.val if left else 0

        return self.sum(node.left, True) + self.sum(node.right, False)
