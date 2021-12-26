# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cPosMap = {}
        maxLength = 0

        left = 0
        for right, c in enumerate(s):
            if c in cPosMap:
                left = max(left, cPosMap[c] + 1)

            cPosMap[c] = right
            # print("len ", left, right, right - left + 1)
            maxLength = max(maxLength, right - left + 1)

        return maxLength


# O(n)
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        maxLength = 0

        left = 0
        for i, c in enumerate(s):
            if c in count:

                for j in range(left, i):
                    left += 1
                    if c == s[j]:
                        break
                    count.remove(s[j])

            else:
                count.add(c)
            # print("len ", i - left, left, i)
            maxLength = max(maxLength, len(count))

        return maxLength


if __name__ == "__main__":
    sol = Solution()

    # print(sol.lengthOfLongestSubstring("bbbbb"))
    # print(sol.lengthOfLongestSubstring("abcabcbb"))
    # print(sol.lengthOfLongestSubstring("dvdf"))
    print(sol.lengthOfLongestSubstring("dfeffd"))
