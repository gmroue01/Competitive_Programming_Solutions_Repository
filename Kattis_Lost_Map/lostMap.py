"""
The code is implemented into the Sample input 1 from Kattis.
4
0 1 1 2
1 0 2 3
1 2 0 3
2 3 3 0
"""

n = 4


table = [
    [0 ,1 ,1 ,2]
    ,[1, 0 ,2 ,3]
    , [1,2,0,3]
    , [2,3,3 ,0]
]

graph = []

for i in range(n):
    for j in range(n):
        dist = table[i][j]
        graph.append([i,j, dist])

adj_list = []



















