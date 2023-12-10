# Runtime: 509 ms, faster than 86.83% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 29.8 MB, less than 20.66% of Python3 online submissions for Contains Duplicate II.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        kSet = set()
        for i in range(len(nums)):
            if nums[i] in kSet:
                return True
            if len(kSet) >= k:
                kSet.remove(nums[i-k])
            kSet.add(nums[i])
        return False