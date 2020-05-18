class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.lstrip()
        out_str = ""
        if s == "":
            return 0

        if s == "+" or s == "-":
            return 0

        if s[0] == "+" or s[0] == "-" or s[0].isdigit():
            if s[0] == "-":
                out_str += "-"
                s = s[1:]

            elif s[0] == "+":
                out_str += "+"
                s = s[1:]

            numbers = ""
            i = 0

            while i < len(s):
                if s[i].isdigit() == False:
                    break
                numbers += s[i]
                i += 1
            print(out_str)
            print(numbers)
            if (out_str == "+" or out_str == "-") and numbers == "":
                return 0

            if int(out_str + numbers) < -2147483648:
                return -2147483648
            if int(out_str + numbers) >= 2147483648:
                return 2147483647
            return int(out_str + numbers)

        return 0

        return 0