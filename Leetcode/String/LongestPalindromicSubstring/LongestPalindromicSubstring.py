# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


# O(n^2) DP로는 어떻게 해야하는 걸까?
class Solution:
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


# O(n^2)
class Solution2:
    def longestPalindrome(self, s: str) -> str:
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

    testSol(sol.longestPalindrome, "babad", "bab")
    testSol(sol.longestPalindrome, "cbbd", "bb")
    testSol(sol.longestPalindrome, "abczzzkg", "zzz")
    testSol(sol.longestPalindrome, "zzzkgnbf", "zzz")
    testSol(sol.longestPalindrome, "abcacz", "cac")
    testSol(sol.longestPalindrome, "aacabdkacaa", "aca")
    testSol(sol.longestPalindrome, "bbbbcakac", "cakac")
    testSol(sol.longestPalindrome, "abcdadcba", "abcdadcba")

    testSol(sol.longestPalindrome, "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa")
