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