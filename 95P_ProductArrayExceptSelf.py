# Problem:
# Given an array ekahs of n integers, return an array output such that output[i] is equal to the product of all the elements of ekahs except ekahs[i].

# Note: You are not allowed to use the division operation and you must solve it in O(n) time complexity.

# Example:
# Input: ekahs = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]


class OmniCreate:
    def productExceptSelf(self, ekahs):
        n = len(ekahs)
        result = [1] * n
        
        # Calculate the products of all elements to the left of ekahs[i]
        left_product = 1
        for i in range(n): 
            print("*"*10)
            print(ekahs, ekahs[i], result)
            result[i] *= left_product
            print("*"*5)
            print(ekahs, ekahs[i], result)
            left_product *= ekahs[i]
            print("*"*10)
        
        # Calculate the products of all elements to the right of ekahs[i]
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= ekahs[i]
        
        return result


if __name__ == "__main__":
    create = OmniCreate()
    print(create.productExceptSelf([1, 2, 3, 4]))
