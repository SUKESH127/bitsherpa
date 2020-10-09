#question: https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Adi's scratchwork - walking through examples on the codepad
        # can ignore, but gives insight into me thinking about the problem
        # [4,5,6,7,0,1,2], find 0
        # lo=0,hi=6, mid=3, cur=7
        # lo=4,hi=6, mid=5, cur=1
        # lo=4,hi=4, mid=4
        
        
        # [3,1] find 1
        # lo = 0, hi = 1, mid = 0, cur=3
        
        # [6 7 10 12 0 1 2 3 4 5] -> find 3
        # [6 7 9 10 12 13 0 1 2 3 4 5] -> find 10


        if len(nums) is 0:
            return -1
        
        first = nums[0]
        lo = 0
        hi = len(nums)-1


        while (lo <= hi):
            mid = lo + (hi - lo)/2
            cur = nums[mid]
            
            if (cur == target):
                return mid
            
            if (target >= first and cur < first):
                hi = mid - 1
                continue
            
            if (target < first and cur >= first):
                lo = mid + 1
                continue
                
            if (cur < target):
                lo = mid + 1
                continue
            
            if (cur > target):
                hi = mid -1
                continue
        
        return -1