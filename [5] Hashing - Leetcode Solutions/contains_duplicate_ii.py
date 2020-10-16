#question: https://leetcode.com/problems/contains-duplicate-ii/

#approach: similar to contains-duplicate - we just maintain a visited number hashMap,
#but now store the array-index of each visited number as the dictionary value. We
#can then check whether, when we observe a duplicate, the index of the duplicates 
#are sufficiently "near" each other.

#runtime: we are going through every element
#in nums, and for each one checking/adding to our hashset and doing other
#constant time work. Thus runtime is o(n) where n is length of nums. 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastSeenMap = {}
        
        for i,n in enumerate(nums):
            if n in lastSeenMap and i - lastSeenMap[n] <= k:
                return True
            lastSeenMap[n] = i
        return False
        