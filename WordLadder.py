class Solution:
    def dif(self, s1, s2, n):
        dif = 0
        for i in range(n):
            if s1[i] != s2[i]:
                dif += 1
        return dif

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        n = len(start)
        s_start = set()
        s_end = set()
        for d in dict:
            if self.dif(d, start, n) == 1:
                s_start.add(d)
        for d in dict:
            if self.dif(d, end, n) == 1:
                s_end.add(d)
        if not len(s_start) or not len(s_end):
            return 0
        if start in s_end or end in s_start:
            return 1

        s_start_now = s_start
        s_start_next = set()
        s_start_used = set()
        d_start = dict.copy()
        s_end_now = s_end
        s_end_next = set()
        s_end_used = set()
        d_end = dict.copy()
        for i in range(n/2):
            for t1 in s_start_now:
                for d in d_start:
                    if self.dif(d, t1, n) == 1 and not d in s_start_used:
                        d_start.remove(d)
                        s_start_next.add(d)
                        s_start_used.add(d)
            for e in s_end_now:
                if e in s_start_next:
                    return 2*i + 4
            for t1 in s_end_now:
                for d in d_end:
                    if self.dif(d, t1, n) == 1 and not d in s_end_used:
                        d_end.remove(d)
                        s_end_next.add(d)
                        s_end_used.add(d)
            for s in s_start_next:
                if s in s_end_next:
                    return 2*i + 5
            s_start_now = s_start_next
            s_start_next = set()
            s_end_now = s_end_next
            s_end_next = set()
        return 0