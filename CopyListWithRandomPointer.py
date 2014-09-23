# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# class Solution:
#     # @param head, a RandomListNode
#     # @return a RandomListNode
def copyRandomList(head):
        if not head:
            return head
        p = head
        while p.next:
            tmp = RandomListNode(p.label)
            tmp.next = p.next
            p.next = tmp
            p = tmp.next
        tmp = RandomListNode(p.label)
        tmp.next = p.next
        p.next = tmp
        p = head
        while p.next.next:
            if p.random:
                p.next.random = p.random.next
            else:
                p.next.random = None
            p = p.next.next
        if p.random:
           p.next.random = p.random.next
        else:
            p.next.random = None
        p = head
        head = p.next
        while p.next.next:
            tmp = p.next
            p.next = p.next.next
            p = tmp.next
            tmp.next = p.next
        p.next = None
        return head