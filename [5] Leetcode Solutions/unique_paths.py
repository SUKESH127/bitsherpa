from functools import lru_cache
class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m is 1 or n is 1:
            return 1
        return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)