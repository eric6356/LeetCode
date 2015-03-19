class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(2)
a.next = b
b.next = a

def detectCycle(self, head):
    if head and head.next and head.next.next and head.next.next.next:
        slow = head.next
        fast = head.next.next
        while True:
            if fast == slow:
                fast = head
                while True:
                    if fast == slow:
                        return slow
                    fast = fast.next
                    slow = slow.next
            elif not fast.next or not fast.next.next:
                    return None
            fast = fast.next.next
            slow = slow.next
    else:
            return None

