n = int(input())
locations = list(map(int, input().split()))

if n == 1:
    print(1)
else:

    # Sort the house nbr according to its location in the street
    # h-1 bc the house nbr start to 1
    # Return a list of the house nbr sorted
    order = sorted(range(1, n + 1), key=lambda h: locations[h - 1])
    
    # List of the location sort according the order.
    x = [locations[h - 1] for h in order]

    # Compute the gaps between the house
    gaps = [x[i + 1] - x[i] for i in range(n - 1)]

    best_house = None
    best_dist = -1

    for i in range(n):
        if i == 0:
            dist = gaps[0]
        elif i == n - 1:
            dist = gaps[-1]
        else:
            dist = min(gaps[i - 1], gaps[i])

        h = order[i]
        if dist > best_dist or (dist == best_dist and h < best_house):
            best_dist = dist
            best_house = h

    print(best_house)