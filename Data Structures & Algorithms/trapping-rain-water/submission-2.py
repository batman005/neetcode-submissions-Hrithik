class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        n = len(height)
        for i in range(n): 
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)

        return res