def maxSubArray(nums):
    max_sum = float('-inf')  # Initialize the maximum sum to a very small value
    current_sum = 0  # Initialize the current sum to 0

    for num in nums:
        current_sum = max(num, current_sum + num)  # Update the current sum by taking the maximum between the current number and the sum so far
        max_sum = max(max_sum, current_sum)  # Update the maximum sum if the current sum is larger

    return max_sum

# Test the function with examples
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1, 2, 3, 4, -10, 5, 6, 7]

print(maxSubArray(nums1))  # Output: 6 (the subarray [4, -1, 2, 1] has the largest sum)
print(maxSubArray(nums2))  # Output: 18 (the subarray [1, 2, 3, 4] has the largest sum)
