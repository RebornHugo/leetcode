class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode 
        :type n: int 
        :rtype: ListNode
        """
        currentHead = head
        length = 1
        while currentHead:
            length += 1
            currentHead = currentHead.next
        n_from_start = length - n
        currentHead = head
        length = 1
        if n_from_start == 1:
            head = currentHead.next
            return head
        while length != n_from_start - 1:
            length += 1
            currentHead = currentHead.next
        nextHead = currentHead.next
        if nextHead is not None:
            currentHead.next = nextHead.next
        else:
            currentHead.next = None
        return head
