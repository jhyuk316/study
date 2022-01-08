# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

# O(nlogn) 가장 긴 스트링을 유지. 덮어써 가면서 갱신
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            self.binarySearchInput(num, lis)
            # print(lis)

        return len(lis)

    def binarySearchInput(self, num, list: List):
        left = 0
        right = len(list) - 1

        if len(list) == 0:
            list.append(num)
            return

        mid = (right + left) // 2
        while left < right:
            if list[mid] == num:
                break
            elif list[mid] < num:
                left = mid + 1
            else:
                right = mid
            mid = (right + left) // 2

        # print(mid)
        if list[mid] >= num:
            list[mid] = num
        else:
            if mid + 1 >= len(list):
                list.append(num)
            else:
                list[mid + 1] = num


# O(n^2)
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengthList = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            temp = 0
            for j in reversed(range(i)):
                if nums[i] > nums[j]:
                    temp = max(temp, lengthList[j])
            lengthList[i] = temp + 1
        # print(lengthList)
        return max(lengthList)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([3, 1, 4, 2]))
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(sol.lengthOfLIS([10, 9, 4, 5, 3, 7, 101, 18]))
    print(sol.lengthOfLIS([5, 2, 3, 7, 1, 4, 6]))
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(sol.lengthOfLIS([4, 10, 4, 3, 8, 9]))
