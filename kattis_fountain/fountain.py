import sys
from collections import deque



def main():
    data = sys.stdin.buffer.read().split()
    n , m = int(data[0]),int(data[1])


    grid = [bytearray(row) for row in data[2:2+n]]
    WATER = ord('V')
    STONE = ord('#')
    AIR = ord('.')

    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == WATER:
                q.append((i,j))


    while q:
        i,j = q.popleft()
        nx,ny = i+1,j
        if i +1 >= n:
            continue
        if grid[nx][ny] == AIR:
            grid[nx][ny] = WATER
            q.append((nx,ny))
        if grid[nx][ny] == STONE:
            for dy in (j-1,j+1):
                if 0 <= dy < m and grid[i][dy] == AIR:
                    grid[i][dy] = WATER
                    q.append((i,dy))

    for row in grid:
        print(row.decode())

main()      