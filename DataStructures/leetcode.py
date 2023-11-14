#nums1 already has enough space to fit m + n elements
def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    
    nums1.sort()



def majorityElement(nums): 
    numMap = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in numMap:
            numMap[nums[i]] +=1
        else:
            numMap[nums[i]] = 1
        if numMap[nums[i]] > (n/2):
            return nums[i]

#another way

def majorityElement2(nums):
    n = len(nums)
    nums.sort()
    return nums[n//2]

def maxProfit(prices):
    maxProfit = 0
    min_price = prices[0]

    n = len(prices)
    for i in range(n):
        price = prices[i]
        if price < min_price :
            min_price = price
        else :
            maxProfit = max(maxProfit, price - min_price)
    return maxProfit

def removeDuplicates(nums) :
    index = 1
    n = len(nums)
    for i in range(n):
        if nums[i] != nums[i-1]:
            nums[index] = nums[i]
            index+=1
    return index

def removeElement(nums, val):
    index = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != val :
            nums[index] = nums[i]
            index += 1

    return index

def removeDuplicates2(nums):
    n = len(nums)
    if( n <= 2):
        return n
    
    index = 2
    for i in range(2,n) :
        if nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1
    return index


def maxArea(height):
    #water: minNum * (bigIndex - smallIndex)
        left = 0
        right = len(height) - 1
        maxA = 0
        while(left < right):
            currentA = min(height[left], height[right]) * (right - left)
            maxA = max(maxA, currentA)
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return maxA

def RomanToInteger(s):
    answer = 0
    romanMap = {
            'I' : 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    n = len(s)
    for i in range(n):
        if i < n-1 and romanMap[s[i]] < romanMap[s[i+1]]:
            answer -= romanMap[s[i]]
        else:
            answer += romanMap[s[i]]
    return answer


def jump(nums):
    if len(nums) <= 1: return 0
    left, right = 0, nums[0]
    jumps = 1
    while right < len(nums) -1:
        jumps+=1
        nxt = max(nums[i] + i for i in range(left, right+1))
        left = right
        right = nxt
    return jumps    

def hIndex(citations):
    count = 0 #initialize counter
    citations.sort(reverse=True) #sort citations in reversed order
    for i, j in enumerate(citations): #key,values pairs
        if i < j:
            count +=1
    return count

def productExceptSelf(nums):
    # for i in range(x,y,z) - start,stop,step
    # using division property
    # product = 1
    # num_zeros = 0
    # n = len(nums)
    # for i in range(n):
    #     if nums[i] == 0:
    #         num_zeros += 1
    #     else:
    #         product *= nums[i]
    # if num_zeros > 1:
    #     return [0 for num in nums]
    # if num_zeros != 0:
    #     return [0 if num == 0 else int(product) for num in nums]
    # return [int(product/num) for num in nums]

    #without using division - prefix and postfix products
    n = len(nums)
    results = [0]*n
    prefix_product = 1
    postfix_product = 1
    for i in range(n):
        results[i] = prefix_product
        prefix_product *= nums[i]
    for i in range(n-1, -1, -1):
        results[i] *= postfix_product
        postfix_product *= nums[i]
    return results








testProductExceptSelf = [1,2,3,4]
print(productExceptSelf(testProductExceptSelf))