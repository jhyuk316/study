# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


"""
밖에서부터 줄여 오는 것이 빠른 것 같이 느껴졌지만,
실제로는 안에서부터 늘려가서 검사하는 것이 빠름.
중복적인 회문 검사를 줄일 수 있음.
aba가 회문이면 kabay는 한 칸씩 밖으로 회문을 검사.
하지만 kabay가 회문이 아니므로  aba를 또 뒤집어 검사.
근데 왜 DP 태그?
"""


# O(n^2) DP로는 어떻게 해야 하는 걸까?
"""
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ""
        maxLength = 0

        dp = [[0] * (len(s) + 1) for _ in range(len(s))]

        for i, c1 in enumerate(s):
            for j, c2 in enumerate(reversed(s)):
                if c1 == c2:
                    dp[i][j] = 1
                    k = 1
                    while dp[i - k][j - k] > 0:
                        if dp[i][j - k] > 0 and dp[i - k][j] > 0:
                            dp[i][j] = k + 1
                        k += 1

                    if maxLength < dp[i][j]:
                        tempStr = s[i + 1 - dp[i][j] : i + 1]
                        if tempStr != tempStr[::-1]:
                            continue

                        maxLength = dp[i][j]
                        maxPal = s[i + 1 - maxLength : i + 1]

        # print(*dp, sep="\n")
        return maxPal
"""


# O(n^2 ?) 빠른 해답을 보고 만든 것 왜 이게 더 빠른 걸까?
# java로 해보니 더 느림. 파이썬이 이상한 것
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        maxLen = 1
        start = 0

        for i in range(1, len(s)):
            odd = s[i - maxLen - 1 : i + 1]
            even = s[i - maxLen : i + 1]

            # 파이썬에서 [::-1]은 reverse를 생성하는 것이 아니라 제너레이터를 만드는 듯.
            if i - maxLen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxLen - 1
                maxLen += 2
            if i - maxLen >= 0 and even == even[::-1]:
                start = i - maxLen
                maxLen += 1

        return s[start : start + maxLen]


# O(n^2)
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:  # 숏컷이 없으면 아주 느림.
            return s

        maxPal = ""

        for i, c in enumerate(s):
            odd = self.maxPalindrome(s, i, i)
            even = self.maxPalindrome(s, i, i + 1)
            tempPal = odd if len(odd) > len(even) else even

            if len(maxPal) < len(tempPal):
                maxPal = tempPal

        return maxPal

    def maxPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]


# O(n^3)
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ""
        for i, c in enumerate(s):
            for j in reversed(range(i, len(s))):
                if len(maxPal) >= j - i + 1:
                    break
                if s[i] != s[j]:
                    continue
                if s[i : j + 1] != s[i : j + 1][::-1]:
                    continue

                maxPal = s[i : j + 1]

        return maxPal


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.longestPalindrome, "", "")
    testSol(sol.longestPalindrome, "a", "a")
    testSol(sol.longestPalindrome, "ab", "a")
    testSol(sol.longestPalindrome, "babad", "bab")
    testSol(sol.longestPalindrome, "cbbd", "bb")
    testSol(sol.longestPalindrome, "abczzzkg", "zzz")
    testSol(sol.longestPalindrome, "zzzkgnbf", "zzz")
    testSol(sol.longestPalindrome, "abcacz", "cac")
    testSol(sol.longestPalindrome, "aacabdkacaa", "aca")
    testSol(sol.longestPalindrome, "bbbbcakac", "cakac")
    testSol(sol.longestPalindrome, "abcdadcba", "abcdadcba")
    testSol(sol.longestPalindrome, "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa")
