class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

# QUESTION: https://leetcode.com/problems/remove-element/submissions/
# #Approach #1, we iterate through the array and identify all matching indexes, 
# #then use DEL or pop() to remove those indexes
#         toRemove = []
#         for i,n in enumerate(nums):
#             if n == val:
#                 toRemove.append(i)
#         #we delete in reversed order so that we don't shift around the earlier indices
#          #and thus remove the wrong elements
#         for i in reversed(toRemove):
#             del nums[i]

#         return len(nums)

# Approach 2 - Use a pointer based approach and shift elements in place. Elegant and in place.
# Whenever we find a value that should be KEPT, we increment our pointer
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p