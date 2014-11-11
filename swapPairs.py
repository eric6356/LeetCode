# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head
        if not head.next:
            return head
        p = head
        q = head.next
        head = q
        while True:
            p.next = q.next
            q.next = p
            if p.next and p.next.next:
                t = p.next
                p.next = t.next
                p = t
                q = t.next
            else:
                break
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
S = Solution()
r = S.swapPairs(a)
while r.next:
    print r.val
    r = r.next
print r.val