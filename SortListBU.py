# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge_list(self, a, b):
        merged_head = ListNode(0)
        m = merged_head
        while a and b:
            if a.val < b.val:
                m .next = a
                a = a.next
            else:
                m.next = b
                b = b.next
            m = m.next
            m.next = None
        if a:
            m.next = a
        else:
            m.next = b
        return merged_head.next
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head

        else:
            h = head
            sz = 1
            while True:
                fast = h.next.next
                fast_prev = h.next
                slow = h.next
                slow_prev = h

                for i in range(sz-1):
                    slow_prev = slow
                    slow = slow.next
                    fast_prev = fast.next
                    fast = fast_prev.next
                fast_prev.next = None
                slow_prev.next = None
                self.merge_list(h, slow)
                h = fast
                sz += sz



