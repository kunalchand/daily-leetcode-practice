package rishabh;

import java.util.Arrays;

/*
 *  Approach: sort
    make sub arrays of size 3 and append to res
    if it's an invalid subarray (diff > k), then return []
    TIME: O(n * log n)
 */
class Solution {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(divideArray(new int[] {1,3,4,8,7,9,3,5,1}, 2)));      // o/p: [[1,1,3],[3,4,5],[7,8,9]]
    }

    public static int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        int[][] res = new int[nums.length / 3][3];
        for (int i = 0; i < nums.length; i += 3) {
            if ((nums[i + 2] - nums[i]) > k) { return new int[0][0]; }
            res[i / 3] = new int[] {nums[i], nums[i + 1], nums[i + 2]};
        }
        return res;
    }
}