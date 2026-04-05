class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime <= h:
                right = mid
            else:
                left = mid + 1
        return left