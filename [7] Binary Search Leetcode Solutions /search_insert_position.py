#question: https://leetcode.com/problems/search-insert-position/submissions/
#approach: modified binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        #handle edge case where nums is empty
        if len(nums) is 0:
            return -1
        
        #handle edge case where first element is the solution
        if target <= nums[0]:
            return 0
        
        #handle edge case where target is treater than everything in the list
        if target > nums[len(nums)-1]:
            return len(nums)
        
        #modified binary search
        #binary search w/ an extra case
        #mid = target -> return mid
        #mid greater than target, mid-1 less than target -> return mid
        #mid greater than target, mid-1 also greater than target -> go left
        #mid less than target -> go right
        lo = 1
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + int((hi-lo)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target and nums[mid-1] < target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        
        