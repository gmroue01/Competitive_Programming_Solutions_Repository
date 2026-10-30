import sys


def main():

    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    h = list(map(int,data[1: N+1]))

    dist = [0]*N

    for i in range(1,N):
        dist[i] = dist[i-1] + abs(h[i]-h[i-1])
        if i >= 2:
            dist[i] = min(dist[i],dist[i-2] + abs(h[i]-h[i-2]))
        
    print(dist[N-1])

main()