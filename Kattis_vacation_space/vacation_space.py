n = int(input())

# TODO : Refactor this code into one line in order to create directly the dict ?
# start refactor 
locations = list(map(int,input().split()))

house_location = dict()

for i,v in enumerate(locations):
    house_location[i+1] = v
# end refactor


sorted_house_location = dict(sorted(house_location.items(),key=lambda item : item[1]))
# print(sorted_house_location) : {3: 1, 2: 3, 1: 4, 4: 7, 6: 10, 5: 11}
print(sorted_house_location)


graph = list(sorted_house_location.keys())

succ = [0]*len(graph)
for i in range(len(graph)):
    # The loop is not working. Index out of range on the graph[i] or succ
    succ[graph[i]] = graph[i+1]
print(succ)