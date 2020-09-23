class Solution:
    # QUESTION: https://leetcode.com/problems/running-sum-of-1d-array/
    
    # SOLUTION: Straightforward, literally perform a running sum 
    # by looping through nums and adding each iterative running sum to
    # the retrun array
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = [nums[0]]
        for i in range(1,len(nums)):
            runSum.append(nums[i] + runSum[i-1])
        return runSum
        
        