import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

grid = []
sy = None
sx = None
ey = None
ex = None

visited = [[False]*m for _ in range(n)]

for i in range(n):
    line = input().rstrip('\n')
    if 'A' in line:
        sy = i
        sx = line.index('A')
    if 'B' in line:
        ey = i
        ex = line.index('B')

    grid.append(line)


def neighbour(y,x):
    for dy,dx  in ((1,0),(0,1),(-1,0),(0,-1)):
        cy = y + dy
        cx = x + dx

        if cy < 0 or cy >= n: continue
        if cx < 0 or cx >= m: continue
        if grid[cy][cx] == "#":continue
        if visited[cy][cx] : continue

        visited[cy][cx] = True
        q.append((cy,cx))
        prev[cy][cx] = (y,x)

def reconstruct_path(ey,ex,sy,sx,prev):
    path = []
    index_y = ey
    index_x = ex
    path.append((ey,ex))
    while (index_y, index_x) != (sy, sx):
        node = prev[index_y][index_x]
        path.append(node)
        index_y = node[0]
        index_x = node[1]

    

    path.reverse()
    return path


def path_direction(path):
    """path est ordonné A -> B, donc aucune inversion ici."""
    d = {(-1, 0): "U", (1, 0): "D", (0, -1): "L", (0, 1): "R"}
    return ''.join(
        d[(path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])]
        for i in range(len(path) - 1)
    )
    



q = deque([(sy,sx)])
visited[sy][sx] = True

prev = [[None]*m for _ in range(n)]
reached_end = False
while q:
    ny,nx = q.popleft()

    if grid[ny][nx] == "B":
        reached_end = True
        break
    neighbour(ny,nx)


if None in [ex,ey,sx,sy]:
    print("NO")
elif reached_end:
    path = reconstruct_path(ey,ex,sy,sx,prev)
    print("YES")
    print(len(path)-1)
    print(path_direction(path))
    
else:
    print("NO")