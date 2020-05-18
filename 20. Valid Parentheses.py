def isOpening(s):
    if s == "(" or s == "{" or s == "[":
        return True
    return False


def isSameType(o, c):
    if o == "(" and c == ")":
        return True
    if o == "[" and c == "]":
        return True
    if o == "{" and c == "}":
        return True
    return False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if isOpening(char):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                o = stack.pop()
                if isSameType(o, char) == False:
                    return False
        return len(stack) == 0



