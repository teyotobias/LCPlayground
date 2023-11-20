class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candy = [1] * n
        if n == 1:
            return 1
        #front pass -> checking if greater than to the right
        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                candy[i+1] = max(candy[i+1], candy[i] + 1)
        # back pass -> checking if rating greater than to the left
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candy[i-1] = max(candy[i-1], candy[i] + 1) 

        return sum(candy)
