# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


# O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimS = [c.lower() for c in s if c.isalnum()]
        return trimS == trimS[::-1]


# O(n)
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        trimS = [c.lower() for c in s if c.isalpha() or c.isdigit()]

        for i in range(len(trimS) // 2):
            if trimS[i] != trimS[-i - 1]:
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

    testSol(sol.isPalindrome, "A man, a plan, a canal: Panama", True)
    testSol(sol.isPalindrome, "race a car", False)
    testSol(sol.isPalindrome, " ", True)
    testSol(sol.isPalindrome, "12321", True)
    testSol(sol.isPalindrome, "123", False)
