class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> sol = new ArrayList<>();

        for (String str : strs) {
            boolean found = false;
            for (int i = 0; i < sol.size(); i++) {
                if (isAnagram(str, sol.get(i).get(0))) {
                    sol.get(i).add(str);
                    found = true;
                    break;
                }
            }

            if (!found) {
                ArrayList<String> list = new ArrayList<>();
                list.add(str);
                sol.add(list);
            }

        }

        return sol;
    }

    public boolean isAnagram(String x1, String x2) {
        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < x1.length(); i++) {
            if (map.get(x1.charAt(i)) == null) {
                map.put(x1.charAt(i), 1);
            } else {
                map.replace(x1.charAt(i), map.get(x1.charAt(i)) + 1);
            }
        }

        for (int i = 0; i < x2.length(); i++) {
            if (map.get(x2.charAt(i)) == null || map.get(x2.charAt(i)) <= 0) {
                return false;
            }

            map.put(x2.charAt(i), map.get(x2.charAt(i)) - 1);

            if (map.get(x2.charAt(i)) == 0) {
                map.remove(x2.charAt(i));
            }
        }

        return map.isEmpty();
    }
}
