# 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator/


from typing import List

# O(n) : 후위표현식으로 변환 후 계산
# 으아 구현 구질구질하다.
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        self.op = set(["+", "-"])

        exp = []
        opStack = []
        startMinus = True

        i = 0
        while i < len(s):
            if startMinus and s[i] == "-":
                exp.append("0")

            startMinus = False
            if s[i].isdigit():
                temp = s[i]
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                    temp += s[i]
                exp.append(temp)
                if opStack and opStack[-1] in self.op:
                    exp.append(opStack.pop())

            elif s[i] in self.op:
                opStack.append(s[i])

            elif s[i] == "(":
                startMinus = True
                opStack.append(s[i])

            elif s[i] == ")":
                if opStack[-1] == "(":
                    opStack.pop()
                    if opStack:
                        exp.append(opStack.pop())

            i += 1

        print(exp)
        return self.postfixCal(exp)

    def postfixCal(self, exp: List[str]):
        stack = []
        for c in exp:
            if c.isdigit():
                stack.append(int(c))
            elif c in self.op:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if c == "+":
                    stack.append(operand1 + operand2)
                elif c == "-":
                    stack.append(operand1 - operand2)

        return stack[0]


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.calculate, "3210", 3210)
    testSol(sol.calculate, "(5)", 5)
    testSol(sol.calculate, "(1 + 1)", 2)
    testSol(sol.calculate, "1 + 1", 2)
    testSol(sol.calculate, " 2-1 + 2 ", 3)
    testSol(sol.calculate, "(1+(4+5+2)-3)+(6+8)", 23)
    testSol(sol.calculate, "(1+(4+54+2)-103)+(6+8)", -28)
    testSol(sol.calculate, "  -(  -2+3)", -1)
