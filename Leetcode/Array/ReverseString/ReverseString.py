from typing import List


# O(n) fail
class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l // 2 :]) + self.reverseString(s[: l // 2])


# O(n)
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        self._reverseString(s, 0)

    def _reverseString(self, s: List[str], pos: int) -> None:
        if pos >= len(s) // 2:
            return
        s[pos], s[-pos - 1] = s[-pos - 1], s[pos]

        return self._reverseString(s, pos + 1)


# O(n)
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]


if __name__ == "__main__":
    sol = Solution()

    a = ["a", "b", "c", "d", "e"]
    print(a)
    print(sol.reverseString(a))
    print(a)
