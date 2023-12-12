# Runtime: 48 ms
# Memory Usage: 16.3 MB
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+= 1
            j += 1
        
        return i == len(s)