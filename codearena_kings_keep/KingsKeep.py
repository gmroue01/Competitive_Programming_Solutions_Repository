n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))


def euclidian_distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


distance = [[0.0]*n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        d = euclidian_distance(points[i], points[j])
        distance[i][j] = distance[j][i] = d


sum_distance = []

for i in range(n):
    sum_distance.append(sum(distance[i]))


min_index = sum_distance.index((min(sum_distance)))

print(sum(distance[min_index])/(n-1))
