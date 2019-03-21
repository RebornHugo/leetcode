# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        res = []

        def f(cur):
            if cur:
                f(cur.left)
                f(cur.right)
                res.append(cur.val)

        f(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodes, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                nodes.insert(0, node.val)
                stack += [node.left, node.right]
        return nodes