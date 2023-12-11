#Runtime: 148 ms
#Memory Usage: 17.9 MB
def majorityElement(self, nums):
        n = len(nums)
        nums.sort()
        return nums[n//2]