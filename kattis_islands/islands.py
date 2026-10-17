import sys
from collections import deque

def main():
    data = sys.stdin.buffer.readline().split()
    n,m = int(data[0]),int(data[1])
    grid = [bytearray(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]
    count = 0
    L, C = ord('L'), ord('C')
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == L and not visited[i][j]:
                count += 1
                q = deque([(i,j)])
                visited[i][j] = True
                while q:
                    x,y = q.popleft()
                    for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and (grid[nx][ny] == L or grid[nx][ny] == C ):
                            q.append((nx,ny))
                            visited[nx][ny] = True
    
    print(count)







main()