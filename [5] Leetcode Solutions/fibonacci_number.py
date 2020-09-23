# Note: Highly recommend looking at the 3 solutions to understand your
# different high level options for coding up any recursion + memoiziation problem.

# Solution 1 -> using a class variable to store the cache for memoization
class Solution:
    cache = {}
    def fib(self, N: int) -> int:
        if N is 0:
            return 0
        if N is 1:
            return 1
        if N in Solution.cache:
            return Solution.cache[N]
        
        Solution.cache[N] = Solution.fib(self,N-1) + Solution.fib(self,N-2)
        return Solution.cache[N]

# Solution 2 (Recommended Style) - create a cache in the "driver" function and then use a recursive helper function
# (recommended over solution 1, especially if your interviewer asks not to use a "class" variable)
class Solution:
    def fib(self, N: int) -> int:
        # since the cache dictionary is non-primitive and passed in as an argument, it will persist.
        # This is because non-primitives (ie dictionaries, lists, objects) are passed
        # by reference.
        return fib(N, {}) 
    

def fib(N, cache):
    if N is 0 or N is 1:
        return N
    if N in cache:
        return cache[N]
    
    # since the return for this function hasn't already been computed and cached,
    # we want to add it in the cache after computing it and before returning it
    cache[N] = fib(N-1, cache) + fib(N-2, cache)
    return cache[N]

# Solution 3 - Recommended if whiteboard coding, and if interviewer is OK with using the library. 
# You can ask.
# We utilize the python existing LRU memoiziation functionality to automatically
# memoize the function. Note this only works for a function when the inputs are primitives,
# which is the case here because the input to fib is a number.
# I will default to this style wherever possible because it is the most concise, but it's important
# to understand how to do the caching yourself (ie write up Solution style 2) before using a python library.
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, N: int) -> int:
        if N is 0 or N is 1:
            return N
        return Solution.fib(self,N-1) + Solution.fib(self,N-2)

