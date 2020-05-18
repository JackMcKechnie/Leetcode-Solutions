class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        numrev = ""
        for i in reversed(range(len(num))):
            numrev += num[i]

        if numrev == num:
            return True
        return False


