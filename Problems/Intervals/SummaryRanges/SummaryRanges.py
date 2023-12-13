# Runtime: 37 ms, faster than 62.38% of Python3 online submissions for Summary Ranges.
# Memory Usage: 16.4 MB, less than 20.62% of Python3 online submissions for Summary Ranges.

def SummaryRanges(nums):
    intervals = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
            i += 1
        if start == nums[i]:
            intervals.append(str(start))
        else:
            intervals.append(str(start) + "->" + str(nums[i]))
        i += 1
    return intervals
