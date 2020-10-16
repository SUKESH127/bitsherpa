#question: https://leetcode.com/problems/two-sum/

#approach: explained inline

#runtime: we are just going through nums and then accessing/adding to 
#our hashtable for each num. o(n) time. 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # our visited hash-table (python dictionary)
        # will contain every number seen so far, each mapped to the index it was observed at
        visited = {}

        # for each number in nums, check if our visited dictionary contains it's complement
        for i, num in enumerate(nums):
            if target - num in visited:
                return [visited[target-num], i]
            visited[num] = i