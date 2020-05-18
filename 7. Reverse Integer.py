class Solution:
    def reverse(self, x: int) -> int:

        x_str = str(x)
        if x >= 0:
            revstr = x_str[::-1]
        else:
            temp = x_str[1::]
            temp2 = temp[::-1]
            revstr = "-" + temp2
        if (int(revstr) < -2 ** 31 or int(revstr) > 2 ** 31 - 1):
            return 0
        return int(revstr)