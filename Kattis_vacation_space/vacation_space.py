n = int(input())
locations = list(map(int,input().split()))

house_location = dict()

for i,v in enumerate(locations):
    house_location[i+1] = v

sorted_house_location = dict(sorted(house_location.items(),key=lambda item : item[1]))

succ = {}
