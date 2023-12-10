class Solution:
    
    def strStr(haystack, needle):
        n, m = len(haystack), len(needle)
        i = 0
        while i <= n-m:
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    break
                if j == m-1:
                    return i
            i += 1
        return -1