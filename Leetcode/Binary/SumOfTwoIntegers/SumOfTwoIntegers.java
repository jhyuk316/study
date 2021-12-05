package Binary.SumOfTwoIntegers;
// 371. Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    public int getSum(int a, int b) {
        int carry = (a & b) << 1;
        int sum = a ^ b;

        if (carry == 0) {
            return sum;
        }

        return getSum(sum, carry);
    }
}


public class SumOfTwoIntegers {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.getSum(1, 2));
        System.out.println(sol.getSum(15, 27));
        System.out.println(sol.getSum(3, 7));
        System.out.println(sol.getSum(1, 2));
    }

}
