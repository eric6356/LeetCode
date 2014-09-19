class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l0 = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l0.next = l1
l1.next = l2


def reorderList(head):
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

reorderList(l0)
print 'done'