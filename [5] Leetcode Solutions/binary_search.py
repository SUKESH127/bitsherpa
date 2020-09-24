#question: https://leetcode.com/problems/binary-search
#approach: binary search, using my personal preferred template - https://algs4.cs.princeton.edu/11model/BinarySearch.java.html

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while (lo <= hi):
            mid = lo + int((hi - lo)/2)
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid-1
            else:
                return mid
        
        return -1
        