# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/


# O(m*n), 공간은 1개 더 잡아서 [0] 처리를 따로 하지 않음.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        temp = [0] * (len(text2) + 1)

        for i, t1 in enumerate(text1):
            for j, t2 in enumerate(text2):
                if t1 == t2:
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(dp[j], temp[j - 1])
            # print(temp)

            # dp = temp.copy()
            dp, temp = temp, dp

        # print(dp)
        return dp[-2]


# O(m*n^2), 파이썬에서 list의 max값을 구할 때 O(n)일까?
class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text2)
        temp = [0] * len(text2)

        for i, t1 in enumerate(text1):
            for j, t2 in enumerate(text2):
                if t1 == t2:
                    if j == 0:
                        temp[0] = 1
                    else:
                        temp[j] = max(dp[:j]) + 1
            # print(temp)
            dp = temp.copy()

        # print(list(text1))
        # print(list(text2))
        # print(dp)
        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))
    print(sol.longestCommonSubsequence("bcdef", "ace"))
    print(sol.longestCommonSubsequence("abcbbaba", "aaabbbbba"))
    print(sol.longestCommonSubsequence("abcbabab", "ab"))
    print(sol.longestCommonSubsequence("cabdeee", "aceee"))
    print(sol.longestCommonSubsequence("ezupkr", "ubmrapg"))
    print(sol.longestCommonSubsequence("ezupkrbmapg", "ubmrapg"))
    print(sol.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
    print(sol.longestCommonSubsequence("hafcdqbgncrcbihkd", "pmjghexybyrgzczy"))
