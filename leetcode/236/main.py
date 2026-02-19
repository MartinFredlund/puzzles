from typing import Optional


class TreeNode:
    pass


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        search_left = self.lowestCommonAncestor(root.left, p, q)
        search_right = self.lowestCommonAncestor(root.right, p, q)

        if search_left and search_right:
            return root
        elif search_left:
            return search_left
        elif search_right:
            return search_right

        return None
