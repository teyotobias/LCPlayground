class Solution:
#fastest solution uncommented, memory efficient solution commented
# 12/09/2023 17:08	Accepted	384 ms	32.4 MB	python3
# 11/29/2023 00:41	Accepted	402 ms	31.3 MB	python3

    def longestConsecutive(self, nums):
        numSet = set(nums)
        if len(numSet) <= 1:
            return len(numSet)
        longest = 1
        for x in numSet:
            if x-1 not in numSet:
                y = x + 1
                while y in numSet:
                    y += 1
                longest = max(longest, y-x)
        return longest
    

# def longestConsecutive(nums):
#     nums = set(nums)
#     best = 0
#     for x in nums:
#         if x - 1 not in nums:
#             y = x + 1
#             while y in nums:
#                 y += 1
#             best = max(best, y - x)
#     return best


