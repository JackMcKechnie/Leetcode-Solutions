class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                    "IV": 4,
                    "IX": 9,
                    "XL": 40,
                    "XC": 90,
                    "CD": 400,
                    "CM": 900
                    }

        total = 0

        while (len(s) >= 2):
            if s[0] in numerals.keys() and s[0] + s[1] not in numerals.keys():
                print(s[0])
                total += numerals[s[0]]
                s = s[1:]
                continue
            print(s[0] + s[1])
            total += numerals[s[0] + s[1]]
            s = s[2:]

        if len(s) == 1:
            print(s[0])
            total += numerals[s[0]]

        return total

