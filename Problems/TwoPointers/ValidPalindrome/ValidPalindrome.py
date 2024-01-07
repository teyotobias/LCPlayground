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
    


    def isPali(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

