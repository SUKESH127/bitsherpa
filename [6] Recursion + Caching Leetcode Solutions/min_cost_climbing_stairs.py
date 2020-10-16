#Problem: https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # RECURSIVE SOLUTION
        return minCost(len(cost), cost, {})

# Solution is quite standard (ie similar to fibonacci)
# note that I used a helper function and implemented the cache (ie in style Solution 2 from fibonacci)
# bc since this function has a non-primitive input (the costArray is a list), 
# using @lru_cache(None) wouldn't work     
def minCost(step, costArray, cache):
    # base cases
    if step == 0 or step == 1:
        return 0    
    
    # check cache
    if step in cache:
        return cache[step]
    
    # recursive breakdown - the cost of getting to any step i is whichever is less expensive: either 
    # getting to step i-1 and then paying cost[i-1] to get to i, or getting to step i-2 and paying cost[i-2] to get to i
    cache[step] = min(minCost(step-1, costArray, cache)+costArray[step-1], minCost(step-2, costArray, cache)+costArray[step-2])
    return cache[step]
        