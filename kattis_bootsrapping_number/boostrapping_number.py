import sys

def main():
    data  = sys.stdin.buffer.read().split()
    n = int(data[0])


    lo,hi = 1.0,10.0

    for _ in range(100):
        mid = (lo+hi) /2
        if mid ** mid  < n:
            lo = mid
        else:
            hi = mid


    print(f"{lo:.10f}")







main()