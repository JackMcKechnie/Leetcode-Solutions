class Solution:
    def intToRoman(self, num: int) -> str:
        ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        numerals = {1: "I", 2: "IV", 3: "V", 4: "IX",
                    5: "X", 6: "XL", 7: "L", 8: "XC",
                    9: "C", 10: "CD", 11: "D", 12: "CM",
                    13: "M"}
        left = num
        out_str = ""

        while left > 0:
            # If number left is a numeral
            if left in ints:
                out_str += numerals[ints.index(left) + 1]
                left -= left
                print(left)
                continue
            # If number left is bigger than 1k
            if left > 1000:
                out_str += "M"
                left -= 1000
                print(left)
            # If number left is not a numeral, find closest
            p1 = 0
            p2 = 1
            while p2 < len(ints):
                if left > ints[p1] and left < ints[p2]:
                    out_str += numerals[p1 + 1]
                    left -= ints[p1]
                    print(left)
                p1 += 1
                p2 += 1

        return out_str
