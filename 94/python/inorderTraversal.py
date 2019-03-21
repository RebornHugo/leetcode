# 9 4Binary Tree Inorder Traversal

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def inorderTraversal_1(self, root: TreeNode) -> List[int]:
        # recursive (trivial
        res = []

        def inorder(cur: TreeNode):
            if cur:
                inorder(cur.left)
                res.append(cur.val)
                inorder(cur.right)

        inorder(root)
        return res
