def hasCycle(head):
    if head and head.next:
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next
                if fast == slow:
                    return True
            else:
                return False
            if fast.next:
                fast = fast.next
                if fast == slow:
                    return True
            else:
                return False
    else:
        return False
