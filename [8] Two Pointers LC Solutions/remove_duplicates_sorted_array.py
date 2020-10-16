# QUESTION: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    # SOLUTION: Not trivial. Since we need everything to
    # be in place, we use a two pointers approach. 
    
    # The upper pointer, j, is going to go through all the elements (it will be the "fast" pointer). 
    
    # The lower pointer, i, will always be pointing to the 
    # the last confirmed unique element. This is the loop invariant. 
    
    # We start i at 0 and j at 1. We increment j until arr[j] is different from arr[i].
    # When this happens, we know that arr[j] is at the next "distinct" element. Since we've found
    # a new unique element, we increment i and then set arr[i] to arr[j].

    #We continue until j has hit the end of the array. Since i points to the last uniquely seen 
    #element, i+1 will be the number of unique elements.
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i +=1
                nums[i] = nums[j]
        return i+1