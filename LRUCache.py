class LRUCache:
    class LinkNode(object):
        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache_dict = dict()
        self.capacity = capacity
        self.head = self.LinkNode(0, 0)
        self.tail = self.LinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        if not key in self.cache_dict:
            return -1
        else:
            self.cache_dict[key].prev.next = self.cache_dict[key].next
            self.cache_dict[key].next.prev = self.cache_dict[key].prev
            self.cache_dict[key].prev = self.tail.prev
            self.cache_dict[key].next = self.tail
            self.tail.prev.next = self.cache_dict[key]
            self.tail.prev = self.cache_dict[key]

            return self.cache_dict[key].val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache_dict:
            self.cache_dict[key].val = value
            self.cache_dict[key].prev.next = self.cache_dict[key].next
            self.cache_dict[key].next.prev = self.cache_dict[key].prev
        elif len(self.cache_dict) == self.capacity:
            self.cache_dict.pop(self.head.next.key)
            self.head = self.head.next
            self.head.next.prev = self.head
            self.cache_dict[key] = self.LinkNode(key, value)
        else:
            self.cache_dict[key] = self.LinkNode(key, value)
        self.cache_dict[key].prev = self.tail.prev
        self.cache_dict[key].next = self.tail
        self.tail.prev.next = self.cache_dict[key]
        self.tail.prev = self.cache_dict[key]
