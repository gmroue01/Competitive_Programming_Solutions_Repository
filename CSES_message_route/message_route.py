import sys
from collections import deque






def main():
    data = sys.stdin.buffer.read().split()

    n,m = int(data[0]),int(data[1])


    adj = [[] for _ in range(n)]
    visited = [False]*n
    parents = list(range(n))
    for i in range(2,2+ 2*m,2):
        u,v = int(data[i])-1,int(data[i+1])-1
        adj[u].append(v)
        adj[v].append(u)
   
    q = deque([(0)])
    visited[0] = True

    POSSIBLE = False
    while q:
        node = q.popleft()
        if node == n-1:
            POSSIBLE = True
            break

        for neighbour in adj[node]:
            if not visited[neighbour]:
                parents[neighbour] = node
                visited[neighbour] = True
                q.append(neighbour)

    

    if not POSSIBLE:
        print("IMPOSSIBLE")
    else:
        idx = n-1
        path = [n]
        
        while idx != 0:
            path.append(parents[idx]+1)
            idx = parents[idx]
        path.reverse()
        print(len(path))
        print(' '.join(map(str,path)))

main()