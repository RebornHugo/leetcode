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

        def postorder(cur):
            if cur:
                postorder(cur.left)
                postorder(cur.right)
                res.append(cur.val)

        postorder(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stack = [], [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))  # 这里注意先右边进栈再左边进栈
                    stack.append((cur.left, False))

        return res
