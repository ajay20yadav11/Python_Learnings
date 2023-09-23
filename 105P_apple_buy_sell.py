# You are given an array prices, where prices[i] represents the price of a stock on the i-th day. You want to maximize your profit by buying and selling the stock at the right time. You may complete as many transactions as you like (buy one stock and sell one stock multiple times).

# However, you must sell the stock before you buy again. That means, you cannot hold multiple stocks at the same time. If you were to buy on the i-th day, you cannot sell on the i-th day. After selling, you can buy again on the next day or any future day.

# Your task is to find the maximum profit that can be achieved by buying and selling the stock.

# Example:
# Let's consider an example with the input array prices = [7, 1, 5, 3, 6, 4]. The following transactions can be made to maximize the profit:

# Buy on day 2 (price = 1) and sell on day 3 (price = 5) to earn a profit of 5 - 1 = 4.
# Buy on day 4 (price = 3) and sell on day 5 (price = 6) to earn a profit of 6 - 3 = 3.
# Total profit = 4 + 3 = 7.

class Apples:
    def dyn_apple_buy_sell(self, apples: list) -> int:
        """
        Using Dynamic Programming Approach
        """
        if not apples:
            return 0

        # Initialize an empty array of length of apples
        dp = [0] * len(apples)
        dp[0] = 0

        for i in range(1, len(apples)):
            # Calculate the profit for each day by comparing current price with previous day's profit
            dp[i] = max(dp[i-1], dp[i-1] + apples[i] - apples[i-1])

        return dp[-1]  # Return the maximum profit

    @staticmethod
    def apple_buy_sell(apples: list) -> int:
        if not apples:
            return 0

        max_profit = 0

        for i in range(1, len(apples)):
            # Calculate the profit for each day by comparing current price with previous day's price
            profit = apples[i] - apples[i-1]
            
            # Only accumulate positive profits to get the maximum profit
            if profit > 0:
                max_profit += profit

        return max_profit

    @staticmethod
    def slid_win_apple_buy_sell(apples: list) -> int:
        """
        Using sliding window approach
        This only calculate maximun profit in a particular day
        """
        minimum_price = apples[0]
        maximum_profit = 0

        for current_apple in apples[1:]:
            if current_apple > minimum_price:
                maximum_profit = max(maximum_profit, current_apple - minimum_price)
            else:
                minimum_price = current_apple

        return maximum_profit


if __name__ == '__main__':
    in_stock = [7, 1, 5, 3, 6, 4]
    dynamic_app = Apples()
    print('Using Dynamic Programming Approach ->', dynamic_app.dyn_apple_buy_sell(in_stock))
    print('Using Sliding Window Approach ->', dynamic_app.slid_win_apple_buy_sell(in_stock))
    print('Using Positive Profits Approach ->', dynamic_app.apple_buy_sell(in_stock))
