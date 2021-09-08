class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        def dfs(grid,r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] == '0':
                return 0
            grid[r][c] = '0'
            dfs(grid,r-1,c)
            dfs(grid,r+1,c)
            dfs(grid,r,c-1)
            dfs(grid,r,c+1)
            return 1
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += dfs(grid,r,c)
        
        return count
