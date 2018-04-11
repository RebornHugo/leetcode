# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = self.decode_ListNode(l1)
        val2 = self.decode_ListNode(l2)
        val = val1 + val2
        return self.encode_ListNode(val)

    def decode_ListNode(self, l):
        if l.next is None and l.val == 0:
            return 0
        counter, res = 0, 0
        while l:
            res += l.val * 10 ** counter
            l = l.next
            counter += 1

        return res

    def encode_ListNode(self, value):
        if value == 0:
            return ListNode(0)
        l = ListNode(value % 10)
        head = l
        value = value // 10
        while value:
            l2 = ListNode(value % 10)
            l.next = l2
            value = value // 10
            l = l2
        return head


if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6
    s = Solution()
    v = s.decode_ListNode(l1)
    print(v)
    l = s.encode_ListNode(v)
    print(l.val)
    while True:
        l = l.next
        print(l.val)
        if not l.next:
            break
    res = s.addTwoNumbers(l1, l4)
    print(res.val)
    while res:
        print(res.val)
        res = res.next
