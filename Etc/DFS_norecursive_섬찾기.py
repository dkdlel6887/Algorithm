def numIslands(grid: List[List[str]]) -> int:
    # dfs 이용, 모든 좌표 확인 후 4방향 이동 불가시 answer += 1
    from collections import deque
    island = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if int(grid[i][j]) == 1:
                s = deque([(i, j)])
                while s:
                    y, x = s.pop()
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌
                    for dy, dx in directions:
                        row, col = y + dy, x + dx
                        if 0 <= row < n and 0 <= col < m and int(grid[row][col]) == 1:
                            grid[row][col] = -1
                            s.append((row, col))
                island += 1
    return island