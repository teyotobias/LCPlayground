# Runtime: 50 ms
# Memory Usage: 17.1 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        while l < r:
            while not s[l].isalnum() and l < r:
                l+= 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                print(s[r] + s[l])
                return False
            l += 1
            r -= 1
        return True