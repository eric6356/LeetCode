# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return None
        cur = end = head
        for i in range(n):
            end = end.next
        if not end:
            return head.next
        while end.next:
            cur = cur.next
            end = end.next
        cur.next = cur.next.next
        return head