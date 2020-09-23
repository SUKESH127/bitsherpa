class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for each int, compare to all other ints
        # seen so far by checking if the hash-set of 
        # all ints observed contains the current int

        # again, we use the keys of a python dictionary
        # with throwaway values as our hash-set. 
        observed = {}
        for n in nums:
            if n in observed:
                return True
            observed[n] = 0
        return False