

#28. Find the Index of the First Occurrence in a String
#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    n,m = len(haystack), len(needle)
    i = 0
    while i <= n - m:
        for j in range(m):
            if needle[j] != haystack[i + j]:
                break
            if j == m - 1:
                return i
        i += 1
    return -1

str1 = "sadbutsad"
str2 = "sad"

print(strStr(str1, str2))