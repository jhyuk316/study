# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

import collections

# 아 허무하다
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


# Dict 대신 list를 써보자! 똑같음
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        cList = [0] * 255

        for c in s:
            cList[ord(c)] += 1

        for c in t:
            if cList[ord(c)] > 0:
                cList[ord(c)] -= 1
            else:
                return False

        if sum(cList) != 0:
            return False

        return True


# O(m+n) 느림 왜지?
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        cMap = {}

        for c in s:
            if c in cMap:
                cMap[c] += 1
            else:
                cMap[c] = 1

        for c in t:
            if c in cMap:
                cMap[c] -= 1
            else:
                return False

        for val in cMap.values():
            if val != 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("anagram", "anagaram"))
