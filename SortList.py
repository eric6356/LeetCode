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
            slow = head
            fast = head.next
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            fast = slow
            slow = slow.next
            fast.next = None
            return self.merge_list(self.sortList(head), self.sortList(slow))
    