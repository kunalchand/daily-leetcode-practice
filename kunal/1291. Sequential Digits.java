package kunal;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        String fixed = "123456789";

        List<Integer> ans = new ArrayList<>();

        for (int digit = String.valueOf(low).length(); digit <= String.valueOf(high).length(); digit++) {
            int left = 0;
            int right = left + digit;

            while (right <= fixed.length()) {
                String subString = fixed.substring(left, right);
                if (Integer.parseInt(subString) >= low && Integer.parseInt(subString) <= high) {
                    ans.add(Integer.parseInt(subString));
                }
                left++;
                right++;
            }
        }

        return ans;
    }
}