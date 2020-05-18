class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_len = 0

        for char in s:
            if char in str_list:
                str_list = str_list[str_list.index(char) + 1:]

            str_list.append(char)
            max_len = max(max_len, len(str_list))

        return max_len

