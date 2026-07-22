class Solution {
    public boolean isValid(String s) {
        Stack<Integer> stack = new Stack<>();
        String[] arr = s.split("");
        for (String a : arr) {
            int x = getBracket(a);
            if (x > 0) {
                stack.push(x);
            } else if (x < 0) {
                if (stack.isEmpty() || stack.pop() != x * -1) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public int getBracket(String bracket) {
        switch (bracket) {
            case "(":
                return 1;
            case ")":
                return -1;
            case "{":
                return 2;
            case "}":
                return -2;
            case "[":
                return 3;
            case "]":
                return -3;
        }
        return 0;
    }
}
