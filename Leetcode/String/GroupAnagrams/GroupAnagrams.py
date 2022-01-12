# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import Dict, List, Tuple


# 문자의 개수를 키로
# O(m * n), m : number of strs, n : length of str
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDic: Dict[Tuple[int], List[str]] = {}

        for str in strs:
            key = self.makeKey(str)

            if key not in strDic:
                strDic[key] = []
            strDic[key].append(str)

        return strDic.values()

    # 기수 정렬
    def makeKey(self, str):
        char = [0] * 26
        for c in str:
            char[ord(c) - ord("a")] += 1
        return tuple(char)


# 정렬된 문자열을 키로
# O(m * nlogn), m : number of strs, n : length of str
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDic: Dict[str, list[str]] = {}

        for str in strs:
            key = "".join(sorted(str))
            if key not in strDic:
                strDic[key] = []
            strDic[key].append(str)

        return strDic.values()


# too slow 6032ms
# 정렬된 문자열 리스트를 만들고, 그 리스트의 인덱스로 원래 문자를 찾아 답 반환
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedStrs = list(map("".join, map(sorted, strs)))
        setStrs = set(sortedStrs)

        res = []
        for sStr in setStrs:
            temp = []
            for i, str in enumerate(sortedStrs):
                if sStr == str:
                    temp.append(i)
            res.append(temp)

        print(res)

        res = list(map(lambda x: list(map(lambda y: strs[y], x)), res))

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
