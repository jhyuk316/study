# 139. Word Break
# https://leetcode.com/problems/word-break/
#

"""
문제에 대한 생각.
DP로 풀어야만 하는가? 의문이 들었다.
DP가 아닌 방법으로 접근이 더 쉬웠던 것 같음.
하지만 실패하고 DP로 풀려고 여러 방법을 시도.

결과적으로 DP로 해결 하고 나니 신기하게도 전형적인 DP문제 였음. 충격!!!
이 문제를 받고 어떻게 DP라는 것을 알 수 있을까?
"""

from typing import List


# O(mn) : n = length of s, m = number of wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        checkList = [False] * len(s)

        for word in wordDict:
            if word == s[len(s) - len(word) :]:
                checkList[len(s) - len(word)] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue

                if word == s[i : i + len(word)] and checkList[i] == False:
                    checkList[i] = checkList[i + len(word)]

        # print(checkList)
        return checkList[0]


# 문제 해석 오류 ㅡㅡ;;
# 모든 단어가 한번씩 들어가야하는 줄 알았음.
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self._wordBreak(s, wordDict, [0] * len(wordDict))

    def _wordBreak(self, s: str, wordDict: List[str], count: List[int]) -> bool:
        tempCount = count.copy()

        # print("start ", s, tempCount)

        maxLen = max(map(len, wordDict))

        for i in range(maxLen + 1):
            if i > len(s):
                break

            if s[:i] in wordDict:
                pos = wordDict.index(s[:i])
                tempCount[pos] += 1
                # print("find", s[:i], tempCount)

                if i == len(s) and 0 not in tempCount:
                    # print("find answer ", tempCount)
                    return True

                if self._wordBreak(s[i:], wordDict, tempCount):
                    return True
                tempCount[pos] -= 1

        return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak("helloworld", ["hello", "world"]))
    print(sol.wordBreak("helloworldhello", ["world", "hello"]))
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
    print(sol.wordBreak("catsandcatsanddog", ["cats", "dog", "sand", "and", "cat"]))
    print(sol.wordBreak("catsandsandcats", ["cats", "and", "cat"]))
    print(sol.wordBreak("catcatssss", ["cats", "sss", "cat"]))
