package Binary.ReverseBits;
// 190. Reverse Bits
// https://leetcode.com/problems/reverse-bits/

// O(n)
class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; ++i) {
            result = result << 1;
            result = result + (n & 1);
            n = n >>> 1;
        }

        return result;
    }
}


public class ReverseBits {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.reverseBits(43261596));
        System.out.println(sol.reverseBits(-3));
    }
}
