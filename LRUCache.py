class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache_dict = dict()
        self.capacity = capacity
        self.cap_list = list()

    # @return an integer
    def get(self, key):
        if not key in self.cache_dict:
            return -1
        else:
            self.touch(key)
            return self.cache_dict[key]

    def touch(self, key):
        l = len(self.cap_list)
        if l > self.capacity:  # full
            del self.cap_list[0]
        # if key in self.cap_list:
        l = len(self.cap_list)        
        for i in xrange(l):
            if self.cap_list[l-i-1] == key:
                self.cap_list.remove(key)
                break
        self.cap_list.append(key)


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.touch(key)
        self.cache_dict[key] = value

