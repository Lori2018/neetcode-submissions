class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), 
                map.get(s.charAt(i)) == null ? 1 : 
                    map.get(s.charAt(i)) + 1);
        }
        System.out.println(map.toString());

        for (int i = 0; i < t.length(); i++) {
            map.put(t.charAt(i), 
                map.get(t.charAt(i)) == null ? -1 : 
                    map.get(t.charAt(i)) - 1);
        }
        Collection<Integer> vals = map.values();
        for (Integer i : vals) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}
