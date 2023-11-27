def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window, longest substr between left and right
            #increment right and find length as you go
            #move left to index of initial instance of repeating character + 1
        length, left = 0, 0
        letMap = {}
        for right in range(len(s)):
            if s[right] in letMap and letMap[s[right]] >= left:
                left = letMap[s[right]] + 1
            else:
                length = max(length, right-left+1)
            letMap[s[right]] = right
        return length