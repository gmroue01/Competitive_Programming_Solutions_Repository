import sys


input = sys.stdin.readline

n,m = map(int,input().split())
grid = [input().rstrip('\n') for _ in range(n)]
visited = [[False]*m for _ in range(n)]


def dfs_iterative(sy,sx):

    stack = [(sy,sx)]

    while len(stack) > 0:
        sy_,sx_ = stack.pop()
        if not visited[sy_][sx_]:
            visited[sy_][sx_] = True
            for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                ny,nx = sy_ + dy, sx_ + dx
                if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '.' and not visited[ny][nx]:
         
                    stack.append((ny,nx))
        


count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and not visited[i][j]:
            count += 1
            dfs_iterative(i,j)
print(count)