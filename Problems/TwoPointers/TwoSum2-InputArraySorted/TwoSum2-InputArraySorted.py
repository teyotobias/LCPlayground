# Runtime: 111 ms, faster than 91.65% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 17.3 MB, less than 8.00% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

class Solution:
    def twoSum(self, numbers, target):
        numMap = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in numMap:
                return [numMap[complement]+1, i+1]
            else:
                numMap[numbers[i]] = i