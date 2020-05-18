def push_to_end(index, nums):
    while index < len(nums) - 1:
        temp = nums[index + 1]
        nums[index + 1] = nums[index]
        nums[index] = temp
        index += 1
    return nums


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0

        while p2 < len(nums):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1

        return p1
