import sys



def main():
    data = sys.stdin.buffer.read().split()
    n,t = int(data[0]),int(data[1])

 
    distance = [int(x) for x in data[2:2 + 2*n:2]]
    speed    = [int(x) for x in data[3:3 + 2*n:2]]

    s_mean = sum(speed)/n
    s_min = min(speed)
    D = sum(distance)

    def time_function(c):
        return sum([distance[i] / (speed[i] + c) for i in range(n)])
    
    def check(m):
        return time_function(m) >= 0 



    lo = (D/t) - s_mean
    hi = (D/t) - s_min

    while hi - lo > 1e-9:
        mid = (lo+hi) / 2 
        if mid in speed:
            continue
        if check(mid):
            hi = mid
        else:
            lo = mid

    print(lo)









    
main()