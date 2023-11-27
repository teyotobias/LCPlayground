class Solution:
    def twoSum(self, nums, target):

        complement = 0
        numsMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsMap:
                return [i, numsMap[complement]]
            numsMap[nums[i]] = i