# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

"""
생각대로 짜면 되는데 바운더리 처리에 생각보다 애를 많이 먹음.
왜 생각대로 잘 안되는 걸까?
나만 어려운 문제 ㅠ.ㅠ
"""

from typing import List

# O(n)
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        # 리스트 합치기
        idx = len(intervals)
        for i, (starti, endi) in enumerate(intervals):
            if starti > newInterval[0]:
                idx = i
                break
        intervals.insert(idx, newInterval)

        # 리스트 줄이기
        tempIntervals = []
        idx = 0
        while idx < len(intervals):
            start = intervals[idx][0]
            end = intervals[idx][1]

            while idx < len(intervals) - 1 and end >= intervals[idx + 1][0]:
                end = max(end, intervals[idx + 1][1])
                idx += 1

            # print(idx, tempIntervals)
            tempIntervals.append([start, end])
            idx += 1

        return tempIntervals


if __name__ == "__main__":
    sol = Solution()

    print(sol.insert([[1, 3], [6, 9]], [2, 5]))
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(sol.insert([], [4, 8]))
    print(sol.insert([[1, 4]], [4, 8]))
    print(sol.insert([[2, 4]], [1, 3]))
    print(sol.insert([[1, 4]], [1, 3]))
