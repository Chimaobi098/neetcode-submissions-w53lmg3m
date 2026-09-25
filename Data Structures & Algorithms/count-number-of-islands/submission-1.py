class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         island = 0

#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
#                 return
#             else:
#                 grid[r][c] = '0'
#                 dfs(r - 1, c)
#                 dfs(r, c + 1)
#                 dfs(r + 1, c)
#                 dfs(r, c - 1)


#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1':
#                     island += 1
#                     dfs(r, c)

#         return island


        if not grid:
            return 0

        island = 0

        # area = 0
        # maxArea = 0

        rows, cols = len(grid) , len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            else:
                # area += 1
                # maxArea = max(area, maxArea)
                grid[r][c] = '0'
                dfs(r - 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
                dfs(r + 1, c)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # maxArea = max(area, maxArea)
                    # area = 0
                    island += 1
                    dfs(r, c)

        return island

        
        
        