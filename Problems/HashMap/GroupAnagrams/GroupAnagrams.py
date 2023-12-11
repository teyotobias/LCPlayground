# Runtime: 101 ms, faster than 52.40% of Python3 online submissions for Group Anagrams.
# Memory Usage: 19.6 MB, less than 79.01% of Python3 online submissions for Group Anagrams.
def groupAnagrams(self, strs):
        mp = {}
        for i in range(len(strs)):
#returns a list of characters, not a string
            # currStr = sorted(strs[i])
#this is correct:
            currStr = ''.join(sorted(strs[i]))
            
            if currStr in mp:   
                mp[currStr].append(strs[i])
            else:
                mp[currStr] = []
                mp[currStr].append(strs[i])
        return list(mp.values())