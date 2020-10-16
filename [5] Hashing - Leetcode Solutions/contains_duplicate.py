#question: https://leetcode.com/problems/contains-duplicate/

#approach: 
# for each int, compare to all other ints
# seen so far by checking if the hash-set of 
# all ints observed contains the current int

#runtime: we are going through every element
#in nums, and for each one checking our hashset
#Thus runtime is o(n) * o(1) = o(n) where n is
#length of nums
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # again, we use the keys of a python dictionary
        # with throwaway values as our hash-set. 
        observed = {}
        for n in nums:
            if n in observed:
                return True
            observed[n] = 0
        return False