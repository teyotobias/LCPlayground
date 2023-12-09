# Runtime: 53 ms, faster than 62.80% of Python3 online submissions for Valid Anagram.
# Memory Usage: 16.8 MB, less than 46.48% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #memory efficient solution commented out
        #fastest solution present below uncommented
        sMapper = {}
        tMapper = {}
        for char in s:
            if char in sMapper:
                sMapper[char] += 1
            else:
                sMapper[char] = 1
        for char in t:
            if char in tMapper:
                tMapper[char] += 1
            else:
                tMapper[char] = 1
        
        return tMapper == sMapper
        
        
        
        
        # letMapper = {}
        # if len(s) != len(t):
        #     return False
        # for char in s:
        #     if char not in letMapper:
        #         letMapper[char] = 1
        #     else:
        #         letMapper[char] += 1
        # for char in t:
        #     if char not in letMapper or letMapper[char] == 0:
        #         return False
        #     else:
        #         letMapper[char] -= 1
        # return True