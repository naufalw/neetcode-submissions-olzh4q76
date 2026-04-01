class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        parent = list(range(rows * cols))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    idx = cols * i + j

                    if i > 0 and grid[i-1][j] == '1':
                        union(idx, cols * (i-1) + j)
                    if i < (rows - 1) and grid[i+1][j] == '1':
                        union(idx, cols * (i+1) + j)
                    if j > 0 and grid[i][j-1] == '1':
                        union(idx, cols * i + (j-1))
                    if j < (cols - 1) and grid[i][j+1] == '1':
                        union(idx, cols * i + (j+1))
        
        return sum(
            find(cols * i + j) == cols *i+j
            for i in range(rows)
            for j in range(cols)
            if grid[i][j] == '1'
        )