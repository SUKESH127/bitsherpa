class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastSeenMap = {}
        for i,n in enumerate(nums):
            if (n in lastSeenMap and i - lastSeenMap[n] <= k):
                return True
            lastSeenMap[n] = i
        return False
        