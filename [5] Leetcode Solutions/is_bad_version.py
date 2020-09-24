# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

#question: https://leetcode.com/problems/first-bad-version/submissions/
#approach: just a modified binary search

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #edge case, n is 0
        if n <= 0:
            return -1
        
        # edge case, the first one is bad, return immediately
        # edge case in this implementation, because in my binary search
        # I'm always comparing isBadVersion(mid) to isBadVersion(mid-1)... I can't do this for isBadVersion(1) because isBadVersion(0) is invalid.
        if isBadVersion(1):
            return 1
        
        #binary search
        #initialize lo to second element since we already checked the edge case that the first one is the bad one
        #modified binary search w three cases:
        #mid is good -> move right
        #mid is bad, mid-1 is bad -> move left
        #mid is bad, mid-1 is good -> hit
        lo = 2
        hi = n
        while (lo <= hi):
            mid = lo + int((hi-lo)/2)
            if not isBadVersion(mid):
                lo = mid+1
            if isBadVersion(mid) and isBadVersion(mid-1):
                hi = mid-1
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
        
        return -1
        