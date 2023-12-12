# Runtime: 212 ms
# Memory Usage: 29.6 MB

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # float('inf') to initialize to infinitely large value
        l, sums, minVal = 0, 0, float('inf')
        for r in range(len(nums)):
            sums += nums[r]

            while sums >= target:
                minVal = min(minVal, r-l+1)
                sums -= nums[l]
                l+= 1
        return 0 if minVal == float('inf') else minVal