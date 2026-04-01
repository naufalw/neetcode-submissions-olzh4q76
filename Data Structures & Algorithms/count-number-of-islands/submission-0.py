class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        result = 0

        # x is row, y is col
        def recurse(x, y):
            if (x, y) not in visited and int(grid[x][y]) == 1:
                visited.add((x,y))

                if x > 0:
                    recurse(x-1, y)
                if x < (rows - 1):
                    recurse(x+1, y)
                if y > 0:
                    recurse(x, y-1)
                if y < (cols - 1):
                    recurse(x, y+1)
        
        for i in range(rows):
            for j in range(cols):
                if int(grid[i][j]) == 1 and (i, j) not in visited:
                    result += 1
                    recurse(i, j)

        return result
