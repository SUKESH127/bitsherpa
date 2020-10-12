#question: https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) is 0:
            return -1
        
        # modified binary search
        # there are two sections: the part bigger than FIRST element, and the part less than FIRST element
        # if target is less than FIRST, it will be found to the right of the pivot.
        # if target is greater than FIRST, it will be found to the left of the pivot
        
        # Approach #1 - we use a binary search to find the pivot
        # pivot is clearly demarcated as a local minima. 
        # if current is less than FIRST, we know we need to go left 
        # if current is greater than FIRST, we have to go RIGHT
        # Once the pivot is identified, we either do a normal binary search to the section of nums either before or after the pivot
        first = nums[0]
        if target == first:
            return 0
        
        #This first modified binary search finds us the pivot
        lo = 1
        hi = len(nums)-1    
        lMin = len(nums) # this is necessary to deal w/ the edge case where there is no pivot
        
        while (lo <= hi):
            mid = lo + int((hi-lo)/2)
            if nums[mid] < nums[mid-1]:
                lMin = mid
                break
            elif nums[mid] > first:
                lo = mid+1
            else:
                hi = mid-1
        
        # This second binary search is just a regular binary search,
        # but limited to either before or after the pivot
        lo = lMin if target < first else 0
        hi = len(nums)-1 if target < first else lMin-1
        while (lo <= hi):
            mid = lo + int((hi-lo)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        
        return -1
        
        

# Alternatively, we can do a single, more significantly
# modified binary search that combines the functionalities of the two searches above. It's elegant and
# saves writing some boilerplate code, but to me it's a little
# more logically challenging to think about the different cases for whether to go left or right.
# Therefore in a realy interview I'd probably use the first approach bc it's easier to compartmentalize the logic.
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
            #happy case
            if (cur == target):
                return mid
            
            # We will HIT the first two of these cases if we are currently in the
            # incorrect "half" of the array.

            # if the target element is greater than first element, this means
            # that it can onlly be found BEFORE the pivot. But if the current element
            # is less than the first element, this means we are currently
            # post-pivot, which means we need to go left.
            if (target >= first and cur < first):
                hi = mid - 1
                continue
            
            # if the target element is less than the first element, it 
            # means the target has to be found AFTER the pivot if it does exist.
            # If the current element is greater or equal to the first element,
            # it means that we are currently BEFORE the pivot. Thus we need to move right.
            if (target < first and cur >= first):
                lo = mid + 1
                continue

            # If we've reached here, it means we are actually in the correct "half" of the array
            # we just apply normal binary search logic - go right if we are too big, left if
            # we are too small
            if (cur < target):
                lo = mid + 1
                continue
            
            if (cur > target):
                hi = mid -1
                continue
        
        return -1