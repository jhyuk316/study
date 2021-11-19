package ContainsDuplicate;
// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ContainsDuplicate {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.containsDuplicate(new int[]{1,2,3,1}));
        System.out.println(sol.containsDuplicate(new int[]{1,2,3,4}));
        System.out.println(sol.containsDuplicate(new int[]{1,1,1,1}));

    }
}

// map
// class Solution {
//     public boolean containsDuplicate(int[] nums) {
//         Map<Integer, Integer> duple = new HashMap<Integer, Integer>();
//         for (int i = 0; i < nums.length; ++i) {
//             if (duple.containsKey(nums[i])) {
//                 return true;
//             } else {
//                 duple.put(nums[i], 1);
//             }
//         }

//         return false;
//     }
// }

// set
// HashSet 해쉬를 이용한 빠른 Set
// TreeSet 오름차순으로 정렬된 Set
// LinkedSet 입력 순서대로 저장되는 Set
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> duple = new HashSet<>();
        for (int num : nums) {
            if(duple.contains(num)){
                return false;
            }else{
                duple.add(num);
            }

        }
        return true;
    }
}