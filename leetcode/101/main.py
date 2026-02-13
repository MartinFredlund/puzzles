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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return isMirror(root.left, root.right)


def isMirror(lr, rr):
    if not lr and not rr:
        return True

    if not lr or not rr:
        return False

    if lr.val != rr.val:
        return False

    return isMirror(lr.left, rr.right) and isMirror(lr.right, rr.left)
