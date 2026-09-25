class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        res = 0
        rows, cols = len(grid) , len(grid[0])

        def dfs(r, c, area):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 0

            return 1 + dfs(r - 1, c, area) + dfs(r, c - 1, area) + dfs(r, c + 1, area) + dfs(r + 1, c, area)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c, 0)
                    res = max(res, area)


        return res



        
        