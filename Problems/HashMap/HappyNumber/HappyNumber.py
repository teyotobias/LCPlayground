#very fast algorithm but bad as far as memory usage goes

# Runtime: 36 ms, faster than 88.33% of Python3 online submissions for Happy Number.
# Memory Usage: 16.4 MB, less than 17.02% of Python3 online submissions for Happy Number.

class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit**2
            return total
        
        memory = set()
        while n!= 1 and n not in memory:
            memory.add(n)
            n = getNext(n)
        return n == 1
