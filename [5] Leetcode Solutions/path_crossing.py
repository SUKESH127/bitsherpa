class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # this is our starting position
        x = 0 
        y = 0
        
        # we use a visited dictionary as a HashSet
        # to keep track of all of the positions we have visited
        visited = {}
        visited['00'] = 0
        
        for dir in path:
            if dir == 'N':
                y += 1
            if dir == 'S':
                y -= 1
            if dir == 'E':
                x += 1
            if dir == 'W':
                x -=1
            pos = str(x) + str(y)
            
            # at every new position, we check if we've been there already
            # with our hash-set. if not, add it to the hash-set
            if pos in visited:
                return True
            visited[pos] = 0
        
        return False
        