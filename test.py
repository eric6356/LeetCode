class LinkNode(object):
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

head = LinkNode(0)
tail = LinkNode(0)
a = LinkNode('a')
b = LinkNode('b')
head.next = a
a.next = b
b.next = tail
tail.prev = b
b.prev = a
a.prev = head

a, b = b, a

print 'done'