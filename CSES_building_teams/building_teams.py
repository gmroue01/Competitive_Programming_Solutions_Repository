import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    n,m = int(data[0]),int(data[1])

    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = int(data[2 + 2*i]) - 1, int(data[3 + 2*i]) - 1
        adj[u].append(v)
        adj[v].append(u)

    colors = [0]*n
    q = deque()
 



    for s in range(n):
        if colors[s]:
            continue

        colors[s] = 1
        q.append(s)
        while q:
            u= q.popleft()



            for v in adj[u]:
                if colors[v] == 0:
                    colors[v] = 3 - colors[u]  
                    q.append(v)
                elif colors[v] == colors[u]:
                    print("IMPOSSIBLE")
                    return
                
    print(' '.join(map(str,colors)))

    
main()