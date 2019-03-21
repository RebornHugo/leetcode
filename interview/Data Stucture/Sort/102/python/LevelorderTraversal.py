from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, q = [], [root]
        while q:
            cur = q.pop(0)
            if cur:
                res.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
        return res

    def levelOrder_leetcode(self, root):
        if not root: return []
        res, level = [], [root]
        while level:
            res.append([_.val for _ in level])
            temp = []
            for leaf in level:
                if leaf.left: temp.append(leaf.left)
                if leaf.right: temp.append(leaf.right)
            level = temp
        return res
