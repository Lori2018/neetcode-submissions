class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0;
        int sell = 0;
        int low = 0;

        for (int i = 0; i < prices.length; i++) {
            int diff = prices[sell] - prices[buy];
            if (prices[i] < prices[low]) {
                low = i;
            }

            if (prices[i] > prices[sell]) {
                if (low > buy) {
                    buy = low;
                }
                sell = i;
            } else if (prices[i] - prices[low] > diff) {
                buy = low;
                sell = i;
            }
        }

        return prices[sell] - prices[buy];
    }
}
