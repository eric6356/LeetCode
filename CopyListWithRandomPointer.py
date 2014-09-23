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
        i = 0
        d = dict()
        if not head:
            return head
        while head:
            d[i] = head
            head = head.next
            i += 1
        head = RandomListNode(d[0].label)
        d_cpy = dict()
        d_cpy[0] = head
        n = len(d)
        for i in range(1, n):
            d_cpy[i] = RandomListNode(d[i].label)
            d_cpy[i-1].next = d_cpy[i]
        for i in range(n):
            j = 0
            tmp = d[i].random
            if not tmp:
                break
            while tmp:
                tmp = tmp.next
                j += 1
            d_cpy[i].random = d_cpy[n-j]
        return head