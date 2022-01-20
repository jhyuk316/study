# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/


from typing import List

"""
이 문제가 왜이렇게 어려울까?
그래프화해서 DFS 너무 오래걸림.
정렬 후 DP. 이 방법이 너무 안 떠올랐음.
"""

# O(n*logn) 해답 왜 이게 된다는 거지?
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        maxLength = 1
        end = intervals[0][1]
        for s, e in intervals:
            if end <= s:
                maxLength += 1
                end = e  # 왜 Greedy하게 되는가? 이 부분이 참 공감이 안됨.
            print(maxLength, end=" ")

        print()
        return len(intervals) - maxLength


# O(n*logn) dp dp[i] = dp[j-1] + 1 j:겹치는 interval
class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        dp = [0] * (len(intervals) + 1)

        j = 0
        for i in range(len(intervals)):
            while intervals[j][1] <= intervals[i][0]:
                j += 1
            dp[i] = dp[j - 1] + 1

        print(dp)
        return len(intervals) - dp[-2]


# O(n^2) 그래프 DFS 메모이제이션, Time Limit Exceeded
class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        results = []
        dp = [-1] * len(intervals)
        print(len(intervals))

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            tempMax = 0
            for j in range(i + 1, len(intervals)):
                if intervals[i][1] <= intervals[j][0]:
                    tempMax = max(tempMax, dfs(j))

            dp[i] = tempMax + 1
            return dp[i]

        for i in range(len(intervals)):
            dfs(i)

        print(dp)

        return len(intervals) - max(dp)


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.eraseOverlapIntervals, [[1, 2], [2, 3], [3, 4], [1, 3]], 1)
    testSol(sol.eraseOverlapIntervals, [[1, 3], [1, 2], [2, 3], [3, 4]], 1)
    testSol(
        sol.eraseOverlapIntervals, [[1, 2], [3, 4], [2, 5], [3, 4], [4, 6], [3, 4]], 3
    )
    testSol(sol.eraseOverlapIntervals, [[1, 2], [1, 2], [1, 2]], 2)
    testSol(sol.eraseOverlapIntervals, [[1, 2], [2, 3]], 0)
    testSol(sol.eraseOverlapIntervals, [[1, 2], [2, 3], [1, 3], [2, 5]], 2)
    testSol(
        sol.eraseOverlapIntervals,
        [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]],
        4,
    )
