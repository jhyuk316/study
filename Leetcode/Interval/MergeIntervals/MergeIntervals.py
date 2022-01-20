# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/


from typing import List


# O(n*logn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []
        i = 0
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            k = 1
            while i + k < len(intervals) and e >= intervals[i + k][0]:
                e = max(e, intervals[i + k][1])
                k += 1

            result.append([s, e])
            i = i + k

        return result


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.merge, [[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])
    testSol(
        sol.merge,
        [[1, 3], [8, 10], [2, 6], [15, 18], [0, 0]],
        [[0, 0], [1, 6], [8, 10], [15, 18]],
    )
    testSol(sol.merge, [[1, 4], [4, 5]], [[1, 5]])
