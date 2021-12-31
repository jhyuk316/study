# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

"""
투포인트로 접근 하지만 너무 복잡하고 어려움.
당연하게도 실행 속도가 느림. 264ms, 18.48%보다 빠름.
복잡도도 정확히 계산을 못하겠음.
"""

# O(n+m)? O(mn)?
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        left = 0
        right = 0

        tDict = {}
        answer = []

        for c in t:
            if c in tDict:
                tDict[c] += 1
            else:
                tDict[c] = 1

        while s[left] not in tDict:
            left += 1
            if left >= len(s):
                return ""

        right = left

        while right < len(s):
            # print("lr ", left, right, tDict)
            if s[right] in tDict:
                tDict[s[right]] -= 1

            while self.checkDict(tDict):
                answer.append([left, right])

                tDict[s[left]] += 1

                left += 1
                while left < right and s[left] not in tDict:
                    left += 1

            right += 1

        if not answer:
            return ""

        lenAnswer = list(map(lambda x: x[1] - x[0], answer))
        pos = lenAnswer.index(min(lenAnswer))
        l = answer[pos][0]
        r = answer[pos][1] + 1

        return s[l:r]

    def checkDict(self, d: dict):
        for val in d.values():
            if val > 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(sol.minWindow("DDDADOBECODEBANC", "ABC"))
    print(sol.minWindow("DDDABBBBCCA", "ABC"))
    print(sol.minWindow("a", "a"))
    print(sol.minWindow("a", "aa"))
    print(sol.minWindow("aa", "aa"))
    print(sol.minWindow("a", "b"))
