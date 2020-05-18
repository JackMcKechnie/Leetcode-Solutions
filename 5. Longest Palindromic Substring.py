def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False


class Solution:
    def longestPalindrome(self, s: str) -> str:
        p1 = 0
        p2 = 1
        longest = ""
        while p1 < len(s):
            while p2 <= len(s):
                if (isPalindrome(s[p1:p2])):
                    if len(s[p1:p2]) > len(longest):
                        longest = s[p1:p2]
                p2 += 1
            p1 += 1
            p2 = p1 + 1

        return longest