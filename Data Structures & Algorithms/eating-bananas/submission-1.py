class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need to use math.ceil
        l, r = 1, max(piles) # max eating speed is the largest
        res = r # can update if find a slower eating speed that is sufficient

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <=h:
                res = k # we can update res to a smaller value as we search to the left
                r = k-1
            else:
                l = k + 1
        return res

        