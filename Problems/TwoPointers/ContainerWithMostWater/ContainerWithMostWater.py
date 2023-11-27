
def maxArea(self, height):
        left, right = 0, len(height) - 1
        maxA = 0
        while left < right:
            maxA = max(maxA, (min(height[left], height[right]) * (right-left)))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxA