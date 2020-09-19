class Solution:
    # QUESTION: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
    
    # SOLUTION: Brute-force: we double for loop to look at every pair of two elements,
    # and keep track of the maximum observed product
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float('-inf')
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                curProduct = (nums[i]-1)*(nums[j]-1)
                if curProduct > maxProduct:
                    maxProduct = curProduct
                    
                    
        return maxProduct