class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        p2 = 0
        p3 = 0

        if needle == "":
            return 0

        while p2 < len(haystack):
            if haystack[p2] == needle[p3]:
                p2 += 1
                p3 += 1
                if p2 - p1 == len(needle):
                    return p1
            else:
                if p1 != p2:
                    p3 = 0
                    p1 += 1
                    p2 = p1
                else:
                    p1 += 1
                    p2 += 1
        return -1