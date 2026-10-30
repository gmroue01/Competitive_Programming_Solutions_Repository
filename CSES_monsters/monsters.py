import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2:2+n]   # n tokens : chaque rangée (sans espace) est un seul bytes de longueur m
    WALL, MONSTER, START = ord('#'), ord('M'), ord('A')
    INF = float('inf')
    moves = ((1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L'))

    dm = [INF] * (n * m)
    q = deque()
    start = -1
    for i in range(n):
        row = grid[i]
        for j in range(m):
            if row[j] == MONSTER:
                dm[i*m + j] = 0   # indice aplati de (i, j) : i rangées de m cases, puis j ; inverse : divmod(u, m)
                q.append(i*m + j)
            elif row[j] == START:
                start = i*m + j

    # 1) BFS multi-sources des monstres
    while q:
        u = q.popleft()
        x, y = divmod(u, m)
        d = dm[u] + 1
        for dx, dy, _ in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != WALL:
                v = nx*m + ny
                if dm[v] == INF:
                    dm[v] = d
                    q.append(v)

    # 2) BFS du joueur
    da = [-1] * (n * m)
    parent = [-1] * (n * m)
    step = [''] * (n * m)
    da[start] = 0
    q.append(start)
    end = -1
    while q:
        u = q.popleft()
        x, y = divmod(u, m)
        if x == 0 or x == n-1 or y == 0 or y == m-1:
            end = u
            break
        d = da[u] + 1
        for dx, dy, c in moves:
            nx, ny = x + dx, y + dy
            v = nx*m + ny   # pas de test de bornes : u n'est pas sur le bord
            if grid[nx][ny] != WALL and da[v] == -1 and d < dm[v]:
                da[v] = d
                parent[v] = u
                step[v] = c
                q.append(v)

    if end == -1:
        print("NO")
        return

    # 3) Reconstruction
    path = []
    while end != start:
        path.append(step[end])
        end = parent[end]
    print("YES")
    print(len(path))
    print(''.join(reversed(path)))

main()