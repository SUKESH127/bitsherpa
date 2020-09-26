# question: https://leetcode.com/problems/unique-paths/
# approach: standard recursion + memoiziation

# runtime: o(m+n) thanks to caching - we compute
# the unique paths number to every square in the 2D array
# exactly once, and each computation is constant time (either
# a base case or an addition of two numbers)
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        #for the first row or first column, there's
        #only one path to get to any of those squares
        if m is 1 or n is 1:
            return 1

        # for any other square, the number of paths to it
        # is the number of paths to the square above PLUS
        # the number of paths to the square to the LEFT.
        return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)