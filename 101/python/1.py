# 101. Symmetric Tree https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # iterative

        q = [root, root]
        while q:
            t1 = q.pop()
            t2 = q.pop()
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        # recursive
        def twoTree(root1: TreeNode, root2: TreeNode):
            if (not root1) != (not root2): return False
            if not root1 and not root2: return True
            return root1.val == root2.val and twoTree(root1.left, root2.right) and twoTree(root1.right, root2.left)

        return twoTree(root, root)
