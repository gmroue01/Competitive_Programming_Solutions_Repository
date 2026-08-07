n = int(input())

table = []

for _ in range(n):
    line = list(map(int, input().split()))
    table.append(line)


visited = [False]*n
min_dist = [float('inf')]*n
parent = [-1]*n

min_dist[0] = 0
edges = []

for _ in range(n):
    # je cherche un nouveau parent
    u = -1
    for v in range(n):
        if not visited[v] and (u == -1 or min_dist[v] < min_dist[u]):
            u = v

    visited[u] = True
    if parent[u] != -1:
        edges.append((parent[u], u))

    for v in range(n):
        # Avec ce nouveau parent u tu as trouvé une distance plus petite.
        if not visited[v] and table[u][v] < min_dist[v]:
            min_dist[v] = table[u][v]
            parent[v] = u


for i in range(n-1):

    print(edges[i][0] + 1, edges[i][1] + 1)
