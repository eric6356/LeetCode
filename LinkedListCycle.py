def hasCycle(head):
    if head and head.next and head.next.next:
        slow = head
        fast = head.next
        while True:
            if fast == slow or fast.next == slow:
                return True
            else:
                fast = fast.next
                if not fast.next or not fast.next.next:
                    return False
            slow = slow.next
            fast = fast.next
    else:
        return False
