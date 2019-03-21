# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        res = []

        def preorder(cur):
            if cur:
                res.append(cur.val)
                preorder(cur.left)
                preorder(cur.right)

        preorder(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res
