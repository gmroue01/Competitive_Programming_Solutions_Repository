import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
grid = [input().rstrip('\n') for _ in range(n)]

visited = [[False]*m for _ in range(n)]

direction = {(1,0): "U",(0,1):"R",(-1,0):"D",(0,-1):"L"}




def bfs(sy,sx):
    stop = False
    q = deque([(sy,sx)])
    count = 0
    path = []
    while q or stop:
        y,x = q.popleft()
        if stop:
            break
        for dy,dx in ((1,0),(0,1),(-1,0),(0,-1)):
            ny,nx = y + dy , x+ dx
            if 0 <= ny < n and 0 <= nx < m and (grid[ny][nx] == '.' or grid[ny][nx] == 'B') and not visited[ny][nx]: 
                visited[ny][nx] = True
                if grid[ny][nx] == 'B':
                    stop = True
                q.append((ny,nx))
                count += 1
                path.append(direction[(dy,dx)])


    return stop, count,path


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A' and not visited[i][j]:
           found_path, lenght, shortest_path = bfs(i,j) 

if not found_path:
    print("NO")
else:
    print("YES")
    print(lenght)
    print(''.join(shortest_path))