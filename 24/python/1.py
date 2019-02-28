# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        cur = dummy.next
        if not cur:
            return dummy.next
        _next = cur.next
        if not _next:
            return dummy.next
        while cur:
            if _next:
                last.next = _next
                cur.next = _next.next
                _next.next = cur

                last = cur
                cur = last.next
                if cur and cur.next:
                    _next = cur.next
                else:
                    return dummy.next
