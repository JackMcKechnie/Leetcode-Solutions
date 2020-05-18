class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxi = min(height[p1], height[p2]) * (p2 - p1)
        while p1 != p2:
            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1
            if min(height[p1], height[p2]) * (p2 - p1) > maxi:
                maxi = min(height[p1], height[p2]) * (p2 - p1)

        return maxi