
class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        found = numbers[i] + numbers[j] == target
        while(not found):
            if target > numbers[i] + numbers[j]:
                i += 1
            else:
                j -= 1
            found = numbers[i] + numbers[j] == target
        return [i+1,j+1]