class Solution {
    public int maxSum(int[] dp, int[] arr, int start, int end, int k) {
        int maxValue = Integer.MIN_VALUE;
        int max = Integer.MIN_VALUE;

        while (start >= 0 && end - start + 1 <= k) {
            maxValue = Math.max(maxValue, arr[start]);

            max = Math.max(max, dp[start] + ((end - start + 1) * maxValue));

            start--;
        }

        return max;
    }

    public int maxSumAfterPartitioning(int[] arr, int k) {
        int[] dp = new int[arr.length + 1];
        dp[0] = 0;

        for (int i = 0; i < arr.length; i++) {
            // Exclude from the ongoing subarray
            int exclude = dp[i] + arr[i];

            // Include in the ongoing array
            int include = maxSum(dp, arr, i, i, k);

            dp[i + 1] = Math.max(exclude, include);
        }

        return dp[dp.length - 1];
    }
}