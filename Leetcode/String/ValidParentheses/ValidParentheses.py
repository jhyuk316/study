# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        openDict = {"(": "s", "{": "m", "[": "l"}
        closeDict = {")": "s", "}": "m", "]": "l"}
        stackParen = []

        for c in s:
            if c in openDict:
                stackParen.append(openDict[c])
            elif c in closeDict:
                if not stackParen or stackParen.pop() != closeDict[c]:
                    return False

        if stackParen:
            return False
        return True


# O(n)
class Solution1:
    def isValid(self, s: str) -> bool:
        stackParen = []

        for c in s:
            if c == "(":
                stackParen.append("s")
            elif c == "{":
                stackParen.append("m")
            elif c == "[":
                stackParen.append("l")
            elif c == ")":
                if not stackParen or stackParen.pop() != "s":
                    return False
            elif c == "}":
                if not stackParen or stackParen.pop() != "m":
                    return False
            elif c == "]":
                if not stackParen or stackParen.pop() != "l":
                    return False

        if stackParen:
            return False
        return True


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.isValid, "()", True)
    testSol(sol.isValid, "()[]{}", True)
    testSol(sol.isValid, "(]", False)
    testSol(sol.isValid, "([)]", False)
    testSol(sol.isValid, "]", False)
    testSol(sol.isValid, "[[[", False)
