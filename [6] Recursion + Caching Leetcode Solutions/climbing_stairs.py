#question: https://leetcode.com/problems/climbing-stairs/

# approach: very simple recursive formulation to this problem, and then use
# memoiziation via python lru_cache library
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        #given that we can take either 1 or 2 steps, the number of ways to get to any 
        #step is equal to:
        #the number of ways to get to the step 2 steps prior PLUS the number of ways to get to the previous step
        return Solution.climbStairs(self,n-2) + Solution.climbStairs(self,n-1)