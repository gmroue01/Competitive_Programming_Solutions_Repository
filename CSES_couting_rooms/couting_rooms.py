import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().rstrip('\n') for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(sy, sx):
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and not visited[i][j]:
            count += 1
            bfs(i, j)

print(count)