# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

from typing import Dict


# O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLenth = 0
        cMap = {}

        left = 0
        length = 0
        for c in s:
            length += 1
            if c in cMap:
                cMap[c] += 1
            else:
                cMap[c] = 1

            # check
            maxChar = max(cMap, key=cMap.get)

            while length - cMap[maxChar] > k:
                if cMap[s[left]] == 1:
                    cMap.pop(s[left])
                else:
                    cMap[s[left]] -= 1
                length -= 1
                left += 1
                maxChar = max(cMap, key=cMap.get)
                print(cMap)

            print(maxChar)

            maxLenth = max(maxLenth, length)

        return maxLenth


if __name__ == "__main__":
    sol = Solution()

    print(sol.characterReplacement("ABAB", 2))
    print(sol.characterReplacement("AABABBA", 1))
    print(sol.characterReplacement("ABBBABAAA", 2))
