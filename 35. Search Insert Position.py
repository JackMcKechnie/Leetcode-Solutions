class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        if target < nums[0]:
            return 0

        if target > nums[len(nums) - 1]:
            return len(nums)

        p1 = 0
        p2 = 1

        while p2 < len(nums):
            if target > nums[p1] and target < nums[p2]:
                return p2
            else:
                p1 += 1
                p2 += 1

