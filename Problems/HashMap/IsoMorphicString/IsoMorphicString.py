# Runtime: 44 ms, faster than 70.09% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 16.5 MB, less than 63.65% of Python3 online submissions for Isomorphic Strings.
def isIsomorphic(s, t):
        if len(s) != len(t):
            return False
        sMapper, tMapper = {}, {}
        for i in range(len(s)):
            if s[i] not in sMapper:
                if t[i] in tMapper:
                    return False
                sMapper[s[i]] = t[i]
                tMapper[t[i]] = s[i]
            elif sMapper[s[i]] != t[i] or tMapper[t[i]] != s[i]:
                return False
        return True