class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        parents = list(range(rows * cols))

        size = [0] * (rows * cols)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size[cols * i + j] = 1

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)

            if pa != pb:
                size[pa] += size[pb]
                parents[pb] = pa

        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    idx = cols * i + j

                    if i > 0 and grid[i-1][j] == 1:
                        union(idx, cols * (i-1) + j)
                    if i < (rows - 1) and grid[i+1][j] == 1:
                        union(idx, cols * (i+1) + j)
                    if j > 0 and grid[i][j-1] == 1:
                        union(idx, cols * i + (j-1))
                    if j < (cols - 1) and grid[i][j+1] == 1:
                        union(idx, cols * i + (j+1))
        

        return max(size)




