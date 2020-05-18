def push_to_end(index, nums):
    while index < len(nums) - 1:
        temp = nums[index + 1]
        nums[index + 1] = nums[index]
        nums[index] = temp
        index += 1
    return nums


def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1

        return p1 + 1

