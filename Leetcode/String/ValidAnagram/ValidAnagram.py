# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/


# O(m+n) 느림 왜지?
class Solution:
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
