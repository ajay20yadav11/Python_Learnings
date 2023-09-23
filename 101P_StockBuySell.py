"""
write this hackerrank question, give solution here  below

A grocery store is selling apples by count.
They want to set the same price for each apple that they sell.
They received total N apples of different weight from the farm.

To be able to set the same price for each apple, they need to select only those set of apples where the weight different between the larget and the smallest apple is not more than K.
Given the range K, what is the maximum number of apples they can select from the N apples.

Input Format
Locked stub code in the editor reads the following input from stdin and passes it to the function:
The first line contains the range K.
The second line contains the number of apples N.
The subsequent lines contain size of each apple, one per line.

Output Fromat

The Function must return an interger specifying the maximum number of apples that can be selected from the input set of N apples which are all within a weight range of maximum K amoung each other

Sample input

2
8
4
2
6
100
101
101
110
102

Sample output 

4

Explanation 0

The above input specifies a maximum wight difference range of 2, and total 8 apples as input followed by their weights

3 different subsets are possible above which are all within weight different of 2:
- 2, 4
- 4, 6
- 100, 101, 101, 102

the maximum number of apples (the larget subset) is hence 4 100, 101, 101, 102
"""

from typing import List, Tuple


class ApplesBuySell:
    def __init__(self, apples_stock: List) -> None:
        self.apples_stock = apples_stock
        self.maximum_apples = 0
        self.k = self.apples_stock.pop(0)
        self.total_lengths = self.apples_stock.pop(0)
        self.apples_stock.sort()

    def __str__(self) -> str:
        return f"Maximum apples that can be selected are {self.maximum_apples}."

    def dp_calculate_maximum_apples(self) -> Tuple[List, int]:
        if len(self.apples_stock) <= 1:
            return len(self.apples_stock)

        selected_apples = [[apple] for apple in self.apples_stock]

        dp = [1] * self.total_lengths  # dp[i] represents the maximum number of apples that can be selected ending at index i
        
        for i in range(1, self.total_lengths):
            dp[i] = 1  # At least one apple can be selected
            selected_apples[i].append(self.apples_stock[i])  # Include the current apple
            for j in range(i-1, -1, -1):
                if abs(self.apples_stock[i] - self.apples_stock[j]) <= self.k:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        selected_apples[i] = selected_apples[j] + [self.apples_stock[i]]

        max_index = dp.index(max(dp))
        return selected_apples[max_index], len(selected_apples[max_index])  # Return the selected apples with maximum count

        # if self.maximum_apples:
        #     self.maximum_apples = maximum_apples
        # return self.maximum_apples

    def brute_force_maximum_apples(self) -> Tuple[List, int]:

        selected_apples = []
        max_count = 0
        
        for i in range(self.total_lengths):
            count = 1
            for j in range(i + 1, self.total_lengths):
                if self.apples_stock[j] - self.apples_stock[i] <= self.k:
                    count += 1

            if count > max_count:
                max_count = count   
                selected_apples = self.apples_stock[i:i + count]
        
        return selected_apples, max_count

    def sliding_window_calculate_maximum_apples(self) -> int:
        if len(self.apples_stock) <= 2:
            return len(self.apples_stock)

        max_apples = 0
        current_apples = 0
        for apple in range(1, self.total_lengths):
            if self.apples_stock[apple] - self.apples_stock[apple - current_apples] > self.k:
                current_apples -= 1
            current_apples += 1
            max_apples = max(max_apples, current_apples)

        return max_apples


if __name__ == '__main__':
    in_stock = [2, 8, 4, 2, 6, 100, 101, 101, 110, 102]
    # in_stock = [3, 10, 7, 4, 8, 5, 11, 6, 9, 12, 10, 13]
    apples = ApplesBuySell(in_stock)
    print('Using Sliding Window -> ', apples.sliding_window_calculate_maximum_apples())
    # print('Using Dynamic Progamming -> ', apples.dp_calculate_maximum_apples())  # Not correct or efficient or optimized
    print('Using Burte-Force Appraoch -> ', apples.brute_force_maximum_apples())

