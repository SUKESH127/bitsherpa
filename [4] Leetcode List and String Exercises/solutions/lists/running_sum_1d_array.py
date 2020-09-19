class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = [nums[0]]
        for i in range(1,len(nums)):
            runSum.append(nums[i] + runSum[i-1])
        return runSum
        
        