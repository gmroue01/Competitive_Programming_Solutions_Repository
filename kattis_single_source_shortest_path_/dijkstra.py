import sys 
from collections import deque




def main():
    data = sys.stdin.buffer.read().split()
    n,m,q,s = int(data[0]),int(data[1]),int(data[2]),int(data[3])

    idx = 4
    
    adj = [[] for _ in range(n)]  

    def dijkstra(adj,src):
        dist = [float('inf')]*(n)

        dist[src] = 0
        q = deque([(src,0)])

        while q:
            u,d = q.popleft()

            if d > dist[u]:
                continue

            for v,w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    q.append((v,dist[v]))

        return dist

    for _ in range(m):
        u,v,w = int(data[idx]),int(data[idx+1]),int(data[idx+2])
        idx += 3
        adj[u].append((v,w))
    distance = dijkstra(adj,s)
    for _ in range(q):
        d_node = distance[int(data[idx])]
        idx += 1
        if d_node == float('inf'):
            print("Impossible")
        else:
            print(d_node)
    print()
    n,m,q,s = int(data[idx]),int(data[idx+ 1]),int(data[idx + 2]),int(data[idx + 3])
    idx += 4
    adj = [[] for _ in range(n)]  
    for _ in range(m):
        u,v,w = int(data[idx]),int(data[idx+1]),int(data[idx+2])
        idx += 3
        adj[u].append((v,w))
    distance = dijkstra(adj,s)
    for _ in range(q):
        d_node = distance[int(data[idx])]
        idx += 1
        if d_node == float('inf'):
            print("Impossible")
        else:
            print(d_node)
            

main()
