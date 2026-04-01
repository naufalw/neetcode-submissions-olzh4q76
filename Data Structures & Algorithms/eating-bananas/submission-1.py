import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            k = (l + r) // 2

            total = sum([math.ceil(float(x)/k) for x in piles])

            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res