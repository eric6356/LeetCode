# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        d = dict()
        i = 0
        pi = head
        if pi:
            while pi.next:
                d[i] = pi
                i += 1
                pi = pi.next
            d[i] = pi
            n = len(d)
            for i in range((n-1)/2):
                d[i].next = d[n-i-1]
                d[n-i-1].next = d[i+1]
                d[n-i-2].next = None
