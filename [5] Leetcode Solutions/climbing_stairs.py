# approach: very simple recursive formulation to this problem, and then use
# memoiziation via python lru_cache library
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return Solution.climbStairs(self,n-2) + Solution.climbStairs(self,n-1)