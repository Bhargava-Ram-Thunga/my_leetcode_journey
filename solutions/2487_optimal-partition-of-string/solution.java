class Solution {
    public int partitionString(String s) {
        int idx = 0;
        int count = 0;
        Map<Character, Boolean> mp = new HashMap<>(); 
        while (idx < s.length()) {
            if (mp.containsKey(s.charAt(idx))) { // if current character has already appeared in current substring
                count++; // increment count
                mp.clear(); // clear HashMap to start a new substring
            }
            mp.put(s.charAt(idx), true); // mark current character as seen
            idx++; // move to next character
        }
        return count + 1; // return number of substrings (add 1 because we need to count the last substring as well)
    }
}