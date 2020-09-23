#Problem: https://leetcode.com/problems/minimum-path-sum/ 

#Approach: quite similar to the min_cost climbing stairs problem,
#except that we are now operating in a 2D function space. 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cache = [[-1]*n for i in range(m)]
        return minPathSum(grid, m-1, n-1, cache)


# using recursion plus memoization!
# the main challenge here, besides figuring out the recurrence relation,
# is making sure that you're base cases are exhaustive so that you don't
# go out of bounds of the 2D array or get incorrect results from doing so.
# I explicitly laid out the bounds by writing bases cases for the top row
# and left column.
def minPathSum(grid, i, j, cache):
    #first check cache hit
    if cache[i][j] != -1:
        return cache[i][j] 
    
    # base case, the top left square
    if i is 0 and j is 0:
        cache[0][0] = grid[0][0]
        return cache[0][0]
    
    # base cases - the top row and the left column
    if i is 0:
        cache[0][j] = grid[0][j] + minPathSum(grid,0,j-1, cache)
        return cache[0][j]
    
    if j is 0:
        cache[i][0] = grid[i][0] + minPathSum(grid, i-1, 0, cache)
        return cache[i][0]
    
    # Recurrence relation: the minSum of any square is going to the value of the square itself, plus 
    # whichever is smaller: either the minSum of getting to the square to the left,
    # or the minSum of getting to the square above.
    cache[i][j] = grid[i][j] + min(minPathSum(grid,i-1,j,cache), minPathSum(grid, i, j-1, cache))
    return cache[i][j]
        