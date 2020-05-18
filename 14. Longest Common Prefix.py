class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        if len(strs) == 1:
            return strs[0]

        if all(elem == strs[0] for elem in strs):
            return strs[0]

        ref = strs[0]
        ptr = 0

        while ptr < len(ref):
            for word in strs:
                if len(word) <= ptr or word[ptr] != ref[ptr]:
                    if ptr == 0:
                        return ""
                    else:
                        return ref[0:ptr]
            ptr += 1

        if ptr == 1:
            return ref[0:ptr]

        return ref[0:ptr]

