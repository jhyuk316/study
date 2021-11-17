
/**
 * TwoSum
 */
import java.util.Arrays;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] res = { 0, 0 };
        for (int i = 0; i < nums.length; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        TwoSum ts = new TwoSum();
        int[] res1 = ts.twoSum(nums, 9);
        System.out.println(Arrays.toString(res1));

        int[] nums1 = { 3, 2, 4 };
        res1 = ts.twoSum(nums1, 6);
        System.out.println(Arrays.toString(res1));

    }
}