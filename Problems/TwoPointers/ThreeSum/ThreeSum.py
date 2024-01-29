# Runtime: 683 ms, faster than 95.84% of Python3 online submissions for 3Sum.
# Memory Usage: 20.8 MB, less than 20.94% of Python3 online submissions for 3Sum.


# redo problem soon - check for pattern
def threeSum(nums):
    # make a result set to hold all triplets that add up to 0
    #gather pos, neg, and zeros into 3 different lists
    # make a set of pos and negs out of the lists
    #check for possible scenarios to add up to 0:
        # Three 0s
        # One 0, 1 pos, 1 neg
        # two positive, 1 negative
        # two negative, 1 positive
    res = set()
    p, n, z = [], [], []
    for num in nums:
        if num < 0:
            n.append(num)
        if num == 0:
            z.append(num)
        else:
            p.append(num)
    positives, negatives = set(p), set(n)
    if z:
        for pos in positives:
            if (-1*pos) in negatives:
                res.add((-1*pos, 0, pos))
    if len(z) >= 3:
        res.add((0,0,0))
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -1*(p[i] + p[j])
            if target in negatives:
                res.add(tuple(sorted([p[i], p[j], target])))
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -1*(n[i] + n[j])
            if target in positives:
                res.add(tuple(sorted([n[i], n[j], target])))
    return res