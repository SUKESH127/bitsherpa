#question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# solution: we perform two modified binary searches to identify first/last elements. 

# note: it is possible and elegant to create a single function that performs both searches (which you can 
# just call from your main routine), but
# in the heat of the interview I personally feel much more comfortable taking the safer/less cognitively taxing/
# less complicated approach of keeping the left and right search logic separate. 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # perform two binary searches, the first to find the LEFTmost occurence,
        # the second to find the rightmost occurrence
        leftRet = -1
        rightRet = -1
        
        if nums is None or len(nums) is 0:
            return [-1,-1]
        
        # to find the leftmost occurence, we have to find the spot where
        # the current element equals the target, and the element to it's left is LESS than
        # the target, we're done!. If the element to the left also equals target, move LEFT. 
        # If current element is bigger than target, move LEFT
        # If current element is less than target, move RIGHT
        
        # Too handle edge cases, we start the search from the 2nd element. If first element does 
        # equal target, we just return it. 
        if nums[0] == target:
            leftRet = 0
        else:
            lo = 1
            hi = len(nums)-1
            while (lo <= hi):
                mid = lo + int((hi-lo)/2)
                if nums[mid] == target:
                    if nums[mid-1] != target:
                        leftRet = mid
                        break
                    else:
                        hi = mid-1
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
        
        #if no leftmost value is find, means the target doesn't exist, so let's just return early
        if leftRet == -1:
            return [-1,-1]
        
        # repeat very similar logic (modified binary search) to find the rightmost target
        if nums[-1] == target:
            rightRet = len(nums)-1
        else:
            lo = 0
            hi = len(nums)-2
            while (lo <= hi):
                mid = lo + int((hi-lo)/2)
                if nums[mid] == target:
                    if nums[mid+1] != target:
                        rightRet = mid
                        break
                    else:
                        lo = mid+1
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
        
        return [leftRet, rightRet]