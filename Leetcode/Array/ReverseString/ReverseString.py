from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        self._reverseString(s)

    def _reverseString(self, s: List[str]):

        return self._reverseString


class Solution1:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]


if __name__ == "__main__":
    sol = Solution()

    a = ["a", "b", "c", "d", "e"]
    print(a)
    sol.reverseString(a)
    print(a)
