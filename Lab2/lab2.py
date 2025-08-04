# count_islands.py
# Function to count islands in a grid using DFS

def countIslands(grid):
    def isSafe(gd, r, c, visited):
        row = len(gd)
        col = len(gd[0])
        return (0 <= r < row) and (0 <= c < col) and (gd[r][c] == 'L' and not visited[r][c])

    def dfs(gd, r, c, visited):
        # DFS logic with all 8 possible directions
        rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[r][c] = True
        for k in range(8):
            nr = r + rNbr[k]
            nc = c + cNbr[k]
            if isSafe(gd, nr, nc, visited):
                dfs(gd, nr, nc, visited)

    row = len(grid)
    col = len(grid[0])
    visited = [[False for _ in range(col)] for _ in range(row)]
    count = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'L' and not visited[i][j]:
                dfs(grid, i, j, visited)
                count += 1

    return count
