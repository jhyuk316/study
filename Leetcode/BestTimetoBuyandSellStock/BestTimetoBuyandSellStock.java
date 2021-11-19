package BestTimetoBuyandSellStock;
// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

public class BestTimetoBuyandSellStock {

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.maxProfit(new int[]{7,1,5,3,6,4}));
        System.out.println(sol.maxProfit(new int[]{7,6,4,3,1}));
        System.out.println(sol.maxProfit(new int[]{3,9,1,5,1}));
    }
}

class Solution {
    public int maxProfit(int[] prices) {
        int min = 10001;
        int max = 0;
        int tmpProfit = 0;
        int result = 0;

        for (int i = 0; i < prices.length; ++i) {
            if (prices[i] < min) {
                min = prices[i];
                max = prices[i];
            }
            if (prices[i] > max) {
                max = prices[i];
                tmpProfit = max - min;
                if (tmpProfit > result) {
                    result = tmpProfit;
                }
            }
        }

        return result;
    }
}