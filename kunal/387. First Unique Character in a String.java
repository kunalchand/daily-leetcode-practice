import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    // Heap Approach
    public int firstUniqChar(String s) {
        HashMap<Character, int[]> map = new HashMap<>(); // ['char' - [index, occurence]]

        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                int[] value = map.get(s.charAt(i));
                value[1] += 1; // increment the occurence
            } else {
                int[] value = new int[2];
                value[0] = i; // index
                value[1] = 1; // first occurence
                map.put(s.charAt(i), value);
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((element1, element2) -> {
            int element1_index = element1[0];
            int element2_index = element2[0];

            int element1_occurence = element1[1];
            int element2_occurence = element2[1];

            if (element1_occurence > element2_occurence)
                return 1;
            else if (element1_occurence < element2_occurence)
                return -1;
            else {
                if (element1_index > element2_index)
                    return 1;
                else
                    return -1;
            }
        });

        for (int[] value : map.values()) {
            pq.add(value);
        }

        if (pq.peek()[1] == 1) // If only one occurence
            return pq.peek()[0]; // return the index
        else
            return -1;
    }
}