# https://leetcode.com/problems/coin-change/
# 322. Coin Change


from typing import List

# O(amount * coins)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 2 ** 31 - 1
        countList = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue

                countList[i] = min(countList[i], countList[i - coin] + 1)

        print(countList)

        return countList[amount] if countList[amount] != MAX else -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.coinChange([474, 83, 404, 3], 264))
