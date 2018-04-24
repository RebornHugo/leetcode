# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:  # 注意这里要先判断p q 是否存在 才能取val值
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
       