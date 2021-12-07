package Binary.NumberOf1Bits;
// 191. Number of 1 Bits
// https://leetcode.com/problems/number-of-1-bits/

class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;

        while (n != 0) {
            if ((n & 1) == 1) {
                count++;
            }
            n = n >>> 1;
        }
        return count;
    }
}


public class NumberOf1Bits {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.hammingWeight(11));
        System.out.println(sol.hammingWeight(-3));


    }
}
