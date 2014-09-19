# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head and head.next:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            m = slow.next
            slow.next = None

            m_next = m.next
            m.next = None
            while m_next:
                temp = m
                m = m_next
                m_next = m.next
                m.next = temp

            l = head
            while m:
                l_next = l.next
                m_next = m.next
                l.next = m
                m = m_next
                l.next.next = l_next
                l = l_next

            return head



