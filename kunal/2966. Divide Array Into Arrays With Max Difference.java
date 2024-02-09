import java.util.Arrays;

class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int subarray_count = nums.length / 3;
        int[][] ans = new int[subarray_count][3];

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i = i + 3) {
            if ((nums[i + 2] - nums[i]) <= k) {
                ans[i / 3][0] = nums[i];
                ans[i / 3][1] = nums[i + 1];
                ans[i / 3][2] = nums[i + 2];
            } else {
                return new int[0][0];
            }
        }

        return ans;
    }
}
