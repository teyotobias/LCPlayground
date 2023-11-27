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