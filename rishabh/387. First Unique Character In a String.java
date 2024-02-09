package rishabh;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;

@SuppressWarnings("unused")
class Solution {
    public static void main(String[] args) {
        System.out.println(firstUniqCharBruteForce("lleetcode"));
        System.out.println(firstUniqCharUsingSets("leetcode"));
        System.out.println(firstUniqCharUsingDictionary("lleettcode"));
    }

    // Approach-3: Using dictionary
    // Time: O(n)
    // Space: O(n)
    public static int firstUniqCharUsingDictionary(String s) {
        // if you want to maintain order
        // LinkedHashMap<Character, Integer> counter = new LinkedHashMap<>();
        HashMap<Character, Integer> counter = new HashMap<>();

        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i ++) {
            if (counter.get(s.charAt(i)) == 1){
                return i;
            }
        }
        return -1;
    }

    // Approach-2: using 2 hashsets
    // Time: O(n)
    // Space: O(n)
    public static int firstUniqCharUsingSets(String s) {
        HashSet<Character> first = new HashSet<>();
        HashSet<Character> second = new HashSet<>();

        for (char c : s.toCharArray()) {
            if (!first.contains(c)){
                first.add(c);
            } else {
                second.add(c);
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (!second.contains(s.charAt(i))){
                return i;
            }
        }
        return -1;
    }

    // Brute Force
    // Time: O(n * n)
    // Space: O(n)
    public static int firstUniqCharBruteForce(String s) {
        for (int i = 0 ; i < s.length(); i ++) {
            boolean duplicate = false;
            for (int j = 0; j < s.length(); j ++) {
                if ((i != j) && (s.charAt(i) == s.charAt(j))) {
                        duplicate = true;
                    }
                }
            if (!duplicate) {return i;}
            }
        return -1;
        }
}
